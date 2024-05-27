import os
import asyncio
import logging
import dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import start, generate, error
from middlewares.access import AccessMiddleware


dotenv.load_dotenv()


async def main() -> None:
    bot = Bot(
        token=os.getenv("TG_TOKEN"),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )

    dp = Dispatcher()
    dp.include_routers(start.start_router, generate.generate_router, error.error_router)
    dp.message.middleware(AccessMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, polling_timeout=10)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
