from fastapi import Request, Depends
from sqlalchemy.orm import Session

from server.main import app
from server.utils.auth import authenticate_user, generate_token
from server.utils.database import get_database
from server.utils.payload import get_payload
from server.utils.response import response
from server.errors import ERRORS


@app.post('/login.awp', tags=['auth'])
async def login(request: Request, db: Session = Depends(get_database)):
    body = await get_payload(request)
    username = body['username']
    password = body['password']
    user = await authenticate_user(username, password, db)
    if user:
        token = generate_token(user.id)
        data = {
            "accounts": [user]
        }
        return response(data, token, 200, "Connexion réussie !")
    return ERRORS.INVALID_CREDS

