from flask import Flask, request, jsonify
import mlflow.pyfunc

app = Flask(__name__)

model = mlflow.pyfunc.load_model("models:/mlops-experiment/1")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([[data["x"]]])
    return jsonify({"prediction": int(prediction[0])})

app.run(host="0.0.0.0", port=5000)