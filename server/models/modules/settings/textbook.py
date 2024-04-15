from pydantic import BaseModel


class TextbookParameters(BaseModel):
    compteRenduSeance: str
    isCDTPrimaire: str
