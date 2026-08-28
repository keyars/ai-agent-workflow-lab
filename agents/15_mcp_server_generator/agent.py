class MCPServerGenerator:
    name = "mcp-server-generator"
    def generate_tool_names(self, schema: dict[str, object]) -> list[str]:
        paths = schema.get("paths", {})
        if not isinstance(paths, dict): return []
        return sorted(str(path).strip("/").replace("/", ".") or "root" for path in paths)
