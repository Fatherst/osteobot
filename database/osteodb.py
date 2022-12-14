from pymongo import MongoClient


def db_connect():
    global db
    cluster = 'mongodb+srv://Fatherst:fZi4u2u47CINseub@based.t7kunff.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(cluster)
    print(client.list_database_names())
    db = client.osteobot
    if db is not None:
        print('База данных успешно подключена')
    print(type(db))


def get_db():
    return db

# def db_add_question(state):
#    async with state.proxy() as data:
