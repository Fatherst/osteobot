from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
API_TOKEN = '5920987375:AAGS-HATq_PCXowI9beWBNKfmT6JMq9r6Ns'
PAYMENTS_TOKEN = '381764678:TEST:46673'
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)