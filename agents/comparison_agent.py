from langchain_openai import ChatOpenAI
from schemas.comparison import ComparisonPage
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


def comparison_agent(state: GraphState) -> GraphState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt = f"""
    You are an AI agent generating a STRUCTURED COMPARISON PAGE.

    STRICT RULES:
    - Output ONLY valid JSON
    - No markdown
    - No commentary
    - No explanations
    - Use ONLY the provided product data
    - Do NOT declare a winner

    JSON SCHEMA:
    {{
      "product_a": {{
        "name": string,
        "ingredients": [string],
        "benefits": [string],
        "price": number
      }},
      "product_b": {{
        "name": string,
        "ingredients": [string],
        "benefits": [string],
        "price": number
      }},
      "comparison_summary": {{
        "price_difference": number,
        "ingredient_difference": [string]
      }}
    }}

    Product A:
    {state['product']}

    Product B:
    {state['product_b']}
    """

    response = llm.invoke(prompt)

    parsed = extract_json(response.content)

    # Schema enforcement
    comparison_page = ComparisonPage(**parsed)

    # GUARANTEE state population
    state["comparison_page"] = comparison_page.model_dump()
    return state
