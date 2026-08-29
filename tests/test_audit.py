from pathlib import Path
from core.models import AuditEvent
from observability.audit import JsonlAuditSink, MemoryAuditSink, audit_event, redact

def test_redaction_hides_secrets() -> None:
    value = redact({"api_key": "secret", "nested": {"token": "abc", "ok": 7}})
    assert value == {"api_key": "[REDACTED]", "nested": {"token": "[REDACTED]", "ok": 7}}

def test_memory_sink_stores_redacted_events() -> None:
    sink = MemoryAuditSink()
    sink.emit(audit_event("test", "unit", password="secret", value="ok"))
    event = sink.snapshot()[0]
    assert event.data["password"] == "[REDACTED]"
    assert event.data["value"] == "ok"

def test_jsonl_sink_persists_json(tmp_path: Path) -> None:
    path = tmp_path / "audit.jsonl"
    sink = JsonlAuditSink(path)
    sink.emit(AuditEvent(event_type="test", actor="unit", data={"authorization": "Bearer abc"}))
    line = path.read_text(encoding="utf-8").strip()
    assert '"authorization":"[REDACTED]"' in line
