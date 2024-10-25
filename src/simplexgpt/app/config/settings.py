from __future__ import annotations
from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    simplex_chat_cli_url: str = os.getenv("SIMPLEX_CHAT_CLI_URL")
    ollama_api_url: str = os.getenv("OLLAMA_API_URL")
