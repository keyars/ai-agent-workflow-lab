from observability.tracing import Span

class AgentObservability:
    name = "agent-observability"
    def summarize(self, spans: list[Span]) -> dict[str, int]:
        return {"spans": len(spans), "duration_ms": sum(s.duration_ms for s in spans)}
