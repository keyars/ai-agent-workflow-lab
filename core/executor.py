from __future__ import annotations
import asyncio
from time import perf_counter
from core.models import AuditEvent, Decision, ToolCall, ToolResult
from core.policies import PolicyEngine
from core.runtime import ToolRegistry
from observability.audit import AuditSink, audit_event
from security.prompt_injection import PromptInjectionFirewall

class ToolExecutor:
    """Single guarded execution path for every tool call."""
    def __init__(self, registry: ToolRegistry, policy: PolicyEngine | None = None, timeout_seconds: float = 30.0, audit: AuditSink | None = None) -> None:
        self.registry = registry
        self.policy = policy or PolicyEngine()
        self.timeout_seconds = timeout_seconds
        self.injection = PromptInjectionFirewall()
        self.audit = audit

    def _emit(self, event: AuditEvent) -> None:
        if self.audit: self.audit.emit(event)

    async def execute(self, call: ToolCall) -> ToolResult:
        decision = self.policy.evaluate(call.tool)
        self._emit(audit_event("tool.policy_decision", "tool-executor", tool=call.tool, decision=decision.decision.value, risk=decision.risk.value))
        if decision.decision is not Decision.ALLOW:
            self._emit(audit_event("tool.blocked", "tool-executor", tool=call.tool, reason=decision.reason))
            return ToolResult(call_id=call.id, success=False, error=f"Blocked: {decision.reason}")
        tool = self.registry.get(call.tool)
        start = perf_counter()
        self._emit(audit_event("tool.started", "tool-executor", call_id=call.id, tool=call.tool, arguments=call.arguments))
        try:
            result = await asyncio.wait_for(tool.execute(call), timeout=self.timeout_seconds)
            result.duration_ms = int((perf_counter() - start) * 1000)
            self._emit(audit_event("tool.completed", "tool-executor", call_id=call.id, tool=call.tool, success=result.success, duration_ms=result.duration_ms))
            return result
        except asyncio.TimeoutError:
            duration = int((perf_counter()-start)*1000)
            self._emit(audit_event("tool.timeout", "tool-executor", call_id=call.id, tool=call.tool, duration_ms=duration))
            return ToolResult(call_id=call.id, success=False, error="Tool execution timed out", duration_ms=duration)
        except Exception as exc:
            duration = int((perf_counter()-start)*1000)
            self._emit(audit_event("tool.failed", "tool-executor", call_id=call.id, tool=call.tool, error_type=type(exc).__name__, duration_ms=duration))
            return ToolResult(call_id=call.id, success=False, error=f"Tool execution failed: {type(exc).__name__}", duration_ms=duration)

    def inspect_external_text(self, text: str) -> tuple[bool, list[str]]:
        return self.injection.inspect(text)
