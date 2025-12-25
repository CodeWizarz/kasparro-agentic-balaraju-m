import json

from agents.parser_agent import ProductDataParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.logic_agent import ContentLogicAgent
from agents.template_agent import TemplateAgent
from agents.assembler_agent import PageAssemblerAgent


def load_template(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def main():
    # --------------------------------------------------
    # 1. Load raw input data
    # --------------------------------------------------
    with open("data/product_input.json", "r") as f:
        raw_product = json.load(f)

    with open("data/fictional_product_b.json", "r") as f:
        product_b = json.load(f)

    # --------------------------------------------------
    # 2. Parse product data
    # --------------------------------------------------
    parser = ProductDataParserAgent()
    product_model = parser.parse(raw_product)

    print("Parsed Product Model:")
    print(product_model)
    print("-" * 50)

    # --------------------------------------------------
    # 3. Generate questions
    # --------------------------------------------------
    question_agent = QuestionGenerationAgent()
    questions = question_agent.generate(product_model)

    print("Generated Questions:")
    print(questions)
    print("-" * 50)

    # --------------------------------------------------
    # 4. Generate all content logic blocks via LogicAgent
    # --------------------------------------------------
    logic_agent = ContentLogicAgent()
    blocks = logic_agent.generate_blocks(
        product=product_model,
        questions=questions,
        product_b=product_b
    )

    print("Content Logic Blocks Generated:")
    print(list(blocks.keys()))
    print("-" * 50)

    # --------------------------------------------------
    # 5. Load templates
    # --------------------------------------------------
    faq_template = load_template("templates/faq_template.json")
    product_template = load_template("templates/product_template.json")
    comparison_template = load_template("templates/comparison_template.json")

    # --------------------------------------------------
    # 6. Apply templates
    # --------------------------------------------------
    template_agent = TemplateAgent()

    faq_page = template_agent.apply_template(faq_template, blocks)
    product_page = template_agent.apply_template(product_template, blocks)
    comparison_page = template_agent.apply_template(comparison_template, blocks)

    # --------------------------------------------------
    # 7. Save output pages
    # --------------------------------------------------
    assembler = PageAssemblerAgent()
    assembler.save_page(faq_page, "faq.json")
    assembler.save_page(product_page, "product_page.json")
    assembler.save_page(comparison_page, "comparison_page.json")

    print("✅ FAQ, Product & Comparison pages generated successfully.")


if __name__ == "__main__":
    main()
