import asyncio
from app.application import SimpleXGPT

async def test_message_flow():
    app = SimpleXGPT()
    await app.run()

if __name__ == "__main__":
    asyncio.run(test_message_flow())
