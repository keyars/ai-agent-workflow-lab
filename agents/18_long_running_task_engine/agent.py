from dataclasses import dataclass
from enum import StrEnum
from uuid import uuid4

class TaskStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

@dataclass
class Task:
    id: str
    status: TaskStatus = TaskStatus.PENDING

class LongRunningTaskEngine:
    name = "long-running-task-engine"
    def create(self) -> Task: return Task(uuid4().hex)
    def pause(self, task: Task) -> Task: task.status = TaskStatus.PAUSED; return task
    def cancel(self, task: Task) -> Task: task.status = TaskStatus.CANCELLED; return task
