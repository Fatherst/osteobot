import collections

import gridfs

from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.kb_client import get_thecure, get_osteodiagn, get_osteoncovid, get_startinline, get_osteoclass, \
    get_reasons_osteo, get_whatis_osteo, get_time, get_kazan, get_cities, get_ques_ans, get_book
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import osteodb
from pymongo import MongoClient, ReadPreference
from database.osteodb import db_connect, get_db
import datetime
from create_bot import PAYMENTS_TOKEN
from aiogram.types.message import ContentTypes
from aiogram.dispatcher.filters import Text

# Цена на запись
PRICE = [types.LabeledPrice(label='Запись', amount=19900)]


class FSMquestion(StatesGroup):
    ques = State()


class FSMfiles(StatesGroup):
    file = State()


async def start_command(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo="https://phonoteka.org/uploads/posts/2021-07/thumbs/1625641004_19-phonoteka-org-p-roza-v-ruke-art-krasivo-20.jpg",
                         caption='Приветствую! Я бот-помощник в борьбе с остеонекрозом.\n\nВозникли вопросы? Используй меню ниже👇',
                         reply_markup=get_startinline())


async def whatis(callback: types.CallbackQuery):
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/e096cbd0-d80e-4e13-88a6-a755f76c0c67/12bf3461cb030daec2e702c220eb0e.jpg",
                         caption='Асептический некроз кости (остеонекроз или ОН) — это тяжелое многофакторное заболевание, в механизме развития которого выделяют сосудистые нарушения и снижение минеральной плотности кости в результате чего происходит гибель костных клеток(остеоцитов), быстро приводящее к разрушению прилежащего сустава.\nНаиболее частой локализацией является головка бедренной кости, на втором месте по распространению находятся кости образующие коленный сустав, реже головка плечевой кости, таранная кость и т.д.\nВыраженность клинических проявлений зависит от локализации, размера, а также сопутствующий повреждений. Пациенты чаще всего жалуются на боль, ограничение движений в суставе. *Однако начальные заболевания могут протекать бессимптомно!*',
                         reply_markup=get_whatis_osteo())


async def reasons(callback: types.CallbackQuery):
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/1e2e1a70-ddfc-4778-a742-282383bac049/priciny-ostnekr.png",
                         caption='Клинически выделяют:- первичный ( или идиопатический) ОН, то есть без явной причины\n- и вторичный ОН, ассоциированный с заболеванием или состоянием, повлекшее развитие ОН ( алкоголизм, табакокурение, гормонотерапия (особенно в результате перенесенного в тяжелой форме COVID-19) и т.д.\nЕсли причины и механизм развития вторичного ОН известны, то этиопатогенез (из-за чего?и почему?) первичного ОН долгое время остается предметом дискуссий.\n Однако исследователи пришли в выводу, что идиопатический (первичный)ОН заболевание полиэтиологическое(многофакторное) в механизме которого выделяют:\n- Сосудистые нарушения(микротромбообразование)\n- Микропереломы, остеопоротической(хрупкой) кости, вследствие чего происходит сдавление питающих сосудов\n- Сосудистый стаз ( застой)',
                         reply_markup=get_reasons_osteo())


async def diagnosis(callback: types.CallbackQuery):
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/0dfd622f-efdf-47af-afc6-fc125fa1df09/rentgen-on.jpg",
                         caption='Рентгенография неэффективна для выявления ранней стадии асептического некроза. На стандартной рентгенографии визуализация патологии возможна на поздний стадиях.\nПри локализации зоны асептического некроза в субхондральной зоне 3 и 4 стадии проявляются наличием деформации суставной поверхности сустава,')
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/d8507111-2cc8-4ad6-9ed6-2789fb6fe4f7/mrt-on.png",
                         caption='Начальные стадии асептического некроза костей могут быть выявлены только при МРТ исследовании.\nВ связи с чем, пациентам с длительными болями в крупных суставах конечностей, при "нормальной" рентген картине, рекомендовано выполнение МРТ-исследования')
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/a0bcfbcb-aae4-4a86-a936-99f5a105d117/kt-on.png",
                         caption='В свою очередь КТ- исследование( компьютерная томография) позволяет дифференцировать стадии остеонекроза:\n- предколлапсная (3А по ARCO), когда не произошло перелома кортикальной пластинки и возможна органосохраняющая тактика лечения\n- постколлапсная ( 3В по ARCO), когда произошла импрессия пораженного участка кости и показана артропластика( эндопротезирование) пораженного  сустава',
                         reply_markup=get_osteodiagn())


async def thecure(callback: types.CallbackQuery):
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/711795dd-b86b-43d1-bc30-e050a26c22e3/tep-tbs-on.jpg",
                         caption='При поздних стадиях ( 3-4 ст. по ARCO) предпочтение отдается_ тотальному эндопротезированию (замене) сустава._ Такое лечение дает хорошие среднесрочные результаты(10-15 лет), однако потребность в ревизионном эндопротезировании вынуждает искать  эффективные методы лечения у пациентов молодого возраста. В эпоху COVID-19, когда наблюдается рост заболеваемости остеонекрозом, очень важно выявлять ОН на ранних стадиях, когда *органосберегающее лечение *может дать положительный результат.')
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/3d6a1681-e07f-4820-880a-06798c87dd01/tunelizaciya-on.png",
                         caption='На стадии* 1 и 2 по ARCO *для снижения болевого синдрома и улучшения кровоснабжения возможно применение тунелизации (декомпрессии) очага пораженного участка кости, которая проводится после ранее назначенной консервативной терапии.Для усиления эффекта тунелизации очага асептического некроза рекомендуется ее сочетание не только с ранее назначенной консервативной терапией, но и с введением биологических субстанций, обладающих стимулирующим действием (PRP-терапия, стромально-васкулярная фракция и т.д.).')
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/99e9c061-78e0-432f-9d47-9e8996cd7d38/konserva-on.png",
                         caption='Тактика лечения остеонекроза зависит от стадии заболевания. Современное понимание механизмов, вызывающий остеонекроз, определяет необходимость комплексного воздействия на различные звенья патогенеза: нарушение микроциркуляции, сосудистый стаз, повышенная локальная резорбция кости.\nУчитывая многофакторность развития заболевания, монотерапия считается менее эффективной, поэтому лечение должно включать в себя не только обезболивание и разгрузку прилежащего сустава.\nКонсервативное лечение проводится пациентам с ранними формами остеонекроза (1-2 ст. по ARCO).\n Состоит из:\n- Соблюдение ортопедического режима\n- Сосудистая терапия/коррекция липидного спектра\n- Сочетание остеотропной и антирезорбтивной терапии\n- Симптоматическое лечение ( НПВС + физиотерапия)',
                         reply_markup=get_thecure())


async def classific(callback: types.CallbackQuery):
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/734561d2-6568-452e-a4df-585c646be87a/klassifikaciya-on.png",
                         reply_markup=get_osteoclass())


async def osteoncovid(callback: types.CallbackQuery):
    await bot.send_photo(callback.message.chat.id,
                         photo="https://eva.botsister.ru/fee7ccef-baba-4bc8-b262-7873c5053339/on-i-kovid.png",
                         reply_markup=get_osteoncovid())


async def mainmenu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://eva.botsister.ru/9bc8473e-e6a6-46e8-bb90-290ee1d97e0d/roza.jpg",
                         caption='Приветствую! Я бот-помощник в борьбе с остеонекрозом.\n\nВозникли вопросы? Используй меню ниже👇',
                         reply_markup=get_startinline())


async def city(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='В каком городе вы находитесь?', reply_markup=get_cities())


async def ochline(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Так как вы из Казани, то вам доступен и очный, и онлайн приём к врачу.\nКак бы вы хотели записаться?',
                           reply_markup=get_kazan())


async def online(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Так как вы не из Казани, то вам доступна запись на онлайн приём к врачу - https://osteopat.bookafy.com/service/-67ae?locale=en')


async def book(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Записаться можно здесь -https://osteopat.bookafy.com/service/-67ae?locale=en')


async def ochno(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='https://osteopat.bookafy.com/service/-f454?locale=en')


async def pre_diary(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Здесь вы можете прислать доктору файлы о своей проблеме(ренгтены, фото и т.д.).\n Нажимая на кнопку и отправляя файлы, вы даёте своё согласие на обработку персональных данных',
                           reply_markup=get_book())


async def diary_fsm(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Пожалуйста, пришлите файлы по одному\nДля выхода из режима загрузки файлов напишите "Отмена"')
    await FSMfiles.file.set()


async def diary_confirmed(message: types.Message, state: FSMContext):
    if message.content_type == 'document' and message.text != 'отмена':
        async with state.proxy() as data:
            data['file'] = message.document.file_id
            data['username'] = message.from_user.username
            photos = osteodb.get_db().user_files
            file = {"username": f"{data['username']}",
                    "file_id": f"{data['file']}",
                    "date": f"{datetime.datetime.now()}"
                    }
            photos.insert_one(file)
        await state.finish()
        await message.reply('Спасибо',reply_markup=get_startinline())
    elif message.text == Text(equals='Отмена', ignore_case=True):
        await state.finish()
        await message.reply('Отмена')
    elif message.content_type != 'document':
        await message.reply('Пришлите вопрос в формате файла, пожалуйста')


async def question(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Здесь вы можете задать интересующий вас вопрос врачу и он на него ответит.\nДля выхода из режима вопросов напишите "Отмена"')
    await FSMquestion.ques.set()


async def asked_ques(message: types.Message, state: FSMContext):
    if message.content_type == 'text' and message.text != 'отмена':
        async with state.proxy() as data:
            data['question'] = message.text
            data['username'] = message.from_user.username
            # Получение из базы данных коллекции с именем questions, при помощи функции get_db
            queses = osteodb.get_db().questions
            print(queses)
            que = {"username": f"{message.from_user.username}",
                   "question": f"{message.text}",
                   "date": f"{datetime.datetime.now()}"
                   }
            queses.insert_one(que)
        await state.finish()
        await message.reply('Ваш вопрос записан, врач ответит вам на него в ближайшее время',
                            reply_markup=get_ques_ans())
    elif message.text == Text(equals='Отмена', ignore_case=True):
        await state.finish()
        await message.reply('Отмена')
    elif message.content_type != 'document':
        await message.reply('Вы должны прислать вопрос текстом')


async def book_buy(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Первичный приём у врача стоит 199 рублей')
    await bot.send_invoice(callback.from_user.id, title='Приём у врача',
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           prices=PRICE,
                           description='Первичный приём производится через бота, в дальнейшем общение с врачом происходит лично',
                           payload='booking')


async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def got_payment(message: types.Message):
    await bot.send_message(message.chat.id, text=f'Оплата успешно выполнена, из какого вы города?',
                           reply_markup=get_cities())
    # f'{message.successful_payment.total_amount/100}{message.successful_payment.currency}')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отмена')


# 1 - Что такое остеонекроз
# 2 - Причины развития
# 3 - Как его диагностировать
# 4 - Как его лечить
# 5 - Классификация остеонекроза
# 6 - Остеонекроз и ковид
# 7 - Главное меню
# 8 - Задать вопрос
# 9 - Запись на приём
# 10 - Дневник болезн

# Чтобы сделать mainmenu - два хендлера, либо отдельная функция(не оч), либо кнопка отсылает команду старт
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(whatis, text='1')
    dp.register_callback_query_handler(reasons, text='2')
    dp.register_callback_query_handler(diagnosis, text='3')
    dp.register_callback_query_handler(thecure, text='4')
    dp.register_callback_query_handler(classific, text='5')
    dp.register_callback_query_handler(osteoncovid, text='6')
    dp.register_callback_query_handler(mainmenu, text='7')
    dp.register_callback_query_handler(question, text='8', state=None)
    # dp.register_callback_query_handler(city, text='9')
    dp.register_callback_query_handler(ochline, text='11')
    dp.register_callback_query_handler(online, text='12')
    dp.register_callback_query_handler(book, text='13')
    dp.register_message_handler(asked_ques, content_types=['document', 'photo', 'text'], state=FSMquestion)
    dp.register_callback_query_handler(mainmenu, text='ok')
    dp.register_callback_query_handler(book_buy, text='9')
    dp.register_pre_checkout_query_handler(checkout, lambda query: True)
    dp.register_message_handler(got_payment, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_callback_query_handler(ochno, text='14')
    dp.register_message_handler(diary_confirmed, content_types=['document', 'photo', 'text'], state=FSMfiles)
    dp.register_callback_query_handler(pre_diary, text='10')
    dp.register_callback_query_handler(diary_fsm, text='yes', state=None)
    dp.register_message_handler(cancel_fsm, state='*', commands='Отмена')
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")
