from __future__ import annotations
from integrations.mcp.protocol import MCPServerInfo, MCPTool

class MCPRegistry:
    """Local capability registry used by discovery and gateway layers."""
    def __init__(self) -> None:
        self._servers: dict[str, MCPServerInfo] = {}
    def register_server(self, server: MCPServerInfo) -> None:
        if server.name in self._servers: raise ValueError(f"MCP server already registered: {server.name}")
        names = [tool.name for tool in server.tools]
        if len(names) != len(set(names)): raise ValueError("MCP tool names must be unique per server")
        self._servers[server.name] = server
    def servers(self) -> list[MCPServerInfo]: return list(self._servers.values())
    def find_tool(self, name: str) -> list[tuple[MCPServerInfo, MCPTool]]:
        return [(server, tool) for server in self._servers.values() for tool in server.tools if tool.name == name]
    def discover(self, query: str = "") -> list[MCPTool]:
        needle = query.strip().lower()
        tools = [tool for server in self._servers.values() for tool in server.tools]
        if not needle: return tools
        return [tool for tool in tools if needle in f"{tool.name} {tool.description}".lower()]
