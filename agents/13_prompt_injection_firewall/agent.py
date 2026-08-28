from security.prompt_injection import PromptInjectionFirewall

class PromptInjectionAgent:
    def __init__(self) -> None: self.firewall = PromptInjectionFirewall()
    def scan(self, content: str) -> dict[str, object]:
        safe, findings = self.firewall.inspect(content)
        return {"safe": safe, "findings": findings}
