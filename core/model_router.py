from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from core.runtime import ModelProvider

@dataclass(frozen=True)
class ModelRoute:
    provider: str
    model: str
    reason: str

class ModelRouter:
    """Provider-neutral routing layer; model credentials remain outside the repository."""
    def __init__(self) -> None:
        self._providers: dict[str, ModelProvider] = {}
        self._routes: dict[str, ModelRoute] = {}

    def register(self, provider: ModelProvider) -> None:
        self._providers[provider.name] = provider

    def route(self, task_type: str, provider: str, model: str, reason: str = "explicit") -> ModelRoute:
        if provider not in self._providers: raise ValueError(f"Provider is not registered: {provider}")
        route = ModelRoute(provider, model, reason)
        self._routes[task_type] = route
        return route

    async def complete(self, task_type: str, *, system: str, user: str, **kwargs: Any) -> str:
        route = self._routes[task_type]
        return await self._providers[route.provider].complete(system=system, user=user, model=route.model, **kwargs)
