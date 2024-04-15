from enum import Enum

from server.utils.response import error


class ERRORS(Enum):
    OBJECT_NOT_FOUND = error(210, "Object not found")
    DUAL_AUTH_REQUIRED = error(250, "Identifiant et/ou mot de passe invalide !")
    UNAUTHORIZED = error(403, "Accès interdit")
    INVALID_CREDS = error(505, "Identifiant et/ou mot de passe invalide !")
    INVALID_BODY = error(512, "Session expiré")
    INVALID_VERSION = error(517, "Version invalide")
    INVALID_TOKEN = error(520, "Token invalide")
    EXPIRED_TOKEN = error(525, "Token expiré")
    EXPIRED_SESSION = error(526, "Session expirée")
    INVALID_FORMAT = error(40129, "Format JSON invalide")
