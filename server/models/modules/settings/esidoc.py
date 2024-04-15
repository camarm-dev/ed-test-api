from typing import List
from pydantic import BaseModel


class EsidocTabParam(BaseModel):
    libelle: str
    url: str


class EsidocParameters(BaseModel):
    tabParams: List[EsidocTabParam]
