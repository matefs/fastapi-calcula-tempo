from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"Hello": name}

