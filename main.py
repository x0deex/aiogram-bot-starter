import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from app.handlers import router
from app.database.models import async_main

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.include_router(router)
    await dp.start_polling(bot)

async def on_startup(dispatcher):
    await async_main()

if __name__ == "__main__":
    try:
        print("Starting up...")
        asyncio.run(main())
    except:
        print("EXIT")