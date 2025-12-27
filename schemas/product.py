from pydantic import BaseModel
from typing import List, Dict

class ProductOverview(BaseModel):
    product_name: str
    concentration: str
    target_skin_type: List[str]
    key_ingredients: List[str]

class ProductBenefit(BaseModel):
    benefit: str
    reason: str

class ProductPage(BaseModel):
    overview: ProductOverview
    benefits: List[ProductBenefit]
    usage: Dict[str, List[str]]
    safety: Dict[str, List[str]]
    pricing: Dict[str, str]
