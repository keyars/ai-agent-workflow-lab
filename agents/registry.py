from agents.base import WorkflowAgent
from agents.catalog import AGENTS

def build_agent_catalog() -> dict[str, WorkflowAgent]:
    return {slug: WorkflowAgent(slug, description) for _, slug, description in AGENTS}
