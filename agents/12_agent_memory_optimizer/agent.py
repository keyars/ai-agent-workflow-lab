class AgentMemoryOptimizer:
    name = "agent-memory-optimizer"
    def classify(self, text: str) -> str:
        lowered = text.lower()
        if any(word in lowered for word in ("always", "prefer", "my name", "remember")):
            return "long_term"
        return "session"
