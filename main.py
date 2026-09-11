import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.handlers import router

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Starting up...")
        asyncio.run(main())
    except:
        print("EXIT")