def generate_safety_block(product: dict) -> dict:
    warnings = []
    if product.get("side_effects"):
        warnings.append("Patch test recommended before full use")

    return {
        "side_effects": product["side_effects"],
        "warnings": warnings
    }
