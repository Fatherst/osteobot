from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton


# 1 - Что такое остеонекроз
# 2 - Причины развития
# 3 - Как его диагностировать
# 4 - Как его лечить
# 5 - Классификация остеонекроза
# 6 - Остеонекроз и ковид
# 7 - Главное меню
# 8 - Задать вопрос
# 9 - Запись на приём
# 10 - Дневник болезни
# 11 - Казань
# 12 - Другой город
# 13 - Онлайн приём
# 14 - Очная запись
# 15 -
# 16 -

def get_startinline():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Что такое остеонекроз?', callback_data='1')
    b2 = InlineKeyboardButton('Причины развития остеонекроза', callback_data='2')
    b3 = InlineKeyboardButton('Как его диагностировать?', callback_data='3')
    b4 = InlineKeyboardButton('Как его лечить?', callback_data='4')
    b5 = InlineKeyboardButton('Задать вопрос', callback_data='8')
    b7 = InlineKeyboardButton('Дневник болезни', callback_data='10')
    start_inline.row(b1, b2).row(b3, b4).add(b5).add(b7)
    return start_inline


def get_whatis_osteo():
    osteo = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Причины развития остеонекроза', callback_data='2')
    b2 = InlineKeyboardButton('Как его диагностировать', callback_data='3')
    b3 = InlineKeyboardButton('Классификация остеонекроза', callback_data='5')
    b4 = InlineKeyboardButton('Как его лечить?', callback_data='4')
    b5 = InlineKeyboardButton('Главное меню', callback_data='7')
    osteo.row(b1).add(b2).add(b3).add(b4).add(b5)
    return osteo


def get_reasons_osteo():
    reasons = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Остеонекроз и COVID-19', callback_data='6')
    b2 = InlineKeyboardButton('Как его диагностировать?', callback_data='3')
    b3 = InlineKeyboardButton('Классификация ОН', callback_data='5')
    b4 = InlineKeyboardButton('Как его лечить?', callback_data='4')
    b5 = InlineKeyboardButton('Главное меню', callback_data='7')
    reasons.add(b1).add(b2).add(b3).add(b4).add(b5)
    return reasons


def get_osteoncovid():
    ostvid = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Как диагностировать остеонекроз?', callback_data='3')
    b2 = InlineKeyboardButton('Классификация остеонекроза', callback_data='5')
    b3 = InlineKeyboardButton('Как лечить остеонекроз?', callback_data='4')
    b4 = InlineKeyboardButton('Главное меню', callback_data='7')
    ostvid.add(b1).add(b2).add(b3).add(b4)
    return ostvid


def get_osteoclass():
    ostclass = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Причины развития остеонекроза', callback_data='2')
    b2 = InlineKeyboardButton('Как диагностировать остеонекроз?', callback_data='3')
    b3 = InlineKeyboardButton('Как лечить остеонекроз?', callback_data='4')
    b4 = InlineKeyboardButton('Главное меню', callback_data='7')
    ostclass.add(b1).add(b2).add(b3).add(b4)
    return ostclass


def get_osteodiagn():
    ostdiagn = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Причины развития остеонекроза', callback_data='2')
    b2 = InlineKeyboardButton('Классификация остеонекроза', callback_data='5')
    b3 = InlineKeyboardButton('Как лечить остеонекроз?', callback_data='4')
    b4 = InlineKeyboardButton('Главное меню', callback_data='7')
    ostdiagn.add(b1).add(b2).add(b3).add(b4)
    return ostdiagn


def get_thecure():
    ostcure = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Причины развития остеонекроза', callback_data='2')
    b2 = InlineKeyboardButton('Классификация остеонекроза', callback_data='5')
    b3 = InlineKeyboardButton('Как диагностировать остеонекроз?', callback_data='3')
    b4 = InlineKeyboardButton('Главное меню', callback_data='7')
    ostcure.add(b1).add(b2).add(b3).add(b4)
    return ostcure


def get_cities():
    cities = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Я в Казани', callback_data='11')
    b2 = InlineKeyboardButton('Я из другого города', callback_data='12')
    cities.add(b1).add(b2)
    return cities


def get_kazan():
    types = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Запись на онлайн приём к врачу', callback_data='13')
    b2 = InlineKeyboardButton('Запись на очный приём к врачу', callback_data='14')
    types.add(b1).add(b2)
    return types


def get_time():
    time = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('19:00', callback_data='19')
    b2 = InlineKeyboardButton('19:15', callback_data='1915')
    b3 = InlineKeyboardButton('19:30', callback_data='1930')
    b4 = InlineKeyboardButton('19:45', callback_data='1945')
    time.add(b1).add(b2).add(b3).add(b4)
    return time


def get_ques_ans():
    ans = InlineKeyboardMarkup(row_width=1)
    b = InlineKeyboardButton('Хорошо', callback_data='ok')
    ans.add(b)
    return ans


def get_book():
    book = InlineKeyboardMarkup(row_width=1)
    yes = InlineKeyboardButton('Согласен', callback_data='yes')
    no = InlineKeyboardButton('Не согласен', callback_data='7')
    book.add(yes).add(no)
    return book
