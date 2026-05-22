import os
import telebot
from flask import Flask
from threading import Thread
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

app = Flask('')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بيك! البوت شغال 24/7 🔥")

@app.route('/')
def home():
    return "البوت شغّال.."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    print("البوت شغّال..")
    keep_alive()
    bot.polling(none_stop=True)