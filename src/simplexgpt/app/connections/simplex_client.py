# this file is responsible for connecting to the simplex chat cli
from __future__ import annotations
import websockets
import asyncio

class SimpleXClient:
    def __init__(self, url: str):
        self.url = url

    async def connect(self):
        self.connection = await websockets.connect(self.url)

    async def receive_message(self):
        return await self.connection.recv()

    async def send_message(self, message: str):
        await self.connection.send(message)
