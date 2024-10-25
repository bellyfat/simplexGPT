from __future__ import annotations
from rich.console import Console
from app.config.settings import Settings
from app.connections.simplex_client import SimpleXClient
from app.connections.ollama_client import OllamaClient

class SimpleXGPT:
    def __init__(self):
        """Initialize the SimpleXGPT application"""
        self.console = Console()
        self.settings = Settings()  # Load settings from environment
        self.simplex_client = SimpleXClient(self.settings.simplex_chat_cli_url)
        self.ollama_client = OllamaClient(self.settings.ollama_api_url)

    def run(self):
        """Run the chatbot application"""
        self.console.print("[bold green]Starting SimpleXGPT...")
        self.simplex_client.connect()
        self.listen_for_messages()

    def listen_for_messages(self):
        """Listen for incoming messages and handle them accordingly"""
        while True:
            message = self.simplex_client.receive_message()
            if message.startswith('/ask'):
                prompt = message[len('/ask '):]
                response = self.ollama_client.get_response(prompt)
                self.simplex_client.send_message(response)
