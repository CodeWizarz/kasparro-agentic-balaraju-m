# Contributing Guidelines

This repository demonstrates a **LangGraph-based, agentic content generation system** built for structured automation, not prompt experimentation.

All contributions must preserve the system’s **agentic boundaries, orchestration model, and schema guarantees**.

---

## 🧩 Core Principles

- **Agent-first design**: Each agent must have a single responsibility.
- **LLM-backed reasoning**: Content generation must be LLM-driven, not hardcoded.
- **Explicit orchestration**: All execution must occur inside the LangGraph DAG.
- **Schema enforcement**: Outputs must validate against defined Pydantic schemas.
- **No global state**: All data must flow through the shared graph state.

---

## ➕ Adding New Products

To support new products:

1. Add a new structured input file under `data/`
2. Ensure the data follows the same schema as existing product inputs
3. Run the pipeline without modifying agent logic

The system is designed to generalize across products without code changes.

---

## ➕ Adding New Page Types

To add a new content page:

1. Define a new Pydantic schema under `schemas/`
2. Implement a new agent responsible for generating that page
3. Add the agent as a node in the LangGraph execution graph
4. Register validation in the `ValidationAgent`
5. Persist output via the `OutputAgent`

Avoid embedding logic inside orchestration or output layers.

---

## 🔁 Modifying Agents

When updating or extending agents:

- Keep responsibilities narrowly scoped
- Accept and return data exclusively via `GraphState`
- Do not introduce hidden side effects or shared globals
- Handle LLM failures via retry utilities
- Never bypass schema validation

---

## 🧪 Testing Requirements

All changes must be accompanied by tests:

- Output existence and structure
- Schema compliance
- Content count constraints (e.g., ≥15 FAQs)

Tests must pass before merging.

---

## 🚫 What Not To Do

- Do not add deterministic or hardcoded content generation
- Do not introduce sequential scripts outside LangGraph
- Do not bypass validation or output gates
- Do not mix legacy template-based logic into agents

---

## 📌 Final Note

This repository reflects **production-oriented applied AI engineering practices**.  
Contributions should prioritize **clarity, robustness, and extensibility** over shortcuts or prompt-only solutions.