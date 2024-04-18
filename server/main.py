import json

from fastapi import FastAPI, Request

from server.utils.auth import is_token_valid, get_user
from server.utils.response import response

app = FastAPI(title="EcoleDirecte test API")
with open('config.json') as file:
    CONFIGURATION = json.loads(file.read())


async def verify_token(request: Request, call_next):
    token = request.headers["X-token"]
    if is_token_valid(token):
        user = get_user(token)
        return await call_next(request)


@app.middleware("auth")
async def authentification_process(request: Request, call_next):
    if request.headers.get("X-token", "") != "":
        res = await verify_token(request, call_next)
    else:
        res = await call_next(request)
    res.headers["X-Powered-By"] = "ed-test-api <github.com/camarm-dev/ed-test-api>"
    return res


@app.get('/')
async def root():
    return response({}, message="Bienvenue sur l'API !")


