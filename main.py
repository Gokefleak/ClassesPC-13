import openpyxl
import telebot
import time
import datetime
from telebot import types
import io
import os
user_data = {}
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    if not (chat_id in user_data):
        user_data[chat_id] = {
            'message_id': 0,

        }
    markup = types.InlineKeyboardMarkup()
    buttonout1 = types.InlineKeyboardButton('Войти в аккаунт админестратора 🔐', callback_data='entrance')
    buttonout2 = types.InlineKeyboardButton('Рассписание', callback_data='timetable')
    buttonout3 = types.InlineKeyboardButton('Узнать свой ID 🔍', callback_data='myId')
    row1 = [buttonout1]
    row2 = [buttonout2]
    row3 = [buttonout3]
    markup.row(*row1)
    markup.row(*row2)
    markup.row(*row3)
    bot.send_message(chat_id=message.chat.id, text='Перед использованием авторизируйтесь', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'timetable')
def timetable(call):
    chat_id = call.message.chat.id
bot.polling()