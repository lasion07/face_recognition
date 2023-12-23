from fastapi import FastAPI
from pydantic import BaseModel

# from model import Model


app = FastAPI()

class FindInput(BaseModel):
    path: str

class FindOutput(BaseModel):
    objects: list[list, str]

@app.get("/")
async def home():
    return {"health_check": "OK"}

@app.post("/find", respone_model=FindOutput)
async def find(path: FindInput):
    # model = Model()
    # objects = model.run(path)
    return objects