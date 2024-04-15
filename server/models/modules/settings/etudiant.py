from pydantic import BaseModel


class EtudiantParameters(BaseModel):
    url: str
