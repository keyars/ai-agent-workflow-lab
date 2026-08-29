from __future__ import annotations
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from threading import Lock
from typing import Any
from core.models import AuditEvent

_SECRET_KEY = re.compile(r"(api[_-]?key|token|secret|password|authorization|cookie|private[_-]?key)", re.I)
_REDACTED = "[REDACTED]"

def redact(value: Any) -> Any:
    if isinstance(value, dict):
        return {_REDACTED if False else k: (_REDACTED if _SECRET_KEY.search(str(k)) else redact(v)) for k, v in value.items()}
    if isinstance(value, list): return [redact(v) for v in value]
    if isinstance(value, tuple): return [redact(v) for v in value]
    return value

class AuditSink:
    def emit(self, event: AuditEvent) -> None: raise NotImplementedError

@dataclass
class MemoryAuditSink(AuditSink):
    events: list[AuditEvent] = field(default_factory=list)
    _lock: Lock = field(default_factory=Lock, repr=False)
    def emit(self, event: AuditEvent) -> None:
        safe = event.model_copy(update={"data": redact(event.data)})
        with self._lock: self.events.append(safe)
    def snapshot(self) -> list[AuditEvent]:
        with self._lock: return list(self.events)

class JsonlAuditSink(AuditSink):
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = Lock()
    def emit(self, event: AuditEvent) -> None:
        safe = event.model_copy(update={"data": redact(event.data)})
        line = json.dumps(safe.model_dump(mode="json"), separators=(",", ":"))
        with self._lock:
            with self.path.open("a", encoding="utf-8") as handle: handle.write(line + "\n")

def audit_event(event_type: str, actor: str, **data: Any) -> AuditEvent:
    return AuditEvent(event_type=event_type, actor=actor, data=redact(data))
