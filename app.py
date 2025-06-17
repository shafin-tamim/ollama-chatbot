from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:3b"  # You can keep this or change to any other model you have installed

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    payload = {
        "model": MODEL_NAME,
        "prompt": user_input,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            bot_reply = response.json()["response"]
            return jsonify({"reply": bot_reply})
        else:
            return jsonify({"reply": "Error from Ollama: " + response.text})
    except Exception as e:
        return jsonify({"reply": "Exception occurred: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)
