from pydantic import BaseModel


class BarcodeParameters(BaseModel):
    numeroBadge: str
