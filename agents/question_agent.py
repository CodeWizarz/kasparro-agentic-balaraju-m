class QuestionGenerationAgent:
    def generate(self, product: dict) -> dict:
        questions = {
            "informational": [
                f"What is {product['name']}?",
                f"What concentration of Vitamin C does {product['name']} contain?",
                f"Who should use {product['name']}?"
            ],
            "usage": [
                f"How do I use {product['name']}?",
                "When should this serum be applied?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is this serum suitable for sensitive skin?"
            ],
            "purchase": [
                f"What is the price of {product['name']}?",
                "Is this product affordable compared to similar serums?"
            ],
            "comparison": [
                f"How does {product['name']} compare to other Vitamin C serums?"
            ]
        }
        return questions
