import json
import os

def test_faq_count():
    import json, os

    with open("output/faq.json") as f:
        faqs = json.load(f)

    assert len(faqs) >= 15, "Less than 15 FAQs generated"

