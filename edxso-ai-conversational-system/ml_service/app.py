from fastapi import FastAPI
from pydantic import BaseModel

from predict import predict_intent

app = FastAPI(
    title="ML Service"
)

class UserInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "message": "ML Service Running"
    }

@app.post("/predict")
def predict(data: UserInput):

    result = predict_intent(
        data.message
    )

    return result