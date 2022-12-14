from aiogram.utils import executor
from handlers import client, admin
from create_bot import dp
#import pymysql
#from database.config_db import host, db_name, user, password
#from pymysql import cursors
from database.osteodb import db_connect,get_db


###Экземпляр класса Bot создаётся в отдельном файле, так как если создавать в main, то работать не будет

async def on_startup(_):
    print('Бот в онлайне')
    db_connect()


###Запуск функций хендлера в мейне, без этого работать не будет
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
