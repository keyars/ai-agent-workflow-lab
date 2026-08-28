from observability.tracing import Span, trace

class AgentObservability:
    def run_span(self, agent: str, **attributes: str) -> Span:
        with trace(agent, **attributes) as span:
            pass
        return span
