import json
import os

class PageAssemblerAgent:
    def save_page(self, page: dict, filename: str):
        os.makedirs("output", exist_ok=True)
        with open(f"output/{filename}", "w") as f:
            json.dump(page, f, indent=2)
