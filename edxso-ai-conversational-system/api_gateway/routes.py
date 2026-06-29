import requests

ML_SERVICE_URL = "http://127.0.0.1:8001/predict"

def call_ml_service(message):

    response = requests.post(
        ML_SERVICE_URL,
        json={
            "message": message
        }
    )

    return response.json()