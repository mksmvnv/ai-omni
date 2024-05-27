from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.ai import ai_omni
from states.user import Generate


generate_router = Router()


@generate_router.message(F.text)
async def generate(message: Message, state: FSMContext) -> None:
    processing = await message.answer("Обрабатка запроса...")

    await state.set_state(Generate.text)

    data = await state.get_data()

    prompt = data.get("prompt", [])

    prompt.append({"role": "user", "content": message.text})

    completion = await ai_omni(prompt)

    prompt.append({"role": "assistant", "content": completion})

    await state.update_data(prompt)

    try:
        await message.answer(completion)
    finally:
        await processing.delete()

    await state.set_state(None)
