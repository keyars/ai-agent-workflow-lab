import pytest
from core.executor import ToolExecutor
from core.models import ToolCall
from core.runtime import ToolRegistry
from core.state import WorkflowState
from core.workflow import Workflow, WorkflowStep
from core.workflow_engine import WorkflowEngine
from tools.builtins import JsonEchoTool

@pytest.mark.asyncio
async def test_guarded_tool_execution_and_checkpointing() -> None:
    registry = ToolRegistry(); registry.register(JsonEchoTool())
    engine = WorkflowEngine(ToolExecutor(registry))
    workflow = Workflow.from_steps("echo", [WorkflowStep(action="echo", tool="utility.echo_json", arguments={"value": 42})])
    state = WorkflowState(workflow_id="echo")
    results = await engine.run(workflow, state)
    assert results[0].result == {"value": 42}
    assert state.status == "completed"
    assert state.cursor == 1

@pytest.mark.asyncio
async def test_unknown_tool_is_blocked_before_execution() -> None:
    registry = ToolRegistry()
    executor = ToolExecutor(registry)
    result = await executor.execute(ToolCall(tool="shell.exec", arguments={"command": "whoami"}))
    assert not result.success
    assert "Blocked" in (result.error or "")

@pytest.mark.asyncio
async def test_approval_required_tool_is_blocked_by_executor() -> None:
    registry = ToolRegistry(); registry.register(JsonEchoTool())
    executor = ToolExecutor(registry)
    result = await executor.execute(ToolCall(tool="git.push", arguments={}))
    assert not result.success
    assert "Blocked" in (result.error or "")
