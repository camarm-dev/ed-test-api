import json
import uvicorn
from fastapi import FastAPI, Request
from fastapi.datastructures import Headers
from urllib.parse import unquote
from utils import *

app = FastAPI(title="EcoleDirecte test API")
accounts = {
    "avraidireonsenfoucestpourtestmaisvoicitontoken": {
        "username": "jean",
        "password": "jean%",
        "id": 0
    },
    "marieaussiauntokenetellepeutseconnecteraedsuper": {
        "username": "marie",
        "password": "marie%",
        "id": 1
    }
}

requests_count = {
    "avraidireonsenfoucestpourtestmaisvoicitontoken": 0,
    "marieaussiauntokenetellepeutseconnecteraedsuper": 0
}

temp_data = {

}


def read_json(path: str):
    return json.loads(open(path).read())


def error_request(error: int):
    if error == 505:
        return {
            "code": 505,
            "token": "",
            "host": "HTTP<ed-test-srv>",
            "message": "Identifiant et/ou mot de passe invalide !",
            "data": {
                "accounts": []
            }
        }
    elif error == 520:
        return {
            "code": 520,
            "token": "",
            "host": "HTTP<ed-test-srv>",
            "message": "Token invalide",
            "data": {
                "accounts": []
            }
        }
    elif error == 525:
        return {
            "code": 525,
            "token": "",
            "host": "HTTP<ed-test-srv>",
            "message": "Token expiré",
            "data": {
                "accounts": []
            }
        }
    elif error == 40129:
        return {
            "code": 40129,
            "token": "",
            "host": "HTTP<ed-test-srv>",
            "message": "Format JSON invalide",
            "data": {
                "accounts": []
            }
        }
    return {
        "code": error,
        "token": "",
        "host": "HTTP<ed-test-srv>",
        "message": "Erreur",
        "data": {
            "accounts": []
        }
    }


def loginMiddleware(data: dict, headers: Headers, path: str):
    if path == '/login.awp':
        username = data['identifiant']
        password = data['motdepasse']
        for token, user in accounts.items():
            if user['username'] == username:
                if user['password'] == password:
                    return True, username, token, 200
        return False, '', '', 505
    else:
        token = headers.get('X-Token', '')
        if token in accounts.keys():
            if requests_count[token] > 10 and not conf['static_token']:
                return False, '', '', 525
            return True, accounts['token']['username'], '', 200
        else:
            return False, '', '', 520


if __name__ == '__main__':
    conf = read_json("config.json")
    routes = read_json("requests.json")

    # Register routes
    for route in routes.keys():
        schema = read_json('responses/' + routes[route])

        @app.post(route)
        async def handler(request: Request, verbe: str = 'default', v: str = 'unknown'):
            print(f"[{route}] Receiving \"{verbe}\" request, requesting version {v}")
            body = unquote((await request.body()).decode())
            data = json.loads(body.replace('data=', '', 1))

            is_logged_in, user, token, code = loginMiddleware(data, request.headers, route)

            if is_logged_in:
                print(f"--> {verbe}.response.{user}")
                response = schema[verbe]['response'][user]
                response['token'] = token
                # Execute action
                eval(schema['action'])
                return response
            else:
                return error_request(code)

    uvicorn.run(app)
