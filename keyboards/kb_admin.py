from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton


def get_questions_kb():
    beka = InlineKeyboardMarkup(row_width=1)
    b = InlineKeyboardButton('Смотреть вопросы пациентов', callback_data='look')
    b1 = InlineKeyboardButton('Смотреть документы пациентов', callback_data='files')
    beka.add(b).add(b1)
    return beka


def get_to_mm():
    mm = InlineKeyboardMarkup(row_width=1)
    b = InlineKeyboardButton('Вернуться в меню админа', callback_data='40')
    mm.add(b)
    return mm


def get_ok():
    bub = InlineKeyboardMarkup(row_width=1)
    b = InlineKeyboardButton('Найти', callback_data='find')
    bub.add(b)
    return bub
