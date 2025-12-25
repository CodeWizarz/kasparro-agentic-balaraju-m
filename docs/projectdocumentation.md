# Project Documentation – Multi-Agent Content Generation System

---

## 1. Problem Statement

Modern content systems require generating structured, consistent, and machine-readable content from raw product data at scale. Traditional approaches rely on tightly coupled scripts or prompt-based generation, which makes systems difficult to maintain, extend, or reason about.

The goal of this project is to design and implement a **modular, agentic content generation system** that transforms structured product data into multiple content pages using **clear agent boundaries**, **reusable logic blocks**, and **template-driven assembly**, without relying on monolithic scripts or ad-hoc prompting.

---

## 2. Solution Overview

This system implements an **agent-orchestrated pipeline** that converts raw product data into structured JSON pages.

### High-level Flow

Raw Product Data
↓
ProductDataParserAgent
↓
QuestionGenerationAgent
↓
ContentLogicAgent
↓
TemplateAgent
↓
PageAssemblerAgent
↓
JSON Outputs

The system cleanly separates:
- data parsing
- content logic
- template structure
- output assembly

This ensures correctness, extensibility, and maintainability.

---

## 3. Scope & Assumptions

### Scope
- Input data is limited to the provided product dataset.
- All outputs are machine-readable JSON.
- Three pages are generated:
  - FAQ Page
  - Product Page
  - Comparison Page

### Assumptions
- No external data or research is used.
- Comparison product (Product B) is fictional but structured.
- Outputs are deterministic and rule-based.
- The system is designed for extensibility, not UI rendering.

---

## 4. System Design (Core Architecture)

### 4.1 Agent Responsibilities

#### ProductDataParserAgent
- Converts raw product input into a normalized internal data model.
- Ensures consistent structure across downstream agents.

#### QuestionGenerationAgent
- Automatically generates categorized user questions (informational, usage, safety, purchase, comparison).
- Outputs structured question sets without page awareness.

#### ContentLogicAgent
- Coordinates reusable, stateless content logic blocks.
- Executes domain-agnostic transformations such as:
  - overview generation
  - benefits mapping
  - usage structuring
  - safety extraction
  - pricing categorization
  - FAQ assembly
  - product comparison
- Returns a unified dictionary of structured content blocks.

#### TemplateAgent
- Applies declarative template definitions.
- Validates required blocks.
- Assembles page drafts based on template layouts.
- Remains independent of business logic and data parsing.

#### PageAssemblerAgent
- Converts structured page drafts into final JSON files.
- Handles output persistence.

---

### 4.2 Logic Blocks

Logic blocks are **pure, reusable functions** that:
- accept structured input
- apply deterministic rules
- return structured output
- have no knowledge of page layout or orchestration

Examples:
- `generate_overview_block`
- `generate_benefits_block`
- `generate_usage_block`
- `generate_pricing_block`
- `assemble_faq_block`
- `compare_products_block`

This separation allows the same logic to be reused across multiple templates or future products.

---

### 4.3 Template Engine

Templates are defined as declarative JSON schemas that specify:
- required logic blocks
- section layout
- page type

Templates do not contain business logic or prose.  
They simply describe **how content blocks are assembled into pages**.

This makes adding new pages possible without modifying existing agents or logic blocks.

---

### 4.4 Orchestration

The orchestration is handled by `main.py`, which acts as the system entrypoint:
- initializes agents
- executes the pipeline in order
- passes structured outputs between agents

This design keeps orchestration explicit and traceable.

---

## 5. Data & Output Structure

All outputs are generated as clean, deterministic JSON:

- `faq.json`
- `product_page.json`
- `comparison_page.json`

Each file contains:
- `page_type`
- structured `sections`
- no free-text blobs
- clear mapping from data → logic → output

---

## 6. Extensibility

The system is designed for easy extension:
- New products → reuse existing agents
- New logic rules → add logic blocks
- New page types → add templates
- New orchestration flows → modify orchestrator without changing logic

This mirrors production-grade content automation systems.

---

## 7. Conclusion

This project demonstrates a production-style approach to building agentic content systems by emphasizing:
- modular design
- separation of concerns
- deterministic logic
- structured outputs
- clear orchestration

The result is a maintainable, extensible system suitable for real-world AI content pipelines.
