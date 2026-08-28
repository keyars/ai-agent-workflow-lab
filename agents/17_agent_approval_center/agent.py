from security.approval import ApprovalCenter, ApprovalRequest

class AgentApprovalCenter:
    name = "agent-approval-center"
    def __init__(self) -> None: self.center = ApprovalCenter()
    def request(self, tool: str, reason: str) -> ApprovalRequest: return self.center.request(tool, reason)
    def approve(self, request_id: str) -> ApprovalRequest: return self.center.approve(request_id)
    def deny(self, request_id: str) -> ApprovalRequest: return self.center.deny(request_id)
