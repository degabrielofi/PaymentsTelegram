import os
from pymongo import MongoClient
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client['DGzzIN Telegram']
pagamentos = db['pagamentos']

def salvar_pagamento(user_id, nome, plano, txid):
    dias = 7 if plano == 'semanal' else 30
    data_exp = datetime.utcnow() + timedelta(days=dias)
    pagamentos.insert_one({
        "user_id": user_id,
        "nome": nome,
        "plano": plano,
        "txid": txid,
        "expira_em": data_exp
    })

def verificar_expirados():
    expirados = pagamentos.find({"expira_em": {"$lt": datetime.utcnow()}})
    return list(expirados)

def remover_usuario(txid):
    pagamentos.delete_one({"txid": txid})