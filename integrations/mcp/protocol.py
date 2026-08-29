from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field

class MCPTool(BaseModel):
    name: str
    description: str = ""
    input_schema: dict[str, Any] = Field(default_factory=dict)

class MCPToolResult(BaseModel):
    content: list[dict[str, Any]] = Field(default_factory=list)
    is_error: bool = False

class MCPServerInfo(BaseModel):
    name: str
    version: str = "0.1.0"
    tools: list[MCPTool] = Field(default_factory=list)

class MCPRequest(BaseModel):
    method: str
    params: dict[str, Any] = Field(default_factory=dict)
    id: str | int | None = None

class MCPResponse(BaseModel):
    result: dict[str, Any] | None = None
    error: dict[str, Any] | None = None
    id: str | int | None = None
