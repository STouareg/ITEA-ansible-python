import telebot
from tokens import * 
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = telegrambot
chat_id = adminchatid


bot = telebot.TeleBot(TOKEN)

#markup = types.ReplyKeyboardMarkup(True)
#itembtn1 = types.KeyboardButton('Start')
#itembtn2 = types.KeyboardButton('Stop')
#markup.row(itembtn1, itembtn2)
#markup.row('/logs','exit')
markup = InlineKeyboardMarkup()
markup.row_width = 2
markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))

hide_keyboard = {'hide_keyboard': True}


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(chat_id, 'Hello ITEA pwd:)')
    bot.send_message(chat_id, "Do you really wanna to see logs from Docker container MyApp? ", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
        bot.send_message(chat_id, "Ok, I will show you:")

    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")
        bot.send_message(chat_id, "Buy!")

bot.polling(none_stop=True)


