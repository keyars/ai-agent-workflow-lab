from dataclasses import dataclass

@dataclass(frozen=True)
class ToolDescriptor:
    name: str
    description: str
    risk: str

class ToolDiscoveryEngine:
    def discover(self, query: str, tools: list[ToolDescriptor], limit: int = 5) -> list[ToolDescriptor]:
        terms = set(query.lower().split())
        scored = [(len(terms & set(t.description.lower().split())), t) for t in tools]
        return [t for score, t in sorted(scored, key=lambda x: x[0], reverse=True) if score > 0][:limit]
