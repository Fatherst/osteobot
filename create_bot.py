from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
API_TOKEN = '5920987375:AAElDAm_FW2GKg3ExCt1ZOjsOz2a_qX_7pI'
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)