from __future__ import annotations
from integrations.mcp.protocol import MCPTool
from integrations.mcp.registry import MCPRegistry

class ToolDiscoveryEngine:
    """Select relevant capabilities without exposing the entire tool catalog."""
    def __init__(self, registry: MCPRegistry) -> None: self.registry = registry
    def discover(self, query: str, limit: int = 10) -> list[MCPTool]:
        if limit < 1: raise ValueError("limit must be positive")
        tools = self.registry.discover(query)
        return sorted(tools, key=lambda t: (query.lower() not in t.name.lower(), t.name))[:limit]
