from loguru import logger

from data.config import ADMINS


def on_startup_notify(bot):
    logger.info("Оповещение администрации...")
    for admin in ADMINS:
        try:
            bot.send_message(
                admin, "Бот был успешно запущен"
            )
        except Exception as err:
            logger.error(err)
            logger.debug("Чат с админом не найден")
