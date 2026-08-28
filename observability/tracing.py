from contextlib import contextmanager
from dataclasses import dataclass, field
from time import perf_counter
from typing import Iterator

@dataclass
class Span:
    name: str
    duration_ms: int = 0
    attributes: dict[str, str] = field(default_factory=dict)

@contextmanager
def trace(name: str, **attributes: str) -> Iterator[Span]:
    start = perf_counter()
    span = Span(name=name, attributes=attributes)
    try:
        yield span
    finally:
        span.duration_ms = int((perf_counter() - start) * 1000)
