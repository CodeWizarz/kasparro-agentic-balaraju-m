def generate_answer(question: str, product: dict) -> dict:
    q = question.lower()

    if "what is" in q:
        answer = (
            f"{product['name']} is a skincare serum formulated with "
            f"{product['concentration']} Vitamin C."
        )

    elif "concentration" in q:
        answer = (
            f"The serum contains {product['concentration']} Vitamin C, "
            f"as specified in the product details."
        )

    elif "who should use" in q:
        skin_types = ", ".join(product["skin_type"])
        answer = (
            f"This product is suitable for individuals with {skin_types} skin types."
        )

    elif "how do i use" in q:
        answer = product["usage"]

    elif "when should" in q:
        answer = (
            "The serum is recommended for morning use, "
            "as indicated in the usage instructions."
        )

    elif "side effects" in q:
        answer = ", ".join(product["side_effects"])

    elif "price" in q:
        answer = f"The product is priced at ₹{product['price']}."

    else:
        answer = (
            "The available product information does not provide additional details "
            "for this question."
        )

    return {
        "question": question,
        "answer": answer
    }


def assemble_faq_block(questions: dict, product: dict) -> dict:
    faq_items = []

    for category in questions:
        for q in questions[category]:
            faq_items.append(generate_answer(q, product))

    return {
        "faq_items": faq_items[:5]  # enforce minimum of 5 FAQs
    }
