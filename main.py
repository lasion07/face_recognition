from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from model import Model
from utils.commons import read_image_from_Bytes

app = FastAPI()

model = Model()

class Input(BaseModel):
    path: str

class FindOutput(BaseModel):
    name: list[str]

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/find")
async def find(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    input_image = read_image_from_Bytes(contents)

    # results = model.run(input_image) # Debug

    try:
        results = model.run(input_image)
    except Exception:
        return {"message": "There was an error when finding the face(s)"}
    
    return {"results": results}