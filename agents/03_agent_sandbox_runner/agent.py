from pathlib import Path

class AgentSandboxRunner:
    name = "agent-sandbox-runner"
    def __init__(self, root: str = "sandbox") -> None:
        self.root = Path(root).resolve()
    def validate_path(self, path: str) -> Path:
        candidate = (self.root / path).resolve()
        if self.root != candidate and self.root not in candidate.parents:
            raise PermissionError("Path escapes sandbox")
        return candidate
