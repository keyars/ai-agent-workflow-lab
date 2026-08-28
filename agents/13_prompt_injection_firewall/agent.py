from security.prompt_injection import PromptInjectionFirewall

class PromptInjectionFirewallAgent:
    name = "prompt-injection-firewall"
    def inspect(self, text: str) -> dict[str, object]:
        safe, findings = PromptInjectionFirewall().inspect(text)
        return {"safe": safe, "findings": findings}
