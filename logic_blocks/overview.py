def generate_overview_block(product: dict) -> dict:
    return {
        "product_name": product["name"],
        "concentration": product["concentration"],
        "target_skin_type": product["skin_type"],
        "key_ingredients": product["ingredients"]
    }
