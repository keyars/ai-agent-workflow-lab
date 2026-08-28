from dataclasses import dataclass

@dataclass(frozen=True)
class MemoryItem:
    key: str
    value: str
    importance: float = 0.5

class MemoryOptimizer:
    def rank(self, items: list[MemoryItem]) -> list[MemoryItem]:
        return sorted(items, key=lambda x: x.importance, reverse=True)
    def compact(self, items: list[MemoryItem], limit: int) -> list[MemoryItem]:
        return self.rank(items)[:max(0, limit)]
