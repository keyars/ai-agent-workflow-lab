from dataclasses import dataclass

@dataclass(frozen=True)
class RecoveryPlan:
    action: str
    delay_seconds: int = 0
    reason: str = ""

class AgentFailureRecovery:
    name = "agent-failure-recovery"
    def plan(self, error: str, attempt: int, max_attempts: int = 3) -> RecoveryPlan:
        if attempt >= max_attempts: return RecoveryPlan("stop", reason=f"retry budget exhausted: {error}")
        return RecoveryPlan("retry", delay_seconds=min(2 ** attempt, 30), reason=error)
