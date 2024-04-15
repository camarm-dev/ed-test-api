from enum import Enum


class Roles(str, Enum):
    STUDENT = 'E'
    TEACHER = 'P'
    STAFF = 'A'
    FAMILY = '1'
