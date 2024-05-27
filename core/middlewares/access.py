import os
import logging
import dotenv

from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message


dotenv.load_dotenv()


AUTHORIZED_USERS = [int(user) for user in os.getenv("USERS").split(",")]


class AccessMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:

        if event.from_user.id not in AUTHORIZED_USERS:
            logging.warning(
                f"Попытка входа неавторизованного пользователя: {event.from_user.id}"
            )
            return
        return await handler(event, data)
