import re

SUSPICIOUS_PATTERNS = (
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"system\s+prompt",
    r"reveal\s+(your|the)\s+instructions",
    r"disable\s+(security|safety)",
    r"bypass\s+(the\s+)?policy",
)

def detect_prompt_injection(text: str) -> list[str]:
    return [pattern for pattern in SUSPICIOUS_PATTERNS if re.search(pattern, text, re.IGNORECASE)]

class PromptInjectionFirewall:
    def inspect(self, text: str) -> tuple[bool, list[str]]:
        findings = detect_prompt_injection(text)
        return not findings, findings
