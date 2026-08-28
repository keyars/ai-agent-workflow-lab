from copy import deepcopy
from typing import Any

class ReplayDebugger:
    def replay(self, events: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return deepcopy(events)
    def tool_calls(self, events: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [e for e in events if e.get("type") == "tool_call"]
