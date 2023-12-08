import asyncio
import os

from mimstralai.async_client import MistralAsyncClient
from mimstralai.models.chat_completion import ChatMessage


async def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-tiny"

    client = MistralAsyncClient(api_key=api_key)

    async for chunk in client.chat_stream(
        model=model,
        messages=[ChatMessage(role="user", content="What is the best French cheese?")],
    ):
        print(chunk)


if __name__ == "__main__":
    asyncio.run(main())