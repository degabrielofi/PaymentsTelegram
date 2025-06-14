# 🤖 Telegram Pix Bot

Este projeto é um bot para Telegram com integração à [BullsPay](https://bullspay.com.br), que automatiza:

- Geração de cobranças via Pix (QR Code + Copia e Cola)
- Verificação automática de pagamento via webhook
- Envio de link de acesso a grupo no Telegram
- Controle de planos (Semanal e Mensal)
- Remoção automática de usuários com plano expirado
- Armazenamento em banco de dados MongoDB

## 📦 Estrutura do Projeto

```

telegram-pix-bot/
├── bot.py # Inicia o bot do Telegram e gera pagamentos
├── webhook.py # Recebe notificações da BullsPay
├── database.py # Controle de pagamentos com MongoDB
├── remover_expirados.py # Script para limpar acessos vencidos
├── requirements.txt # Dependências do projeto
├── Procfile # Arquivo para deploy no Render
├── .env # (NÃO SUBIR) Variáveis secretas

```

---

## 🚀 Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/degabrielofi/PaymentsTelegram.git
cd PaymentsTelegram
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Crie o arquivo `.env`

Crie um arquivo chamado `.env` e preencha com suas credenciais:

```
TELEGRAM_TOKEN=SEU_TOKEN_DO_BOT
SECRET_KEY_BULL=SUA_SECRET_KEY_DA_BULLSPAY
MONGO_URL=SUA_STRING_DE_CONEXAO_MONGODB
GRUPO_ID=-1001234567890
```

> **⚠️ Nunca suba este arquivo para o GitHub.**

---

## 🧠 Como funciona

- O usuário acessa o bot e escolhe um plano (Semanal ou Mensal).
- O bot gera uma cobrança via Pix usando a API da BullsPay.
- A BullsPay envia a confirmação de pagamento via webhook.
- O bot envia automaticamente o link para entrar no grupo privado do Telegram.
- Um script (remover_expirados.py) pode ser executado periodicamente para remover usuários cujo plano venceu.

---

## 🌐 Deploy (opcional)

Você pode hospedar o `webhook.py` gratuitamente no [Render](https://render.com):

1. Crie um repositório no GitHub com este projeto.
2. Acesse o Render > New Web Service > Connect repositório.
3. Configure a URL pública que será usada como Webhook (ex: `https://seubot.onrender.com/webhook`)
4. Cadastre essa URL no painel da BullsPay em **Configurações > Webhook**.

---

## ✅ Checklist

- [x] Integração Pix via API BullsPay
- [x] Armazenamento no MongoDB
- [x] Webhook para pagamento confirmado
- [x] Bot envia link do grupo automaticamente
- [x] Remoção automática por expiração

---

## 🛡️ Segurança

- Tokens e dados sensíveis são carregados via `.env`.
- O arquivo `.gitignore` está configurado para ignorar o `.env` por segurança.

---

## 🤝 Contribuições

Pull requests são bem-vindos. Para mudanças significativas, abra uma issue primeiro.

---
