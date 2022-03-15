from filters.admin_filter import AdminFilter


def setup_filters(bot):
    bot.add_custom_filter(AdminFilter())