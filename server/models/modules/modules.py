from enum import Enum
<<<<<<< HEAD
from typing import Optional
from pydantic import BaseModel

from server.models.modules.settings.barcode import BarcodeParameters
from server.models.modules.settings.cloud import CloudParameters
from server.models.modules.settings.documents import DocumentsParameters
from server.models.modules.settings.esidoc import EsidocParameters
from server.models.modules.settings.etudiant import EtudiantParameters
from server.models.modules.settings.messages import MessagesParameters
from server.models.modules.settings.reservations import ReservationsParameters
from server.models.modules.settings.textbook import TextbookParameters

=======
from pydantic import BaseModel

>>>>>>> 92fbd08 (fix: nouvelle structure)

class ModuleCodes(Enum):
    BARCODE = 'CANTINE_BARCODE'
    SCHOOL_LIFE = 'VIE_SCOLAIRE'
    CLASS_LIFE = 'VIE_DE_LA_CLASSE'
    GRADES = 'NOTES'
    CLOUD = 'CLOUD'
    MESSAGES = 'MESSAGERIE'
    TIMETABLE = 'EDT'
<<<<<<< HEAD
    DOCUMENTS = 'DOCUMENTS_ELEVES'
    TEXTBOOK = 'CAHIER_DE_TEXTES'
    QCM = 'QCM'
    RESERVATIONS = 'RESERVATIONS'
    CORRESPONDANCE_BOOK = 'CARNET_CORRESPONDANCE'
    ESIDOC = 'ESIDOC'
    EDUANO = 'EDUANO'
    CATER = 'CATER'
    ARD = 'ARD'
    PEARLTREES = 'PEARLTREES'
    EDUMALIN = 'EDUMALIN'
    SUIVI_STAGE = 'SUIVI_STAGE'
    CLICKNPLAY = 'CLICKNPLAY'
    VOLTAIRE = 'VOLTAIRE'
    ONISEPSERVICES = 'ONISEPSERVICES'
    AVENRIA = 'AVENRIA'
    SACOCHE = 'SACOCHE'
    ETUDIANT = 'ETUDIANT'
    IJBOX = 'IJBOX'


class ModulesParameters(Enum):
    BARCODE = BarcodeParameters
    CLOUD = CloudParameters
    MESSAGES = MessagesParameters
    DOCUMENTS = DocumentsParameters
    TEXTBOOK = TextbookParameters
    RESERVATIONS = ReservationsParameters
    ESIDOC = EsidocParameters
    EDUDIANT = EtudiantParameters

class Module(BaseModel):
    code: ModuleCodes
    params: Optional[ModulesParameters]
=======


class Module(BaseModel):
    code: ModuleCodes
>>>>>>> 92fbd08 (fix: nouvelle structure)
