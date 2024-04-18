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


def is_token_valid(token: str):
    try:
        jwt.decode(token, SECRET)
        return True
    except jwt.PyJWTError:
        return False


def get_user(token: str):
    return jwt.decode(token, SECRET)['user']
