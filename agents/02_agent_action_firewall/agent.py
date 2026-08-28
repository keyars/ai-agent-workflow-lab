from security.action_firewall import ActionFirewall
from core.models import ToolCall, PolicyDecision

class AgentActionFirewall:
    name = "agent-action-firewall"
    def check(self, call: ToolCall) -> PolicyDecision:
        return ActionFirewall().check(call.tool)
