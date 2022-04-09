from flask import Flask, jsonify, request
from clf import get_prediction

app = Flask(__name__)

@app.route("/predict-alphabets", methods = ["POST"])
def predict_data():
    image = request.files.get("alphabets")
    prediction = get_prediction(image)
    return jsonify({
        "prediction": prediction
    }), 200

    if __name__ === "__main__":
        app.run(debug = True)