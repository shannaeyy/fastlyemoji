from flask import Flask, request
import os
import telegram

TOKEN = "8473212500:AAEgo9Zz85zItQXwX8rKUslhm1ZqeQJ42iM"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running"

@app.route(f'/{TOKEN}', methods=['POST'])
def receive_update():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Basic reply
    bot.send_message(chat_id=chat_id, text=f"You said: {text}")
    return "ok"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}"
    bot.setWebhook(webhook_url)
    app.run(host='0.0.0.0', port=port)
