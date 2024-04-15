def response(data: dict, token: str = "", code: int = 200, message: str = ""):
    return {
        "code": code,
        "token": token,
        "host": "HTTP<ed-test-srv>",
        "message": message,
        "data": data
    }


def error(error: int, message: str):
    data = {
        "accounts": []
    }
    return response(data, "", error, message)
