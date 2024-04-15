from pydantic import BaseModel
from server.types.fakebool import FakeBool


class DocumentsParameters(BaseModel):
    DocumentsNotesActif: FakeBool
    DocumentsVSActif: FakeBool
    DocumentsAdministratifActif: FakeBool
    AnneArchive: str
