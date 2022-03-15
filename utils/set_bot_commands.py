from telebot import types


def set_default_commands(bot):
    bot.set_my_commands(commands=[types.BotCommand(command="start",
                                                   description="Run bot"),
                                  types.BotCommand(command="help",
                                                   description="Help text"),
                                  ])
