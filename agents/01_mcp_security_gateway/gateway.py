from __future__ import annotations
from core.models import Decision, PolicyDecision
from core.policies import PolicyEngine

class MCPSecurityGateway:
    """Policy boundary for MCP capabilities before execution."""
    def __init__(self, policy: PolicyEngine | None = None) -> None: self.policy = policy or PolicyEngine()
    def authorize(self, tool_name: str) -> PolicyDecision: return self.policy.evaluate(tool_name)
    def allowed(self, tool_name: str) -> bool: return self.authorize(tool_name).decision is Decision.ALLOW
