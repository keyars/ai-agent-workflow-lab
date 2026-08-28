class ToolDiscoveryEngine:
    name = "tool-discovery-engine"
    def rank(self, query: str, tools: list[str]) -> list[str]:
        terms = set(query.lower().split())
        scored = [(sum(term in tool.lower() for term in terms), tool) for tool in tools]
        return [tool for score, tool in sorted(scored, key=lambda item: (-item[0], item[1])) if score > 0] or sorted(tools)
