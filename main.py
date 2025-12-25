import json
from agents.parser_agent import ProductDataParserAgent

with open("data/product_input.json") as f:
    raw_product = json.load(f)

parser = ProductDataParserAgent()
product_model = parser.parse(raw_product)

print(product_model)
