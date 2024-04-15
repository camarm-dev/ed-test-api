from pydantic import BaseModel

from server.types.fakebool import FakeBool


class MessagesParameters(BaseModel):
    isActif: FakeBool
    canParentsLireMessagesEnfants: FakeBool
    destAdmin: FakeBool
    destEleve: FakeBool
    destFamille: FakeBool
    destProf: FakeBool
    destEspTravail: FakeBool
    disabledNotification: FakeBool
    notificationEmailEtablissement: FakeBool
    choixMailNotification: FakeBool
    autreMailNotification: str
    mailPro: str
    mailPerso: str
    messagerieApiVersion: str
    blackListProfActive: FakeBool
    estEnBlackList: FakeBool
    afficherToutesLesClasses: FakeBool
