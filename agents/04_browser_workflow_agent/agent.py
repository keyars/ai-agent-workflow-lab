from dataclasses import dataclass

@dataclass(frozen=True)
class BrowserStep:
    action: str
    target: str | None = None
    value: str | None = None

class BrowserWorkflowAgent:
    name = "browser-workflow-agent"
    def plan(self, goal: str) -> list[BrowserStep]:
        return [BrowserStep("goal", value=goal)]
