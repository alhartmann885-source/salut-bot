import telebot
import os

# ВАЖНО: Эта строчка говорит боту взять токен из настроек Render
API_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🎆 Салют судеб запущен! Я готов предсказывать будущее Академии.")

# Твой остальной код...

if __name__ == "__main__":
    bot.infinity_polling()
