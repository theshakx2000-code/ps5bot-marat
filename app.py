from flask import Flask, request
import requests, os

app = Flask(__name__)

GREEN_ID = os.getenv("GREEN_API_INSTANCE")
GREEN_TOKEN = os.getenv("GREEN_API_TOKEN")

@app.route("/", methods=["GET"])
def home():
    return "Бот Марат онлайн ✅"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data or "body" not in data:
        return {"status": "no data"}

    message = data["body"].get("messageData", {}).get("textMessageData", {}).get("textMessage", "")
    chat_id = data["body"].get("senderData", {}).get("chatId")

    if message and chat_id:
        reply = f"Привет! 👋 Это Марат. Аренда PS4 и PS5 в Новом Уренгое. Что вас интересует?"
        send_message(chat_id, reply)
    return {"status": "ok"}

def send_message(chat_id, text):
    url = f"https://api.green-api.com/waInstance{GREEN_ID}/sendMessage/{GREEN_TOKEN}"
    requests.post(url, json={"ch
  atId": chat_id, "message": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
  
