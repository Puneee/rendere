# app.py

from flask import Flask, request, jsonify
from models import run_models

app = Flask(__name__)

@app.route('/')
def home():
    return "ML Backend is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = run_models(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
