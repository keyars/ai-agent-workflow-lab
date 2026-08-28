from dataclasses import dataclass

@dataclass(frozen=True)
class BrowserStep:
    action: str
    target: str | None = None
    value: str | None = None

class BrowserWorkflowAgent:
    """Produces explicit browser steps; execution belongs to a separately secured adapter."""
    def plan(self, intent: str) -> list[BrowserStep]:
        text = intent.lower()
        steps: list[BrowserStep] = []
        if "login" in text: steps.append(BrowserStep("navigate", "/login"))
        if "search" in text: steps.append(BrowserStep("search"))
        if not steps: steps.append(BrowserStep("inspect", intent))
        return steps
