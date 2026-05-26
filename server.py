#!/usr/bin/env python3
"""QuantumForge — Multi-Agent Quantum Circuit Design & Simulation"""
import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "project": "QuantumForge", "agents": 8})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8104))
    app.run(host="0.0.0.0", port=port)
