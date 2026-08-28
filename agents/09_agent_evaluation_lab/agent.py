from observability.evaluation import EvalCase, EvalResult, exact_match

class AgentEvaluationLab:
    name = "agent-evaluation-lab"
    def evaluate(self, case: EvalCase, actual: dict[str, object]) -> EvalResult:
        passed = exact_match(actual, case.expected)
        return EvalResult(case.name, passed, 1.0 if passed else 0.0)
