import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Dummy dataset
data = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [0, 0, 1, 1]
})

X = data[["x"]]
y = data["y"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model/model.pkl")
print("Model trained and saved!")