from dataclasses import dataclass

@dataclass(frozen=True)
class SecurityFinding:
    rule: str
    severity: str
    message: str

class AgentSecurityScanner:
    def scan(self, config: dict[str, object]) -> list[SecurityFinding]:
        findings=[]
        if config.get("allow_unknown_tools", False): findings.append(SecurityFinding("unknown-tools", "high", "Unknown tools must not execute by default"))
        if config.get("auto_approve_high_risk", False): findings.append(SecurityFinding("auto-approval", "critical", "High-risk actions require human approval"))
        if not config.get("audit_enabled", False): findings.append(SecurityFinding("audit", "medium", "Execution audit logging is disabled"))
        return findings
