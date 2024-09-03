from aiogram.types import User, Chat

TEST_USER = User(
    id=1234, 
    is_bot=False, 
    first_name="Test", 
    last_name="User"
)

TEST_USER_CHAT = Chat(
    id=1234, 
    type="private", 
    first_name=TEST_USER.first_name, 
    last_name=TEST_USER.last_name)