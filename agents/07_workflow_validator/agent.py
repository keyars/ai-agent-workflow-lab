from core.models import ToolCall
from security.action_firewall import ActionFirewall

class WorkflowValidator:
    name = "workflow-validator"
    def validate(self, calls: list[ToolCall]) -> list[dict[str, str]]:
        firewall = ActionFirewall()
        return [{"tool": c.tool, "decision": firewall.check(c.tool).decision.value} for c in calls]
