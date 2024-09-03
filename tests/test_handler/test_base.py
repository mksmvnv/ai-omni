import pytest
from unittest.mock import AsyncMock
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from utils import TEST_USER, TEST_USER_CHAT
from core.handlers.start import command_start

@pytest.mark.asyncio
async def test_command_start():
    message = AsyncMock()

    message.from_user = TEST_USER
    message.chat = TEST_USER_CHAT

    storage = MemoryStorage()

    storage_key = (message.chat.id, message.from_user.id)
    
    await storage.set_data(storage_key, {})

    state = FSMContext(storage=storage, key=storage_key)

    await command_start(message=message, state=state)

    message.answer.assert_called_with("Авторизация прошла успешно! Какой у вас вопрос?")
    
    data = await storage.get_data(storage_key)
    assert data == {'prompt': []}