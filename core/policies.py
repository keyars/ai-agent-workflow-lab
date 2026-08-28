from dataclasses import dataclass, field
from core.models import Decision, PolicyDecision, RiskLevel

@dataclass(frozen=True)
class ToolPolicy:
    name: str
    risk: RiskLevel
    requires_approval: bool = False
    allowed_arguments: set[str] = field(default_factory=set)

class PolicyEngine:
    def __init__(self, policies: list[ToolPolicy] | None = None) -> None:
        self._policies = {p.name: p for p in (policies or self._defaults())}
    @staticmethod
    def _defaults() -> list[ToolPolicy]:
        return [
            ToolPolicy("filesystem.read", RiskLevel.LOW),
            ToolPolicy("git.status", RiskLevel.LOW),
            ToolPolicy("github.read", RiskLevel.LOW),
            ToolPolicy("filesystem.write", RiskLevel.MEDIUM, True),
            ToolPolicy("git.push", RiskLevel.HIGH, True),
            ToolPolicy("github.delete_branch", RiskLevel.CRITICAL, True),
            ToolPolicy("database.delete", RiskLevel.CRITICAL, True),
        ]
    def evaluate(self, tool_name: str) -> PolicyDecision:
        policy = self._policies.get(tool_name)
        if policy is None:
            return PolicyDecision(decision=Decision.DENY, risk=RiskLevel.HIGH, reason="Tool is not allowlisted", policy="allowlist")
        if policy.requires_approval:
            return PolicyDecision(decision=Decision.APPROVAL_REQUIRED, risk=policy.risk, reason="Tool requires explicit human approval", policy=policy.name)
        return PolicyDecision(decision=Decision.ALLOW, risk=policy.risk, reason="Tool is allowlisted", policy=policy.name)
