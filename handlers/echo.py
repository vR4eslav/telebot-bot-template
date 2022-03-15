from telebot import types

from loader import bot


@bot.message_handler()
def start_handler(message: types.Message):
    bot.send_message(message.from_user.id,
                     f"Echo!\n\n"
                     f"<code>{message}</code>")
