# AI Agent Workflow Lab

> Production-oriented infrastructure for building, securing, evaluating, and operating tool-using AI agents.

This is a **platform**, not a collection of chatbot demos. It is designed around a shared agent runtime, deterministic security controls, MCP/tool execution, durable workflows, evaluation, observability, replay, and recovery.

## 20 production-oriented agents

1. MCP Security Gateway
2. Agent Action Firewall
3. Agent Sandbox Runner
4. Browser Workflow Agent
5. Workflow Recorder
6. Workflow Generator
7. Workflow Validator
8. Agent Observability
9. Agent Evaluation Lab
10. Agent Replay Debugger
11. Agent Cost Optimizer
12. Agent Memory Optimizer
13. Prompt Injection Firewall
14. Tool Discovery Engine
15. MCP Server Generator
16. REST-to-MCP Adapter
17. Agent Approval Center
18. Long-Running Task Engine
19. Agent Failure Recovery
20. Agent Security Scanner

## Platform architecture

```text
                         User / API / CLI
                                |
                         Agent Runtime
                                |
        +-----------------------+-----------------------+
        |                       |                       |
   Model Router            Tool Registry            Memory
        |                       |                       |
        +-----------------------+-----------------------+
                                |
                        Workflow Engine
                                |
        +-----------+-----------+-----------+-----------+
        |           |                       |           |
    Discovery    Security              Execution    State
        |           |                       |           |
        |      +----+----+                  |           |
        |      |         |                  |           |
        |   Firewall  Approval              |        Durable
        |      |         |                  |         Tasks
        +------+---------+------------------+-----------+
                                |
                    Observability / Evaluation
                                |
                     Trace / Cost / Replay
```

## Engineering principles

- deterministic controls before model autonomy
- deny-by-default tool access
- least privilege
- typed structured contracts
- explicit approval for high-risk actions
- timeout, cancellation, retry and recovery
- auditable execution
- reproducible evaluations
- model/provider agnostic interfaces
- secure-by-default examples

## Repository layout

```text
apps/             CLI and application entrypoints
core/             runtime contracts, registries and policy
security/         firewall, injection defense, approval controls
observability/    tracing and evaluation
agents/           20 workflow/agent modules
tools/            safe tool adapters
integrations/     external integrations
tests/            automated verification
docs/             architecture and agent documentation
```

## Development

Python 3.12+ is the initial implementation target.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
agent-lab agents
```

The current branch contains the shared foundation. Agent implementations will be built on these stable contracts rather than becoming 20 incompatible mini-applications.
