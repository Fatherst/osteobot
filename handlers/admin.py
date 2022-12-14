from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import osteodb
from pymongo import MongoClient, ReadPreference
from keyboards.kb_admin import get_questions_kb, get_to_mm


async def admin_start(message: types.Message):
    admin_username = 'Blexeich'
    if message.from_user.username == admin_username:
        await bot.send_message(message.from_user.id, text='Вы зашли в админ-панель, показать вопросы пациентов?',
                               reply_markup=get_questions_kb())
    else:
        await bot.send_message(message.from_user.id, text='Вы не админ')


async def list_questions(callback: types.CallbackQuery):
    questions = osteodb.get_db().questions
    # print(questions.find_one({"username":"Blexeich"}))
    for i in questions.find():
        username = i['username']
        quest = i['question']
        date = i['date']
        print(i)
        await bot.send_message(callback.from_user.id, text=f'Задал вопрос:@{username}\n'
                                                           f'{quest}\n'
                                                           f'Когда был задан вопрос:{date}')
    await bot.send_message(callback.from_user.id,text='Это все вопросы, вернуться в главное меню?',
                           reply_markup=get_to_mm())


async def main_menu(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Вы зашли в админ-панель, показать вопросы пациентов?',
                           reply_markup=get_questions_kb())


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])
    dp.register_callback_query_handler(list_questions, text='look')
    dp.register_callback_query_handler(main_menu, text='40')
