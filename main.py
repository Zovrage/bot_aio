import logging
import asyncio

from aiogram import Bot, Dispatcher
from config.config import TOKEN
from handlers.user_handler import router



async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
    except Exception as ex:
        print(f'Ошибка: {ex}')