from __future__ import annotations
import json
from pathlib import Path
from core.models import ToolCall, ToolResult

class JsonEchoTool:
    name = "utility.echo_json"
    async def execute(self, call: ToolCall) -> ToolResult:
        return ToolResult(call_id=call.id, success=True, output=json.loads(json.dumps(call.arguments)))

class FileReadTool:
    name = "filesystem.read"
    async def execute(self, call: ToolCall) -> ToolResult:
        path = Path(str(call.arguments.get("path", ""))).expanduser()
        if not path.is_file(): return ToolResult(call_id=call.id, success=False, error="File does not exist")
        text = path.read_text(encoding="utf-8")
        return ToolResult(call_id=call.id, success=True, output=text[:65536])
