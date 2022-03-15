from telebot import types

from loader import bot


@bot.message_handler(commands=['help'])
def start_handler(message: types.Message):
    bot.send_message(message.from_user.id,
                     f"Commands: \n\n"
                     f"/start - Start\n"
                     f"/help - Help\n")
