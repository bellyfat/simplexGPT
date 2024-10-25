import asyncio
import websockets
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SIMPLEX_CHAT_CLI_URL = os.getenv("SIMPLEX_CHAT_CLI_URL")

async def test_connect_to_simplex():
    try:
        async with websockets.connect(SIMPLEX_CHAT_CLI_URL) as websocket:
            print("Successfully connected to SimpleX Chat CLI!")
    except Exception as e:
        print(f"Failed to connect to SimpleX Chat CLI: {e}")

if __name__ == "__main__":
    asyncio.run(test_connect_to_simplex())
