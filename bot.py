import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
BULLSPAY_TOKEN = os.getenv('SECRET_KEY_BULL')
BULLSPAY_API = 'https://api.bullspay.net/pagamento/pix'
GRUPO_ID = int(os.getenv('GRUPO_ID'))

bot = telebot.TeleBot(TOKEN)

planos = {
    'semanal': {'nome': 'Plano Semanal', 'valor': 9.99},
    'mensal': {'nome': 'Plano Mensal', 'valor': 29.99}
}

@bot.message_handler(commands=['start', 'help'])
def inicio(m):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Plano Semanal", callback_data='semanal'),
        InlineKeyboardButton("Plano Mensal", callback_data='mensal')
    )
    bot.reply_to(m, "Escolha o plano:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in planos)
def gerar_pix(call):
    plano = planos[call.data]
    payload = {
        "token": BULLSPAY_TOKEN,
        "valor": plano['valor'],
        "referencia": str(call.from_user.id),
        "plano": call.data,
        "nome": call.from_user.first_name
    }
    r = requests.post(BULLSPAY_API, json=payload)
    data = r.json()

    if data.get('status'):
        bot.send_message(call.message.chat.id,
            f"💳 Pague usando o código Pix abaixo:\n\n`{data['copiaecola']}`",
            parse_mode='Markdown')
        bot.send_photo(call.message.chat.id, data['qrcode'])
    else:
        bot.send_message(call.message.chat.id, "Erro ao gerar pagamento. Tente novamente.")

bot.polling()