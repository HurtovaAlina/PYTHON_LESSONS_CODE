from fastapi import FastAPI

#create object

app = FastAPI()

@app.get("/hello_endpoint")
def hello():
    return {
        "message": "hello",
        "status" : "OK"
    }
