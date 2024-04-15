from pydantic import BaseModel
from server.types.fakebool import FakeBool


class CloudParameters(BaseModel):
    padsActif: FakeBool
