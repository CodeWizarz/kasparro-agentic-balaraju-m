import json
import os

def test_outputs_exist():
    assert os.path.exists("output/faq.json")
    assert os.path.exists("output/product_page.json")
    assert os.path.exists("output/comparison_page.json")

def test_faq_count():
    with open("output/faq.json") as f:
        faq = json.load(f)
    assert len(faq) >= 5

def test_product_page_structure():
    with open("output/product_page.json") as f:
        product = json.load(f)
    assert "overview" in product
    assert "benefits" in product
    assert "usage" in product
