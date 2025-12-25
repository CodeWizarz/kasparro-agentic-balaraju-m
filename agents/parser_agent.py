import json

class ProductDataParserAgent:
    def parse(self, raw_data: dict) -> dict:
        return {
            "name": raw_data["name"],
            "concentration": raw_data["concentration"],
            "skin_type": raw_data["skin_type"],
            "ingredients": raw_data["ingredients"],
            "benefits": raw_data["benefits"],
            "usage": raw_data["usage"],
            "side_effects": raw_data["side_effects"],
            "price": raw_data["price"]
        }
