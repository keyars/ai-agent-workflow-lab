from core.models import ToolCall, PolicyDecision
from core.policies import PolicyEngine

class MCPSecurityGateway:
    name = "mcp-security-gateway"
    def authorize(self, call: ToolCall) -> PolicyDecision:
        return PolicyEngine().evaluate(call.tool)
