from fastapi import FastAPI

from schemas import UserQuery
from routes import call_ml_service

app = FastAPI(
    title="API Gateway"
)

@app.get("/")
def home():
    return {
        "message": "API Gateway Running"
    }

@app.post("/chat")
def chat(data: UserQuery):

    result = call_ml_service(
        data.message
    )

    return {
        "user_query": data.message,
        "prediction": result
    }