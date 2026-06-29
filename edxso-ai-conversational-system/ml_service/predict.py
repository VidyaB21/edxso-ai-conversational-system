from model import classifier

LABELS = [
    "password_reset",
    "order_tracking",
    "cancel_order",
    "refund_request"
]

def predict_intent(text):

    result = classifier(
        text,
        candidate_labels=LABELS
    )

    return {
        "intent": result["labels"][0],
        "confidence": round(result["scores"][0], 4)
    }