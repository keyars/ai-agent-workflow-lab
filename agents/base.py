from core.models import AgentRequest, AgentResponse
from core.runtime import Agent

class WorkflowAgent(Agent):
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    async def run(self, request: AgentRequest) -> AgentResponse:
        return AgentResponse(task_id=request.task_id, success=True, output={"agent": self.name, "description": self.description, "input": request.input})
