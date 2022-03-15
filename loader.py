from telebot import TeleBot

from data import config

bot: TeleBot = TeleBot(config.BOT_TOKEN, num_threads=5, parse_mode="html")
