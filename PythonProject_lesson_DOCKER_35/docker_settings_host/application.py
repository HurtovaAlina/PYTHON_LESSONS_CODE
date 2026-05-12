from fastapi import FastAPI
from settings import settings

# змінна для застосунку
app = FastAPI()


@app.get("/hello_endpoint")
def hello():
    return {"message": settings.hello_text}
