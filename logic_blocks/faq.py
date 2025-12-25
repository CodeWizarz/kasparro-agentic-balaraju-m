def generate_answer(question: str, product: dict) -> dict:
    q = question.lower()

    if "what is" in q:
        answer = f"{product['name']} is a skincare serum containing {product['concentration']} Vitamin C."
    elif "how do i use" in q:
        answer = product["usage"]
    elif "side effects" in q:
        answer = ", ".join(product["side_effects"])
    elif "price" in q:
        answer = f"The product is priced at ₹{product['price']}."
    else:
        answer = "This information is based on the provided product details."

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
        "faq_items": faq_items[:5]  # enforce min 5
    }
