import json

from agents.parser_agent import ProductDataParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.template_agent import TemplateAgent
from agents.assembler_agent import PageAssemblerAgent

from logic_blocks.benefits import generate_benefits_block
from logic_blocks.usage import generate_usage_block
from logic_blocks.safety import generate_safety_block
from logic_blocks.faq import assemble_faq_block
from logic_blocks.comparison import compare_products_block


def load_template(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def main():
    # --------------------------------------------------
    # 1. Load raw product data
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
    # 4. Generate logic blocks
    # --------------------------------------------------
    benefits_block = generate_benefits_block(product_model)
    usage_block = generate_usage_block(product_model)
    safety_block = generate_safety_block(product_model)
    faq_block = assemble_faq_block(questions, product_model)

    # Comparison logic block
    comparison_block = compare_products_block(product_model, product_b)

    print("Logic Blocks Generated")
    print("-" * 50)

    # --------------------------------------------------
    # 5. Load templates
    # --------------------------------------------------
    faq_template = load_template("templates/faq_template.json")
    product_template = load_template("templates/product_template.json")
    comparison_template = load_template("templates/comparison_template.json")

    # --------------------------------------------------
    # 6. Assemble blocks dictionary
    # --------------------------------------------------
    blocks = {
        "benefits": benefits_block,
        "usage": usage_block,
        "safety": safety_block,
        "faq": faq_block,
        "comparison": comparison_block
    }

    # --------------------------------------------------
    # 7. Apply templates
    # --------------------------------------------------
    template_agent = TemplateAgent()

    faq_page = template_agent.apply_template(faq_template, blocks)
    product_page = template_agent.apply_template(product_template, blocks)
    comparison_page = template_agent.apply_template(comparison_template, blocks)

    # --------------------------------------------------
    # 8. Save output pages
    # --------------------------------------------------
    assembler = PageAssemblerAgent()
    assembler.save_page(faq_page, "faq.json")
    assembler.save_page(product_page, "product_page.json")
    assembler.save_page(comparison_page, "comparison_page.json")

    print("✅ FAQ, Product & Comparison pages generated successfully.")


if __name__ == "__main__":
    main()
