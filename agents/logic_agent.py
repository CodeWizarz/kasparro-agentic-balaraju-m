from logic_blocks.overview import generate_overview_block
from logic_blocks.benefits import generate_benefits_block
from logic_blocks.usage import generate_usage_block
from logic_blocks.safety import generate_safety_block
from logic_blocks.pricing import generate_pricing_block
from logic_blocks.faq import assemble_faq_block
from logic_blocks.comparison import compare_products_block


class ContentLogicAgent:
    def generate_blocks(self, product: dict, questions: dict, product_b: dict) -> dict:
        return {
            "overview": generate_overview_block(product),
            "benefits": generate_benefits_block(product),
            "usage": generate_usage_block(product),
            "safety": generate_safety_block(product),
            "pricing": generate_pricing_block(product),
            "faq": assemble_faq_block(questions, product),
            "comparison": compare_products_block(product, product_b)
        }
