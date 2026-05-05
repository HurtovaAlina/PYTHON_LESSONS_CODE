

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HelloResponse(BaseModel):
    message: str


@app.get("/greeting")
def hello() -> HelloResponse:
    return HelloResponse(message = "Привіт з сервера2")
