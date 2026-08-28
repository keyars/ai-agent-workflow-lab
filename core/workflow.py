from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

@dataclass(frozen=True)
class WorkflowStep:
    action: str
    tool: str | None = None
    arguments: dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: uuid4().hex)

@dataclass(frozen=True)
class Workflow:
    name: str
    steps: tuple[WorkflowStep, ...]
    version: int = 1

    @classmethod
    def from_steps(cls, name: str, steps: list[WorkflowStep]) -> "Workflow":
        if not name.strip(): raise ValueError("Workflow name cannot be empty")
        if not steps: raise ValueError("Workflow must contain at least one step")
        return cls(name=name.strip(), steps=tuple(steps))

    def to_dict(self) -> dict[str, Any]:
        return {"name": self.name, "version": self.version, "steps": [
            {"id": s.id, "action": s.action, "tool": s.tool, "arguments": s.arguments}
            for s in self.steps
        ]}
