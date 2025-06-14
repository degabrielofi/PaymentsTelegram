from flask import Flask, request, jsonify
import telebot
import os
from database import salvar_pagamento
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TOKEN = os.getenv('TELEGRAM_TOKEN')
GRUPO_ID = int(os.getenv('GRUPO_ID'))
bot = telebot.TeleBot(TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data.get("status") == "APPROVED":
        nome = data["customer"]["name"]
        plano = data["items"][0]["title"].lower()
        txid = data["paymentId"]
        user_id = int(txid[-6:], 36) % 999999999

        salvar_pagamento(user_id, nome, plano, txid)

        try:
            link = bot.create_chat_invite_link(GRUPO_ID, member_limit=1)
            bot.send_message(user_id, f"✅ Pagamento aprovado!\nAcesse o grupo: {link.invite_link}")
        except Exception as e:
            print("Erro ao enviar link:", e)
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)