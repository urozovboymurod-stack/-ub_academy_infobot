import os
import telebot
from flask import Flask

# Flask veb serverini yaratamiz (Render tekin rejasida bot o'chib qolmasligi uchun kerak)
app = Flask(__name__)

# GitHub Secrets-ga qo'ygan tokenimizni o'qib olamiz
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def home():
    return "UB Academy Bot is Running!"

# Bot foydalanuvchi /start bosganda javob beradi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! UB ACADEMY infobotiga xush kelibsiz!")

# Botga kelgan har qanday matnga javob berish
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}\nTez orada administratorimiz bog'lanadi.")

if __name__ == "__main__":
    # Botni alohida tarmoqda ishga tushiramiz
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Veb serverni Render uchun kerakli portda yoqamiz
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
