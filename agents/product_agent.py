from langchain_openai import ChatOpenAI
from schemas.product import ProductPage
from graph.state import GraphState
import json
import re


def extract_json(text: str) -> dict:
    """
    Extract JSON object from LLM output, stripping markdown if present.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM response")
    return json.loads(match.group())


def ensure_list_fields(data: dict) -> dict:
    """
    Normalize fields that MUST be lists according to schema.
    This protects against LLMs returning strings instead of arrays.
    """

    # usage.steps
    if isinstance(data.get("usage", {}).get("steps"), str):
        data["usage"]["steps"] = [data["usage"]["steps"]]

    # usage.time_of_use
    if isinstance(data.get("usage", {}).get("time_of_use"), str):
        data["usage"]["time_of_use"] = [data["usage"]["time_of_use"]]

    # safety.warnings
    if isinstance(data.get("safety", {}).get("warnings"), str):
        data["safety"]["warnings"] = [data["safety"]["warnings"]]

    # safety.side_effects
    if isinstance(data.get("safety", {}).get("side_effects"), str):
        data["safety"]["side_effects"] = [data["safety"]["side_effects"]]

    return data


def product_page_agent(state: GraphState) -> GraphState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt = f"""
You are an AI agent generating a PRODUCT PAGE.

STRICT RULES (MANDATORY):
- Output ONLY valid JSON
- No markdown
- No commentary
- Every field that is a list MUST be a JSON array, even if it has only one item
- Do NOT output strings where arrays are expected
- Use ONLY the product data provided

JSON SCHEMA (FOLLOW EXACTLY):
{{
  "overview": {{
    "product_name": string,
    "concentration": string,
    "target_skin_type": [string],
    "key_ingredients": [string]
  }},
  "benefits": [
    {{
      "benefit": string,
      "reason": string
    }}
  ],
  "usage": {{
    "time_of_use": [string],
    "steps": [string]
  }},
  "safety": {{
    "side_effects": [string],
    "warnings": [string]
  }},
  "pricing": {{
    "price": string,
    "category": string
  }}
}}

Product Data:
{state['product']}
"""

    response = llm.invoke(prompt)

    # Extract and clean JSON
    parsed = extract_json(response.content)

    # Normalize list fields defensively
    parsed = ensure_list_fields(parsed)

    # Ensure at least one safety warning
    if not parsed["safety"].get("warnings"):
        parsed["safety"]["warnings"] = ["Patch test recommended before full use"]
    # Normalize pricing category
    parsed["pricing"]["category"] = "mid-range"


    # Schema validation (hard gate)
    product_page = ProductPage(**parsed)

    # Guarantee state mutation
    state["product_page"] = product_page.model_dump()
    return state
