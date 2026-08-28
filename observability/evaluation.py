from dataclasses import dataclass

@dataclass(frozen=True)
class EvalCase:
    name: str
    input: dict[str, object]
    expected: dict[str, object]

@dataclass
class EvalResult:
    case: str
    passed: bool
    score: float
    notes: str = ""

def exact_match(actual: dict[str, object], expected: dict[str, object]) -> bool:
    return actual == expected
