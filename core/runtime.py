from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Protocol
from core.models import AgentRequest, AgentResponse, ToolCall, ToolResult

class Tool(Protocol):
    name: str
    async def execute(self, call: ToolCall) -> ToolResult: ...

class Agent(ABC):
    name: str
    @abstractmethod
    async def run(self, request: AgentRequest) -> AgentResponse:
        raise NotImplementedError

class ModelProvider(Protocol):
    name: str
    async def complete(self, *, system: str, user: str, **kwargs: Any) -> str: ...

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}
    def register(self, tool: Tool) -> None:
        if tool.name in self._tools: raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool
    def get(self, name: str) -> Tool:
        try: return self._tools[name]
        except KeyError as exc: raise KeyError(f"Unknown tool: {name}") from exc
    def list_names(self) -> list[str]: return sorted(self._tools)

class AgentRegistry:
    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}
    def register(self, agent: Agent) -> None:
        if agent.name in self._agents: raise ValueError(f"Agent already registered: {agent.name}")
        self._agents[agent.name] = agent
    def get(self, name: str) -> Agent:
        try: return self._agents[name]
        except KeyError as exc: raise KeyError(f"Unknown agent: {name}") from exc
    def list_names(self) -> list[str]: return sorted(self._agents)
