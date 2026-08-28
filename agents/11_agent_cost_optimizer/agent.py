class AgentCostOptimizer:
    name = "agent-cost-optimizer"
    def savings(self, current_cost: float, optimized_cost: float) -> dict[str, float]:
        if current_cost < 0 or optimized_cost < 0: raise ValueError("Costs cannot be negative")
        saved = max(0.0, current_cost - optimized_cost)
        percent = (saved / current_cost * 100.0) if current_cost else 0.0
        return {"current": current_cost, "optimized": optimized_cost, "saved": saved, "savings_percent": percent}
