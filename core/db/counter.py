from db.models import Calculate
from db.engine import session_marker


async def add_tokens(
    user_id: int, user_name: str, user_tokens: int, ai_tokens: int
) -> None:
    async with session_marker() as session:
        async with session.begin():
            new_log = Calculate(
                user_id=user_id,
                user_name=user_name,
                user_tokens=user_tokens,
                ai_tokens=ai_tokens,
            )
            session.add(new_log)

            await session.commit()
