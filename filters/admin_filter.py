from telebot.custom_filters import SimpleCustomFilter

from data.config import ADMINS


class AdminFilter(SimpleCustomFilter):
    """
    Filter for admin users
    """

    key = 'admin'

    def check(self, message):
        if int(message.chat.id) in ADMINS:
            return True
