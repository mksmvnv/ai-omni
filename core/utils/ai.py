from openai import AsyncOpenAI

from utils.config import settings


client = AsyncOpenAI(api_key=settings.ai_token, base_url=settings.ai_base_url)


async def ai_omni(prompt: str) -> str:
    completion = await client.chat.completions.create(
        model="gpt-4o", max_tokens=500, messages=prompt
    )

    return completion.choices[0].message.content
