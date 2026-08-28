from dataclasses import dataclass

@dataclass(frozen=True)
class MCPMapping:
    method: str
    path: str
    tool_name: str

class RESTToMCPAdapter:
    name = "rest-to-mcp-adapter"
    def map_endpoint(self, method: str, path: str) -> MCPMapping:
        normalized = path.strip("/").replace("/", ".") or "root"
        return MCPMapping(method.upper(), path, f"{method.lower()}.{normalized}")
