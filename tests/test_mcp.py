from integrations.mcp.protocol import MCPServerInfo, MCPTool
from integrations.mcp.registry import MCPRegistry

def test_mcp_registry_discovers_matching_tools() -> None:
    registry = MCPRegistry()
    registry.register_server(MCPServerInfo(name="demo", tools=[
        MCPTool(name="github.search", description="Search repositories"),
        MCPTool(name="github.issue", description="Create an issue"),
    ]))
    matches = registry.discover("search")
    assert [tool.name for tool in matches] == ["github.search"]

def test_mcp_registry_rejects_duplicate_server() -> None:
    registry = MCPRegistry()
    server = MCPServerInfo(name="demo")
    registry.register_server(server)
    try:
        registry.register_server(server)
        raise AssertionError("duplicate server should fail")
    except ValueError as exc:
        assert "already registered" in str(exc)
