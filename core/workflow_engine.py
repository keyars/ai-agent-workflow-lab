from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
from core.executor import ToolExecutor
from core.models import ToolCall
from core.state import WorkflowState
from core.workflow import Workflow

@dataclass
class StepExecution:
    index: int
    action: str
    result: Any

class WorkflowEngine:
    """Runs typed workflows and checkpoints after each successful step."""
    def __init__(self, executor: ToolExecutor, action_handlers: dict[str, Callable[..., Any]] | None = None) -> None:
        self.executor = executor
        self.action_handlers = action_handlers or {}

    async def run(self, workflow: Workflow, state: WorkflowState | None = None) -> list[StepExecution]:
        current = state or WorkflowState(workflow_id=workflow.name)
        current.status = "running"
        results: list[StepExecution] = []
        for index in range(current.cursor, len(workflow.steps)):
            step = workflow.steps[index]
            try:
                if step.tool:
                    result = await self.executor.execute(ToolCall(tool=step.tool, arguments=step.arguments))
                    if not result.success:
                        current.fail(result.error or "Tool failed")
                        break
                    value = result.output
                elif step.action in self.action_handlers:
                    value = self.action_handlers[step.action](**step.arguments)
                else:
                    current.fail(f"No handler registered for action: {step.action}")
                    break
                results.append(StepExecution(index, step.action, value))
                current.checkpoint(index + 1, value)
            except Exception as exc:
                current.fail(f"Step {index + 1} failed: {type(exc).__name__}")
                break
        else:
            current.status = "completed"
        return results
