#pip install pyTelegramBotAPI
import telebot
import time

bot_token = '1336436573:AAFpaGsPLEc90A9LBObk6kSXDvjrySmQH14'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')

#bot.polling()

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
