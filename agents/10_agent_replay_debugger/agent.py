class AgentReplayDebugger:
    name = "agent-replay-debugger"
    def replay(self, events: list[dict[str, object]]) -> list[dict[str, object]]:
        return [dict(event) for event in events]
