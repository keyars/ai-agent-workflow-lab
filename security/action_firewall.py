from core.models import Decision, PolicyDecision
from core.policies import PolicyEngine

class ActionFirewall:
    def __init__(self, policy_engine: PolicyEngine | None = None) -> None:
        self.policy_engine = policy_engine or PolicyEngine()
    def check(self, tool_name: str) -> PolicyDecision:
        return self.policy_engine.evaluate(tool_name)
    def should_execute(self, decision: PolicyDecision) -> bool:
        return decision.decision is Decision.ALLOW
