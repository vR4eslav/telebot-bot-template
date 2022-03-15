from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Token
ADMINS = list(map(int, env.list("ADMINS")))  # Admins
IP = env.str("IP")  # ip host
