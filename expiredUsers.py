from db import verificar_expirados, remover_usuario
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))
GRUPO_ID = int(os.getenv('GRUPO_ID'))

expirados = verificar_expirados()
for user in expirados:
    try:
        bot.ban_chat_member(GRUPO_ID, user['user_id'])
        remover_usuario(user['txid'])
        print(f"Usuário {user['user_id']} removido por expiração.")
    except Exception as e:
        print(f"Erro ao remover {user['user_id']}: {e}")