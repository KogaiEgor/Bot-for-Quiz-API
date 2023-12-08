from aiogram import Bot, Dispatcher
from config_reader import config
import asyncio
from bot.handlers import user_handlers


async def main() -> None:
    token = config.token_api.get_secret_value()

    bot = Bot(token)
    dp = Dispatcher()
    dp.bot = bot

    dp.include_router(user_handlers.router)

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(_ex)

if __name__ == '__main__':
    asyncio.run(main())
