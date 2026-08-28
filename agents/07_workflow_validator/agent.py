from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ValidationIssue:
    level: str
    message: str

class WorkflowValidator:
    def validate(self, steps: list[dict[str, Any]]) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        if not steps: issues.append(ValidationIssue("error", "Workflow has no steps"))
        for i, step in enumerate(steps):
            if not step.get("action"): issues.append(ValidationIssue("error", f"Step {i + 1} has no action"))
        return issues
