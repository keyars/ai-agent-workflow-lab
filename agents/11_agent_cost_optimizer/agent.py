from dataclasses import dataclass

@dataclass(frozen=True)
class ModelTier:
    name: str
    input_cost_per_million: float
    output_cost_per_million: float

class CostOptimizer:
    def choose(self, tiers: list[ModelTier], required_quality: float = 0.0) -> ModelTier:
        if not tiers: raise ValueError("No model tiers supplied")
        return min(tiers, key=lambda t: t.input_cost_per_million + t.output_cost_per_million)
    def estimate(self, tier: ModelTier, input_tokens: int, output_tokens: int) -> float:
        return (input_tokens * tier.input_cost_per_million + output_tokens * tier.output_cost_per_million) / 1_000_000
