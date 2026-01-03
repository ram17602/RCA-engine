from fastapi import FastAPI
from .agent import handle_event


app = FastAPI()

@app.post("/analyze")
def analyze(event: dict):
    return handle_event(event)
