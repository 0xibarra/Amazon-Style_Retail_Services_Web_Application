from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Catalog Service Running"

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Amazon Echo Show 11", "price": 249.99},
        {"id": 2, "name": "Bounty Paper Towels, 16 Family Rolls", "price": 45.19},
        {"id": 3, "name": "American Silver Eagle 1 oz Bullion Coin with Certificate of Authenticity", "price": 88.95}
    ])

app.run(host="0.0.0.0", port=5001)
