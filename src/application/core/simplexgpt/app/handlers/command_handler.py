from app.connections.ollama_client import OllamaClient

class CommandHandler:
    def __init__(self, ollama_client: OllamaClient):
        self.ollama_client = ollama_client

    async def handle_ask(self, prompt: str) -> str:
        response = self.ollama_client.get_response(prompt)
        return response
