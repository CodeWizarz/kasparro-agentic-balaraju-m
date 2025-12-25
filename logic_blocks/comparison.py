def compare_products_block(product_a: dict, product_b: dict) -> dict:
    return {
        "product_a": {
            "name": product_a["name"],
            "ingredients": product_a["ingredients"],
            "benefits": product_a["benefits"],
            "price": product_a["price"]
        },
        "product_b": {
            "name": product_b["name"],
            "ingredients": product_b["ingredients"],
            "benefits": product_b["benefits"],
            "price": product_b["price"]
        },
        "comparison_summary": {
            "price_difference": product_b["price"] - product_a["price"],
            "ingredient_difference": list(
                set(product_a["ingredients"]) - set(product_b["ingredients"])
            )
        }
    }
