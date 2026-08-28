# Architecture

The platform separates model planning from tool execution. Model output is treated as untrusted intent and converted into typed tool calls. Deterministic policy executes before tools. High-risk actions enter approval flow. Structured events feed observability, evaluation, replay, and recovery.

## Target execution path

Planner → Tool Discovery → Security Gateway → Policy → Approval (when required) → Tool Execution → Validation → Recovery → Observability.

## Shared contracts

Agents use `AgentRequest` and `AgentResponse`. Tools use `ToolCall` and `ToolResult`. This keeps modules provider-neutral and makes deterministic testing possible.

## Security posture

Unknown tools are denied by default. Destructive tools are approval-gated. External content is inspected for prompt-injection signals before it is allowed to influence an agent workflow. These are baseline controls; production deployments should add identity, secrets isolation, network policy and stronger policy-as-code.
