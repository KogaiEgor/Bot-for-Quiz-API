from aiogram import types, Router, F
from aiogram.filters import Command
from bot.utils.call_api import *


router = Router()

@router.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Создавать тесты")],
        [types.KeyboardButton(text="Пройти тест")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await msg.answer(
        text='Вы хотите создавать тесты или пройти тест?',
        reply_markup=keyboard
    )


@router.message(F.text.lower() == "создавать тесты")
async def creator(msg: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Загрузить тест")],
        [types.KeyboardButton(text="Посмотреть список тестов")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    user_id = msg.from_user.id
    username = msg.from_user.username
    data = await call_creator(user_id, username)
    await msg.answer(
        text=str(data),
        reply_markup=keyboard
    )


@router.message(F.text.lower() == "посмотреть список тестов")
async def get_quiz_list(msg: types.Message) -> None:
    await msg.answer(
        text='Список тестов',
    )


@router.message(F.text.lower() == "загрузить тест")
async def send_quiz(msg: types.Message) -> None:
    await msg.answer(
        text='Загрузите тест в формате .docx',
    )


@router.message()
async def handle_uploaded_file(msg: types.File):
    bot = msg.bot
    file = await bot.get_file(file_id=msg.document.file_id)
    file_path = file.file_path
    success = await upload_quiz(telegram_id=msg.from_user.id, file_path=file_path)


    if success:
        await msg.answer("Файл успешно загружен")
    else:
        await msg.answer("Что-то пошло не так. Файл не был загружен")


