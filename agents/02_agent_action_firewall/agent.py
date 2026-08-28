from core.models import ToolCall
from security.action_firewall import ActionFirewall

class AgentActionFirewall:
    def __init__(self, firewall: ActionFirewall | None = None) -> None:
        self.firewall = firewall or ActionFirewall()
    def inspect(self, call: ToolCall):
        return self.firewall.check(call.tool)
    def allowed(self, call: ToolCall) -> bool:
        return self.firewall.should_execute(self.inspect(call))
