import datetime
import hashlib

import jwt
from sqlalchemy.orm import Session

from server.main import CONFIGURATION
from server.models.accounts.student import Student

SECRET = CONFIGURATION['secret']


def hash_password(password: str):
    return hashlib.sha3_512(password.encode()).hexdigest()


def authenticate_user(username: str, password: str, database: Session):
    user = database.query(Student).filter(Student.identifiant == username).first()
    if user['password'] == hash_password(password):
        return user
    return None


def generate_token(user_id: int):
    payload = {
        'user': user_id
    }
    expire = datetime.datetime.now() + datetime.timedelta(hours=1)
    payload["exp"] = expire
    return jwt.encode(payload, SECRET)


def generate_access_token(uuid: str):
    payload = {
        'uuid': uuid
    }
    expire = datetime.datetime.now() + datetime.timedelta(hours=24 * 365.25 * 3)
    payload["exp"] = expire
    return jwt.encode(payload, SECRET)


def is_token_valid(token: str):
    try:
        data = jwt.decode(token, SECRET)
        expire = data['exp']
        if datetime.datetime.now() > datetime.datetime.fromisoformat(expire):
            return False
        return True
    except jwt.PyJWTError:
        return False


def is_access_token_valid(token: str, uuid: str):
    if is_token_valid(token):
        data = jwt.decode(token, SECRET)
        token_uuid = data.get('uuid')
        return token_uuid == uuid
    return False


def get_user(token: str):
    return jwt.decode(token, SECRET)['user']
