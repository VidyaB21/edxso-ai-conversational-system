import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")

with mlflow.start_run():

    mlflow.log_param(
        "model",
        "LogisticRegression"
    )

    mlflow.log_metric(
        "accuracy",
        0.25
    )

    mlflow.log_metric(
        "precision",
        0.25
    )

    mlflow.log_metric(
        "recall",
        0.25
    )

print("Metrics Logged Successfully")