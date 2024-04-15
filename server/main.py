import json
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine

from server.utils.response import response

app = FastAPI(title="EcoleDirecte test API")


@app.get('/')
async def root():
    return response({}, message="Bienvenue sur l'API")


