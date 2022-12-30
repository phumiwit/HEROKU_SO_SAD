from fastapi import FastAPI
import uvicorn
from key import Keyword_Spotting_Service
from pydantic import BaseModel


class file(BaseModel):
    file: str
    
class file1(BaseModel):
    file:str
app = FastAPI()

@app.get('/')
def Hello():
    return {'Hello':'Hello'}

@app.post('/predict')
async def predict(path:file):
    kss = Keyword_Spotting_Service()
    keyword1,keyword2= kss.prediction(path.file)
    return {"prediction":keyword1}

@app.post('/value')
async def value(path:file1):
    kss = Keyword_Spotting_Service()
    keyword1,keyword2 = kss.prediction(path.file)
    return keyword2


if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)