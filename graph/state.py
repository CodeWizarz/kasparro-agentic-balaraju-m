from typing import TypedDict, List, Dict, Any

class GraphState(TypedDict):
    product: Dict[str, Any]
    product_b: Dict[str, Any]

    questions: List[str]
    faq: List[Dict[str, str]]
    product_page: Dict[str, Any]
    comparison_page: Dict[str, Any]

    errors: List[str]
    retry_count: int
