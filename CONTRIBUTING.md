# Contributing Guidelines

This repository demonstrates a modular, agentic content generation system.

## Adding New Products
- Add product data to the `data/` directory
- Reuse existing agents and logic blocks
- No changes to templates are required unless adding new page types

## Adding New Page Types
- Define a new template in `templates/`
- Reuse existing logic blocks or introduce new ones
- Avoid embedding business logic inside templates

## Code Principles
- Agents orchestrate, logic blocks compute
- Logic blocks must be stateless and deterministic
- Outputs must remain machine-readable JSON
