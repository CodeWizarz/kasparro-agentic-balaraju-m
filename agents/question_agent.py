from langchain_openai import ChatOpenAI
from graph.state import GraphState

def question_generation_agent(state: GraphState) -> GraphState:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    prompt = f"""
    Generate at least 15 diverse user questions about this product.
    Categories: informational, usage, safety, pricing, comparison.

    Product:
    {state['product']}

    Return as a numbered list.
    """

    response = llm.invoke(prompt)
    questions = [q.strip() for q in response.content.split("\n") if q.strip()]

    if len(questions) < 15:
        raise ValueError("LLM did not generate enough questions")

    state["questions"] = questions
    return state
