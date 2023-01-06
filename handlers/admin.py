from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import osteodb
from pymongo import MongoClient, ReadPreference
from keyboards.kb_admin import get_questions_kb, get_to_mm, get_ok
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text


class FSMusers(StatesGroup):
    username = State()


async def admin_start(message: types.Message):
    admin_username = ['Blexeich', 'Osteodoc23', 'sergpreneur']
    if message.from_user.username in admin_username:
        await bot.send_message(message.from_user.id, text='Вы зашли в админ-панель, показать вопросы пациентов?',
                               reply_markup=get_questions_kb())
    else:
        await bot.send_message(message.from_user.id, text='Вы не админ')


### Сделать сортировку по имени пользователя, кнопки по имени пользователя

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
    await bot.send_message(callback.from_user.id, text='Это все вопросы, вернуться в главное меню?',
                           reply_markup=get_to_mm())


async def list_files(callback: types.CallbackQuery):
    files = osteodb.get_db().user_files
    for i in files.find():
        file_user = i['file_id']
        file_username = i['username']
        file_date = i['date']
        await bot.send_document(callback.from_user.id, document=f'{file_user}',
                                caption=f'@{file_username}\nВремя отправки файла:{file_date}', )
    await bot.send_message(callback.from_user.id,
                           text='Вы можете найти все файлы для одного пациента по его юзернейму, для этого сначала нажмите на кнопку',
                           reply_markup=get_ok())


async def main_menu(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Вы зашли в админ-панель, показать вопросы пациентов?',
                           reply_markup=get_questions_kb())


async def sort(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Напишите ник пациента(без знака @), чтобы получить только его файлы')
    await FSMusers.username.set()


async def get_files(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
        photos = osteodb.get_db().user_files
        for i in photos.find({"username": f"{data['username']}"}):
            await bot.send_document(message.from_user.id, document=f'{i["file_id"]}',
                                    caption=f'@{i["username"]}\n'
                                            f'Время отправки файла: {i["date"]}')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отмена')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])
    dp.register_callback_query_handler(list_questions, text='look')
    dp.register_callback_query_handler(main_menu, text='40')
    dp.register_callback_query_handler(list_files, text='files')
    dp.register_callback_query_handler(sort, text='find', state=None)
    dp.register_message_handler(get_files, content_types=['text'], state=FSMusers)
    dp.register_message_handler(cancel_fsm, state='*', commands='Отмена')
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',ignore_case=True), state="*")
