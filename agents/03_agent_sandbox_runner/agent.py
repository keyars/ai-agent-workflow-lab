from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class SandboxPolicy:
    allowed_commands: frozenset[str] = frozenset()
    max_output_bytes: int = 65536

class SandboxRunner:
    """Policy-first command runner abstraction; production adapters can plug in a container runtime."""
    def __init__(self, policy: SandboxPolicy | None = None) -> None:
        self.policy = policy or SandboxPolicy()
    def validate_command(self, command: str) -> bool:
        executable = command.strip().split(maxsplit=1)[0] if command.strip() else ""
        return executable in self.policy.allowed_commands
