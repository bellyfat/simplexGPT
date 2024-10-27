from __future__ import annotations
import requests

class OllamaClient:
    def __init__(self, url: str):
        self.url = url

    def get_response(self, prompt: str) -> str:
        data = {"prompt": prompt}
        response = requests.post(self.url, json=data)
        if response.status_code == 200:
            return response.json().get("response", "Sorry, I couldn't understand the question.")
        else:
            return "Error contacting Ollama API."
