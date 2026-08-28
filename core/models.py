from __future__ import annotations
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import uuid4
from pydantic import BaseModel, Field

class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Decision(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    APPROVAL_REQUIRED = "approval_required"

class ToolCall(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    tool: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    requested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ToolResult(BaseModel):
    call_id: str
    success: bool
    output: Any = None
    error: str | None = None
    duration_ms: int | None = None

class PolicyDecision(BaseModel):
    decision: Decision
    risk: RiskLevel
    reason: str
    policy: str = "default"

class AuditEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: uuid4().hex)
    event_type: str
    actor: str
    data: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class AgentRequest(BaseModel):
    task_id: str = Field(default_factory=lambda: uuid4().hex)
    agent: str
    input: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)

class AgentResponse(BaseModel):
    task_id: str
    success: bool
    output: dict[str, Any] = Field(default_factory=dict)
    errors: list[str] = Field(default_factory=list)
