from fastapi import FastAPI, Depends
from jwt_utils import create_token


app = FastAPI()


@app.post("/login")
def login(user: str):
    return create_token(user)