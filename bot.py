import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

if not API_TOKEN:
    raise ValueError("Bot API token not set in .env file.")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Calculate Arithmetic Progression')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Hello, I can calculate arithmetic progressions. What do you want to do?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Calculate Arithmetic Progression')
def calculate_progression(message):
    bot.send_message(message.chat.id, "Please provide the first term (a1), the common difference (d), and the number of terms (n) separated by commas (e.g., 5, 2, 10).")
    bot.register_next_step_handler(message, process_input)

def process_input(message):
    try:
        # Split the input by commas and convert to float/int
        a1, d, n = map(float, message.text.split(','))
    except:
        bot.send_message(message.chat.id, "Invalid input. Please enter three numbers separated by commas (e.g., 5, 2, 10).")
        bot.register_next_step_handler(message, process_input)
        return

    result = ", ".join(str(a1 + i * d) for i in range(int(n)))
    bot.send_message(message.chat.id, f"The arithmetic progression is: {result}")

bot.polling()