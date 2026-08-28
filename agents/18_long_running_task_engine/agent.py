from dataclasses import dataclass
from enum import StrEnum
from uuid import uuid4

class TaskStatus(StrEnum):
    QUEUED="queued"; RUNNING="running"; PAUSED="paused"; COMPLETED="completed"; FAILED="failed"; CANCELLED="cancelled"
@dataclass
class Task:
    id: str
    status: TaskStatus = TaskStatus.QUEUED
    checkpoint: int = 0
class LongRunningTaskEngine:
    def __init__(self) -> None: self.tasks: dict[str, Task] = {}
    def create(self) -> Task:
        t=Task(uuid4().hex); self.tasks[t.id]=t; return t
    def transition(self, task_id: str, status: TaskStatus, checkpoint: int | None = None) -> Task:
        t=self.tasks[task_id]; t.status=status
        if checkpoint is not None: t.checkpoint=checkpoint
        return t
