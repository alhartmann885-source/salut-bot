import telebot
import os
from threading import Thread
from flask import Flask

# 1. Создаем мини-сайт для Render (чтобы он не ругался на порты)
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    # Render любит порт 8080
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Настройка твоего бота
API_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🎆 Салют судеб запущен через бесплатный сервер! Напиши /catch.")

# Если у тебя были свои предсказания, вставь их ниже...
@bot.message_handler(commands=['catch'])
def catch(message):
    bot.send_message(message.chat.id, "✨ Твое предсказание: Сегодня удачный день для магии!")

if __name__ == "__main__":
    keep_alive() # Запускаем "сайт" для обхода ошибки
    print("Бот запущен!")
    bot.infinity_polling()
