from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class MCPToolSchema:
    name: str
    description: str
    input_schema: dict[str, Any]

class MCPServerGenerator:
    def generate_manifest(self, tools: list[MCPToolSchema]) -> dict[str, Any]:
        return {"protocol": "mcp", "tools": [t.__dict__ for t in tools]}
