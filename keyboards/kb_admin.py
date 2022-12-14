from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton


def get_questions_kb():
    beka = InlineKeyboardMarkup(row_width=1)
    b = InlineKeyboardButton('Смотреть вопросы пациентов', callback_data='look')
    beka.add(b)
    return beka


def get_to_mm():
    mm = InlineKeyboardMarkup(row_width=1)
    b = InlineKeyboardButton('Вернуться в меню админа', callback_data='40')
    mm.add(b)
    return mm
