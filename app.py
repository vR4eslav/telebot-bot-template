import logging

from loguru import logger

from loader import bot
from utils.notify_admins import on_startup_notify

from utils.set_bot_commands import set_default_commands
import middlewares
import handlers
import filters
filters.setup_filters(bot)


def run():
    bot.infinity_polling()


def start_bot():
    logger.debug("Starting...")
    logger.debug("Bot started!")
    run()
    set_default_commands(bot)
    on_startup_notify(bot)


if __name__ == "__main__":
    start_bot()



