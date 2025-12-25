def generate_benefits_block(product: dict) -> dict:
    benefits = []
    for benefit in product["benefits"]:
        reason = "Derived from key ingredients"

        if benefit.lower() == "brightening":
            reason = "Vitamin C helps improve skin brightness"
        elif "dark" in benefit.lower():
            reason = "Vitamin C supports reduction of dark spots"

        benefits.append({
            "benefit": benefit,
            "reason": reason
        })

    return {
        "benefits": benefits
    }
