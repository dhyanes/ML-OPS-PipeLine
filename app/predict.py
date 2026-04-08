from flask import Flask, request, jsonify
import mlflow.pyfunc
import time

from prometheus_client import start_http_server
from metrics import REQUEST_COUNT, REQUEST_LATENCY

app = Flask(__name__)

# Start Prometheus metrics server
start_http_server(8000)

model = mlflow.pyfunc.load_model("models:/mlops-experiment/1")

@app.route("/predict", methods=["POST"])
def predict():
    REQUEST_COUNT.inc()
    
    start_time = time.time()

    data = request.json
    prediction = model.predict([[data["x"]]])

    REQUEST_LATENCY.observe(time.time() - start_time)

    return jsonify({"prediction": int(prediction[0])})

app.run(host="0.0.0.0", port=5000)