from telebot import types

from loader import bot


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    bot.send_message(message.from_user.id,
                     f"Hello, {message.from_user.full_name}!")
