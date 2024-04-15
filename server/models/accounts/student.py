from typing import List, Optional
from pydantic import BaseModel
from server.models.accounts.roles import Roles
from server.models.modules.modules import Module
from server.models.classes.school_class import Class


class StudentSettings(BaseModel):
    lsuPoilDansLaMainBorne1: str
    lsuPoilDansLaMainBorne2: str
    lsuPoilDansLaMainBorne3: str
    modeCalculLSU: str
    isQrcode: bool
    modeAccessibiliteVisuelle: bool
    typeSaisieNotesDefaut: str
    nbJoursMaxRenduDevoirCDT: str


class StudentProfile(BaseModel):
    sexe: str
    infoEDT: str
    nomEtablissement: str
    idEtablissement: str
    idReelEtab: str
    photo: str
    classe: Optional[Class]


class Student(BaseModel):

    idLogin: int
    id: int
    uid: str
    identifiant: str

    typeCompte: Roles.STUDENT
    codeOgec: str
    main: bool
    lastConnexion: str

    civilite: str
    prenom: str
    particule: str
    nom: str
    email: str

    anneeScolaireCourante: str

    nomEtablissement: str
    logoEtablissement: str
    couleurAgendaEtablissement: str
    dicoEnLigneLeRobert: bool

    accessToken: str
    socketToken: str

    modules: List[Module]

    parametresIndividuels: StudentSettings
    profile: StudentProfile
