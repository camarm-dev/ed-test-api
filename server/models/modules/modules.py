from enum import Enum
from pydantic import BaseModel


class ModuleCodes(Enum):
    BARCODE = 'CANTINE_BARCODE'
    SCHOOL_LIFE = 'VIE_SCOLAIRE'
    CLASS_LIFE = 'VIE_DE_LA_CLASSE'
    GRADES = 'NOTES'
    CLOUD = 'CLOUD'
    MESSAGES = 'MESSAGERIE'
    TIMETABLE = 'EDT'


class Module(BaseModel):
    code: ModuleCodes
