# AI Agent Workflow Lab

> Production-oriented infrastructure for building, securing, evaluating, and operating tool-using AI agents.

This is a **platform**, not a collection of chatbot demos. It provides a shared runtime and a guarded execution path so the 20 workflow agents can compose instead of becoming 20 incompatible mini-applications.

## What works now

- typed `Workflow` and `WorkflowStep` contracts
- checkpointable `WorkflowState`
- provider-neutral `ModelRouter`
- central `ToolRegistry`
- guarded asynchronous `ToolExecutor`
- deny-by-default policy enforcement
- approval gating for risky tools
- prompt-injection inspection boundary
- safe built-in JSON echo and file-read tools
- automated workflow execution tests
- GitHub Actions CI

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

## Guarded execution path

```text
Intent / Agent
      |
      v
Workflow
      |
      v
ToolCall
      |
      v
Prompt-Injection Boundary
      |
      v
Policy / Allowlist
   |       |
 deny    approval
   |       |
   +---+---+
       |
       v
ToolExecutor
       |
       v
ToolRegistry
       |
       v
Result + Duration
       |
       v
Checkpoint / Observability / Evaluation
```

Every tool call must pass through the executor. Unknown tools and approval-gated operations are blocked before execution.

## Architecture

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
        |      +----+----+                  |        Durable
        |      |         |                  |         Tasks
        |   Firewall  Approval              |           |
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
core/             runtime, workflows, state, routing and policy
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

The next layers will add real MCP transports, browser adapters, durable persistence, model-provider integrations, richer evaluation metrics, structured audit events, and production deployment examples while preserving the guarded execution contract.
