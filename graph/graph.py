from langgraph.graph import StateGraph
from graph.state import GraphState
from agents.question_agent import question_generation_agent
from agents.faq_agent import faq_answer_agent
from agents.product_agent import product_page_agent
from agents.comparison_agent import comparison_agent
from agents.validation_agent import validation_agent
from agents.output_agent import output_writer_agent
from agents.retry_utils import with_retry

graph = StateGraph(GraphState)

# Nodes
graph.add_node("questions", with_retry(question_generation_agent))
graph.add_node("faq", with_retry(faq_answer_agent))
graph.add_node("product_page", with_retry(product_page_agent))
graph.add_node("comparison", with_retry(comparison_agent))
graph.add_node("validate", validation_agent)
graph.add_node("output", output_writer_agent)

# SINGLE LINEAR FLOW (IMPORTANT)
graph.set_entry_point("questions")
graph.add_edge("questions", "faq")
graph.add_edge("faq", "product_page")
graph.add_edge("product_page", "comparison")
graph.add_edge("comparison", "validate")
graph.add_edge("validate", "output")

compiled_graph = graph.compile()
