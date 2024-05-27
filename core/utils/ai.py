import os
import dotenv

from openai import AsyncOpenAI


dotenv.load_dotenv()


client = AsyncOpenAI(api_key=os.getenv("AI_TOKEN"), base_url=os.getenv("AI_BASE_URL"))


async def ai_omni(prompt: str) -> str:
    completion = await client.chat.completions.create(model="gpt-4o", messages=prompt)

    return completion.choices[0].message.content
