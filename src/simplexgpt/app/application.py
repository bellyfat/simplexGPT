from __future__ import annotations
from app.connections.simplex_client import SimpleXClient
from app.connections.ollama_client import OllamaClient
from app.handlers.command_handler import CommandHandler
from app.config.settings import Settings
from rich.console import Console

class SimpleXGPT:
    def __init__(self):
        """Initialize the SimpleXGPT application"""
        self.console = Console()
        self.settings = Settings()  # Load settings from environment
        self.simplex_client = SimpleXClient(self.settings.simplex_chat_cli_url)
        self.ollama_client = OllamaClient(self.settings.ollama_api_url)
        self.command_handler = CommandHandler(self.ollama_client)

    async def run(self):
        """Run the chatbot application"""
        await self.simplex_client.connect()
        await self.listen_for_messages()

    async def listen_for_messages(self):
        """Listen for incoming messages and handle them accordingly"""
        while True:
            message = await self.simplex_client.receive_message()
            self.console.print(f"[blue]Received message: {message}")

            if message.startswith('/ask'):
                prompt = message[len('/ask '):]
                response = await self.command_handler.handle_ask(prompt)
                await self.simplex_client.send_message(response)
