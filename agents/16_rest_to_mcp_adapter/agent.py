from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class RESTEndpoint:
    method: str
    path: str
    operation_id: str
    description: str = ""

class RESTToMCPAdapter:
    def convert(self, endpoint: RESTEndpoint) -> dict[str, Any]:
        return {"name": endpoint.operation_id, "description": endpoint.description, "http": {"method": endpoint.method.upper(), "path": endpoint.path}}
