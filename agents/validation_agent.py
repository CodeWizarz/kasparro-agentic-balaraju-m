

from schemas.product import ProductPage
from schemas.comparison import ComparisonPage

def validation_agent(state):
    try:
        # Enforce minimum counts
        if len(state["questions"]) < 15:
            raise ValueError("Less than 15 questions generated")

        if len(state["faq"]) < 15:
           raise ValueError(f"Expected at least 15 FAQs, got {len(state['faq'])}")


        # Schema validation
        ProductPage(**state["product_page"])
        ComparisonPage(**state["comparison_page"])

    except Exception as e:
        state["errors"].append(str(e))
        raise

    return state
