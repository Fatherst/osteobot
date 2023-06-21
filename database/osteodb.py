from pymongo import MongoClient
import gridfs


def db_connect():
    global db, fs
    cluster = 'URI'
    client = MongoClient(cluster)
    print(client.list_database_names())
    db = client.osteobot
    if db is not None:
        print('База данных успешно подключена')
    print(type(db))


### gridfs - нужен для хранения файлов
def get_db():
    return db



# def db_add_question(state):
#    async with state.proxy() as data:
