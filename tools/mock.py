from core.models import ToolCall, ToolResult

class MockTool:
    def __init__(self, name: str, output: object = None) -> None:
        self.name = name
        self.output = output

    async def execute(self, call: ToolCall) -> ToolResult:
        return ToolResult(call_id=call.id, success=True, output=self.output)
