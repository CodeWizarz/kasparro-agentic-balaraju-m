def generate_usage_block(product: dict) -> dict:
    usage_text = product["usage"]

    steps = []
    if "apply" in usage_text.lower():
        steps.append("Cleanse your face")
        steps.append("Apply 2–3 drops of the serum")
        steps.append("Use before sunscreen")

    return {
        "time_of_use": "Morning",
        "steps": steps
    }
