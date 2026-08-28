class AgentSecurityScanner:
    name = "agent-security-scanner"
    def scan(self, tools: list[str], approval_required: set[str]) -> list[str]:
        findings = []
        for tool in tools:
            if tool in {"shell.exec", "database.delete"} and tool not in approval_required:
                findings.append(f"High-risk tool without approval: {tool}")
        return findings
