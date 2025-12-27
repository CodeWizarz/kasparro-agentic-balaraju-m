from langchain_openai import ChatOpenAI
from graph.state import GraphState
import re

def clean_question(q: str) -> str:
    # Remove leading numbering like "1. ", "2) ", etc.
    return re.sub(r"^\s*\d+[\.\)]\s*", "", q).strip()

def faq_answer_agent(state: GraphState) -> GraphState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    faqs = []

    for raw_q in state["questions"]:
        question = clean_question(raw_q)

        prompt = f"""
You are answering a product FAQ.

Rules:
- Use ONLY the product data provided
- Be concise and factual
- Do NOT invent information

Product:
{state['product']}

Question:
{question}
"""

        answer = llm.invoke(prompt).content.strip()

        faqs.append({
            "question": question,
            "answer": answer
        })

    state["faq"] = faqs
    return state
