# this file is responsible for connecting to the simplex chat cli
import websockets
import asyncio

class SimpleXClient:
    def __init__(self, url: str):
        self.url = url
        self.connection = None

    async def connect(self):
        self.connection = await websockets.connect(self.url)
        print("Connected to SimpleX Chat CLI")

    async def receive_message(self) -> str:
        return await self.connection.recv()

    async def send_message(self, message: str):
        await self.connection.send(message)
        print(f"Sent message: {message}")
