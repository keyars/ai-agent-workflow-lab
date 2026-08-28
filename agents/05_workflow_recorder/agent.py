from dataclasses import dataclass, field
from typing import Any

@dataclass
class WorkflowRecorder:
    steps: list[dict[str, Any]] = field(default_factory=list)
    def record(self, action: str, **data: Any) -> None:
        self.steps.append({"action": action, **data})
    def export(self) -> list[dict[str, Any]]:
        return list(self.steps)
