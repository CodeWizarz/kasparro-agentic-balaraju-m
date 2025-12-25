# import json
# from agents.parser_agent import ProductDataParserAgent

# with open("data/product_input.json") as f:
#     raw_product = json.load(f)

# parser = ProductDataParserAgent()
# product_model = parser.parse(raw_product)

# print(product_model)


import json

from agents.parser_agent import ProductDataParserAgent
from agents.question_agent import QuestionGenerationAgent
from logic_blocks.benefits import generate_benefits_block


def main():
    # 1. Load raw product data
    with open("data/product_input.json") as f:
        raw_product = json.load(f)

    # 2. Parse product data
    parser = ProductDataParserAgent()
    product_model = parser.parse(raw_product)

    print("Parsed Product Model:")
    print(product_model)
    print("-" * 50)

    # 3. Generate questions
    question_agent = QuestionGenerationAgent()
    questions = question_agent.generate(product_model)

    print("Generated Questions:")
    print(questions)
    print("-" * 50)

    # 4. Generate benefits block
    benefits_block = generate_benefits_block(product_model)

    print("Benefits Block:")
    print(benefits_block)


if __name__ == "__main__":
    main()
