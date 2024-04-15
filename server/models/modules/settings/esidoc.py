from typing import List
from pydantic import BaseModel


class EsidocParameters(BaseModel):
    tabParams: List[EsidocTabParam]

class EsidocTabParam(BaseModel):
    libelle: str
    url: str
