from aiogram import types, Router, F
from aiogram.filters import Command

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
        input_field_placeholder="Выберите способ подачи"
    )
    await msg.answer(
        text='Вы хотите создавать тесты или пройти тест?',
        reply_markup=keyboard
    )


