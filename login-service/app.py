from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    static_folder=str(PROJECT_DIR / "styling"),
    static_url_path="/styling"
)

CORS(app)

@app.route("/")
def home():
    return "Login Service Running"

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pw = request.form.get("password")

    if user == "admin" and pw == "password123":
        print("Login Successful")
        return jsonify({"status": "success", "message": "Login Successful"})

    print("Login Failed")
    return jsonify({"status": "failure", "message": "Login Failed"})

app.run(host="0.0.0.0", port=5002)
