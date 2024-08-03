from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.ai import ai_omni
from states.user import Generate
from db.counter import add_tokens


generate_router = Router()


@generate_router.message(F.text)
async def generate(message: Message, state: FSMContext) -> None:
    processing = await message.answer("Обработка запроса...")

    await state.set_state(Generate.text)

    data = await state.get_data()

    prompt = data.get("prompt", [])
    prompt.append({"role": "user", "content": message.text})

    completion = await ai_omni(prompt)
    prompt.append({"role": "assistant", "content": completion})

    user_tokens = len(message.text)
    ai_tokens = len(completion)

    await add_tokens(
        message.from_user.id, message.from_user.username, user_tokens, ai_tokens
    )

    await state.update_data(prompt)

    try:
        await message.answer(completion)
    finally:
        await processing.delete()

    await state.set_state(None)
