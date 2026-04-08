import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Enable MLflow tracking
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("mlops-experiment")

# Dummy data
data = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [0, 0, 1, 1]
})

X = data[["x"]]
y = data["y"]

with mlflow.start_run():

    model = LogisticRegression()
    model.fit(X, y)

    # Log parameters
    mlflow.log_param("model_type", "LogisticRegression")

    # Log metrics
    accuracy = model.score(X, y)
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    print("Model logged in MLflow!")