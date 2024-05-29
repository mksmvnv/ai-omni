import os
import asyncio
import logging
import dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, error, generate
from middlewares.access import AccessMiddleware
from db.engine import init_db


dotenv.load_dotenv()


async def main() -> None:
    await init_db()

    bot = Bot(
        token=os.getenv("TG_TOKEN"),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)
    dp.include_routers(start.start_router, error.error_router, generate.generate_router)
    dp.message.middleware(AccessMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, polling_timeout=10)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
