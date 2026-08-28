from __future__ import annotations
import asyncio
from time import perf_counter
from typing import Any
from core.models import Decision, ToolCall, ToolResult
from core.policies import PolicyEngine
from core.runtime import ToolRegistry
from security.prompt_injection import PromptInjectionFirewall

class ToolExecutor:
    """Single guarded execution path for every tool call."""
    def __init__(self, registry: ToolRegistry, policy: PolicyEngine | None = None, timeout_seconds: float = 30.0) -> None:
        self.registry = registry
        self.policy = policy or PolicyEngine()
        self.timeout_seconds = timeout_seconds
        self.injection = PromptInjectionFirewall()

    async def execute(self, call: ToolCall) -> ToolResult:
        decision = self.policy.evaluate(call.tool)
        if decision.decision is not Decision.ALLOW:
            return ToolResult(call_id=call.id, success=False, error=f"Blocked: {decision.reason}")
        tool = self.registry.get(call.tool)
        start = perf_counter()
        try:
            result = await asyncio.wait_for(tool.execute(call), timeout=self.timeout_seconds)
            result.duration_ms = int((perf_counter() - start) * 1000)
            return result
        except asyncio.TimeoutError:
            return ToolResult(call_id=call.id, success=False, error="Tool execution timed out", duration_ms=int((perf_counter()-start)*1000))
        except Exception as exc:
            return ToolResult(call_id=call.id, success=False, error=f"Tool execution failed: {type(exc).__name__}", duration_ms=int((perf_counter()-start)*1000))

    def inspect_external_text(self, text: str) -> tuple[bool, list[str]]:
        return self.injection.inspect(text)
