from dotenv import load_dotenv
load_dotenv()

from graph.graph import compiled_graph
import json

initial_state = {
    "product": json.load(open("data/product_input.json")),
    "product_b": json.load(open("data/fictional_product_b.json")),
    "questions": [],
    "faq": [],
    "product_page": {},
    "comparison_page": {},
    "errors": [],
    "retry_count": 0
}


final_state = compiled_graph.invoke(initial_state)

print("Pipeline completed successfully")
