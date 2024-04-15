from server.utils.response import error


class ERRORS:
    INVALID_CREDS = lambda _: error(505, "Identifiant et/ou mot de passe invalide !")
    INVALID_TOKEN = lambda _: error(520, "Token invalide")
    EXPIRED_TOKEN = lambda _: error(525, "Token expiré")
    INVALID_FORMAT = lambda _: error(40129, "Format JSON invalide")
