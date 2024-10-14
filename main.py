import asyncio
import logging

from aiogram import Bot, Dispatcher

from routers import router as main_router
from settings import settings


async def main():
    bot = Bot(token=settings.token)

    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
