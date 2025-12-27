![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/Framework-LangGraph-green)
![Architecture](https://img.shields.io/badge/Architecture-Agentic%20System-orange)
![Output](https://img.shields.io/badge/Output-Structured%20JSON-blueviolet)

# Kasparro – Multi-Agent Content Generation System

This repository contains a **production-style, agentic content generation system** built as part of the **Kasparro Applied AI Engineer assignment**.

The system demonstrates how a small, structured product dataset can be transformed into multiple **machine-readable content pages** using **LLM-backed agents**, **explicit orchestration**, **schema validation**, and **robust automation design**.

---

## 🚀 What This Project Does

Given a structured product dataset, the system autonomously generates:

- **FAQ Page** (`faq.json`) — 15+ user questions and answers
- **Product Page** (`product_page.json`) — structured product description
- **Comparison Page** (`comparison_page.json`) — GlowBoost vs a fictional product

All outputs are:
- **LLM-generated** (no hardcoded content)
- **Schema-validated** (machine-readable JSON)
- **Orchestrated via LangGraph**
- **Produced by specialized agents**, not a monolithic script

---

## 🧠 System Architecture

The system is implemented as a **LangGraph-based multi-agent pipeline**, where each agent performs a single responsibility and communicates through a shared graph state.

```mermaid
graph TD
    Input[Product Dataset] --> QGen[Question Generation Agent]
    QGen --> FAQ[FAQ Agent]
    FAQ --> Product[Product Page Agent]
    Product --> Compare[Comparison Agent]
    Compare --> Validate[Validation Agent]
    Validate --> Output[Output Writer Agent]
````

Key architectural characteristics:

* Explicit DAG execution
* Clear agent boundaries
* No global state
* Retry handling for LLM failures
* Validation gates before persistence

---

## 📁 Repository Structure

```text
.
├── agents/
│   ├── question_agent.py
│   ├── faq_agent.py
│   ├── product_agent.py
│   ├── comparison_agent.py
│   ├── validation_agent.py
│   ├── output_agent.py
│   ├── retry_utils.py
│   └── __init__.py
│
├── graph/
│   ├── graph.py
│   ├── state.py
│   └── __init__.py
│
├── schemas/
│   ├── faq.py
│   ├── product.py
│   ├── comparison.py
│   └── __init__.py
│
├── data/
│   ├── product_input.json
│   └── fictional_product_b.json
│
├── output/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── tests/
│   ├── test_faq_count.py
│   └── test_pipeline_outputs.py
│
├── docs/
│   └── projectdocumentation.md
│
├── main.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## ▶️ How to Run

### Prerequisites

* Python 3.10+
* OpenAI API key

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file using the provided template:

```env
OPENAI_API_KEY=your_api_key_here
```

### Run the Pipeline

```bash
python main.py
```

### Run Tests

```bash
pytest
```

---

## 🧩 Design Principles

* **Agentic orchestration**: Each task is handled by a dedicated agent.
* **LLM-based reasoning**: No deterministic or hardcoded content generation.
* **Schema-driven templates**: Pydantic schemas act as structural templates.
* **Explicit validation**: Outputs are validated before persistence.
* **Robust execution**: Retry logic and failure isolation.
* **Production-oriented design**: Extensible, testable, and auditable.

---

## 📄 Documentation

Detailed system design, architecture rationale, and engineering decisions are documented in:

```
docs/projectdocumentation.md
```

---

## ⚠️ Constraints & Notes

* No external data or research is used.
* Comparison products are fictional and defined in input data.
* The project focuses on **automation and system design**, not UI rendering.

---

## ✅ Conclusion

This project demonstrates a **real-world applied AI engineering approach** to building agentic automation systems. By combining **LangGraph orchestration**, **LLM-backed agents**, and **schema-enforced outputs**, the system avoids brittle prompt-only solutions and delivers a robust, extensible content generation pipeline.

