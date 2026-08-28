from dataclasses import dataclass
from uuid import uuid4

@dataclass
class ApprovalRequest:
    id: str
    tool: str
    reason: str
    status: str = "pending"

class ApprovalCenter:
    def __init__(self) -> None:
        self._requests: dict[str, ApprovalRequest] = {}
    def request(self, tool: str, reason: str) -> ApprovalRequest:
        item = ApprovalRequest(uuid4().hex, tool, reason)
        self._requests[item.id] = item
        return item
    def approve(self, request_id: str) -> ApprovalRequest:
        item = self._requests[request_id]
        item.status = "approved"
        return item
    def deny(self, request_id: str) -> ApprovalRequest:
        item = self._requests[request_id]
        item.status = "denied"
        return item
