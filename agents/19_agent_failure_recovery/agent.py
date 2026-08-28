from dataclasses import dataclass
from typing import Callable, TypeVar
T = TypeVar("T")

@dataclass(frozen=True)
class RecoveryPolicy:
    max_attempts: int = 3

class FailureRecovery:
    def run(self, operation: Callable[[], T], policy: RecoveryPolicy | None = None) -> T:
        p=policy or RecoveryPolicy(); last: Exception | None=None
        for _ in range(max(1,p.max_attempts)):
            try: return operation()
            except Exception as exc: last=exc
        assert last is not None
        raise last
