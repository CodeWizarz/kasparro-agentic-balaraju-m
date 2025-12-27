from pydantic import BaseModel
from typing import List, Dict

class ProductSummary(BaseModel):
    name: str
    ingredients: List[str]
    benefits: List[str]
    price: int

class ComparisonSummary(BaseModel):
    price_difference: int
    ingredient_difference: List[str]

class ComparisonPage(BaseModel):
    product_a: ProductSummary
    product_b: ProductSummary
    comparison_summary: ComparisonSummary
