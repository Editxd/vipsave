#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
FORCESUB = config("FORCESUB", default=None)
ACCESS = int("-1001688331719")
MONGODB_URI = "mongodb+srv://projeklisatiga:Malik10_@cluster0.tgthj.mongodb.net/?retryWrites=true&w=majority"
AUTH_USERS = config("AUTH", default=None)
SUDO_USERS = []
if len(AUTH_USERS != 0:
    SUDO_USERS = {int(AUTH_USERS.strip()) for AUTH_USERS in AUTH_USERS.split()}
else:
    SUDO_USERS = set()
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
