from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
import model

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# pydantic models
class SequenceIn(BaseModel):
    sequence: str
    protein: str

class SequenceOut(SequenceIn):
    result: dict

@app.post("/predict", response_model=SequenceOut, status_code=200)
def get_prediction(payload: SequenceIn):
    sequence = payload.sequence
    protein = payload.protein

    prediction = model.predict(sequence, protein)
    
    if not prediction:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "sequence": sequence,
        "protein": protein, 
        "result": model.convert(prediction)
    }
    
    return response_object