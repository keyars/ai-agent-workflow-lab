from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class WorkflowState:
    workflow_id: str
    status: str = "pending"
    cursor: int = 0
    outputs: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def checkpoint(self, cursor: int, output: Any = None) -> None:
        self.cursor = cursor
        if output is not None: self.outputs[str(cursor)] = output
        self.updated_at = datetime.now(timezone.utc)

    def fail(self, message: str) -> None:
        self.status = "failed"
        self.errors.append(message)
        self.updated_at = datetime.now(timezone.utc)
