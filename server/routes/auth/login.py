from fastapi import Request, Depends
from sqlalchemy.orm import Session

from server.main import app
from server.models.accounts.student import Student
from server.utils.auth import authenticate_user, generate_token, is_access_token_valid, authenticate_access_token, \
    generate_access_token
from server.utils.database import get_database
from server.utils.payload import get_payload
from server.utils.response import response
from server.errors import ERRORS


def login_response(user: Student):
    token = generate_token(user.id)
    data = {
        "accounts": [user]
    }
    return response(data, token, 200, "Connexion réussie !")


async def re_login_procedure(body: dict, db: Session):
    access_token = body.get('accessToken', '')
    if is_access_token_valid(access_token):
        username = body.get('username', '')
        user = await authenticate_access_token(username, access_token, db)
        return login_response(user)
    return ERRORS.INVALID_TOKEN


async def login_procedure(body: dict, db: Session):
    username = body.get('identifiant', '')
    password = body.get('motdepasse', '')

    user = await authenticate_user(username, password, db)

    uuid = body.get('uuid', None)
    remember_me = body.get('sesouvenirdemoi', False)

    if user:
        if uuid and remember_me:
            user['accessToken'] = generate_access_token(uuid)
        return login_response(user)
    return ERRORS.INVALID_CREDS


@app.post('/login.awp', tags=['auth'])
async def login(request: Request, db: Session = Depends(get_database)):
    body = await get_payload(request)
    re_login = body.get('isRelogin', False)
    if re_login:
        return await re_login_procedure(body, db)
    return await login_procedure(body, db)

