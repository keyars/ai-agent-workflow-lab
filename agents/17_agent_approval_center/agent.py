from security.approval import ApprovalCenter, ApprovalRequest

class AgentApprovalCenter:
    def __init__(self, center: ApprovalCenter | None = None) -> None: self.center = center or ApprovalCenter()
    def submit(self, tool: str, reason: str) -> ApprovalRequest: return self.center.request(tool, reason)
    def approve(self, request_id: str) -> ApprovalRequest: return self.center.approve(request_id)
    def deny(self, request_id: str) -> ApprovalRequest: return self.center.deny(request_id)
