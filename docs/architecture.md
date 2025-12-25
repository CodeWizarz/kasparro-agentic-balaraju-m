# System Architecture

## Agent Responsibilities
- ParserAgent: Normalizes input data
- QuestionAgent: Generates categorized questions
- LogicAgent: Coordinates reusable logic blocks
- TemplateAgent: Applies declarative templates
- AssemblerAgent: Persists JSON outputs

## Execution Flow

Parser → QuestionAgent → LogicAgent → TemplateAgent → Assembler

## Design Goals
- Determinism over generation
- Reusability over duplication
- Templates over hardcoded pages
