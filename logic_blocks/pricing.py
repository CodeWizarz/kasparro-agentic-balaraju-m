def generate_pricing_block(product: dict) -> dict:
    price = product["price"]

    if price < 500:
        category = "Budget"
    elif price <= 1000:
        category = "Mid-range"
    else:
        category = "Premium"

    return {
        "price_inr": price,
        "price_category": category
    }
