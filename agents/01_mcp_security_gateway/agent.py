from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from core.models import Decision, PolicyDecision, ToolCall
from core.policies import PolicyEngine

@dataclass
class MCPRequest:
    tool: str
    arguments: dict[str, Any]

class MCPSecurityGateway:
    """Authorize MCP tool calls before they reach an MCP server."""
    def __init__(self, policy: PolicyEngine | None = None) -> None:
        self.policy = policy or PolicyEngine()
    def authorize(self, request: MCPRequest) -> PolicyDecision:
        return self.policy.evaluate(request.tool)
    def to_tool_call(self, request: MCPRequest) -> ToolCall:
        return ToolCall(tool=request.tool, arguments=request.arguments)
