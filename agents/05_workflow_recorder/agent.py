from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class RecordedAction:
    action: str
    target: str | None = None
    value: str | None = None

class WorkflowRecorder:
    name = "workflow-recorder"
    def record(self, actions: list[RecordedAction]) -> list[dict[str, str | None]]:
        return [asdict(action) for action in actions]
