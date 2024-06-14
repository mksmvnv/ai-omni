from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


start_router = Router()


@start_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer("Авторизация прошла успешно! Какой у вас вопрос?")
    await state.update_data(prompt=[])
