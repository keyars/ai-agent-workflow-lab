from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class WorkflowStep:
    id: str
    action: str
    params: dict[str, Any]

class WorkflowGenerator:
    def generate(self, intent: str) -> list[WorkflowStep]:
        words = [w for w in intent.lower().split() if w]
        return [WorkflowStep(str(i + 1), word, {}) for i, word in enumerate(words[:20])]
