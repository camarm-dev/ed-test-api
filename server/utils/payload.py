import json
from urllib.parse import unquote
from fastapi import Request


async def get_payload(request: Request):
    body = unquote((await request.body()).decode())
    data = json.loads(body.replace('data=', '', 1))
    return data
