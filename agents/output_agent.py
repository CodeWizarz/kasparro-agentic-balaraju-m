import json
import os
from graph.state import GraphState

def output_writer_agent(state: GraphState) -> GraphState:
    os.makedirs("output", exist_ok=True)

    with open("output/faq.json", "w") as f:
        json.dump(state["faq"], f, indent=2)

    with open("output/product_page.json", "w") as f:
        json.dump(state["product_page"], f, indent=2)

    with open("output/comparison_page.json", "w") as f:
        json.dump(state["comparison_page"], f, indent=2)

    return state
