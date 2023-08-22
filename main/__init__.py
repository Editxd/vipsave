#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22825629
API_HASH = "e8db542482a1638b4e5b03ed1ddae521"
BOT_TOKEN = "6180255742:AAGSbz5JTRk7FEA_QAHCYvOcdo3N-C_Yk2A"
FORCESUB = -1001743550303
ACCESS = int("-1001688331719")
MONGODB_URI = "mongodb+srv://projeklisatiga:Malik10_@cluster0.tgthj.mongodb.net/?retryWrites=true&w=majority"
AUTH_USERS =  6404342282

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
