from aiogram import Router
from aiogram.types import Message

from states.user import Generate


error_router = Router()


@error_router.message(Generate.text)
async def generate_error(message: Message) -> None:
    await message.answer(
        "Подождите, пока обрабатывается предыдущий запрос или нажмите /start чтобы начать сначала"
    )
