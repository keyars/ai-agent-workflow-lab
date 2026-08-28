from core.models import ToolCall

class WorkflowGenerator:
    name = "workflow-generator"
    def from_tools(self, tools: list[str]) -> list[ToolCall]:
        return [ToolCall(tool=tool) for tool in tools]
