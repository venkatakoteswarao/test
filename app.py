from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables access from Netlify

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask backend!"})
