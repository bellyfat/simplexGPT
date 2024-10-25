# SimplexGPT

SimplexGPT is a privacy-focused chatbot that uses SimpleX Chat as its messaging interface. It leverages the Ollama API to provide intelligent, conversational responses to user questions, similar to how Telegram bots interact with OpenAI's GPT. This project aims to create a privacy-friendly alternative for users who value confidentiality in their conversations.

## Features
- **Privacy-First Messaging**: Uses SimpleX Chat, a secure messaging platform, instead of traditional centralized services like Telegram.
- **AI-Powered Chatbot**: Connects to the Ollama API to provide detailed responses to user queries.
- **WebSocket Integration**: Communicates with the SimpleX Chat CLI using a local WebSocket server.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- SimpleX Chat CLI installed ([SimpleX Chat GitHub](https://github.com/simplex-chat/simplex-chat))
- WebSockets library for Python
- Ollama API access

### Installation & Setup

1. Install SimpleX Chat CLI
   You can find the instructions here: https://simplex.chat/docs/cli.html

2. Clone the repository:
   ```bash
   git clone https://github.com/cammclain/simplexGPT.git
   cd simplexGPT
   ```
3. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Bot

1. **Start SimpleX Chat CLI**
   Make sure SimpleX Chat CLI is running and listening on port 5225:
   ```bash
   simplex-chat
   ```

2. **Run SimplexGPT**
   Run the Python script to start the bot:
   ```bash
   python simplex_gpt.py
   ```

The bot will connect to the SimpleX WebSocket server and start listening for messages. Any message starting with `/ask` will be processed by the Ollama API, and the response will be sent back to the user.

## Configuration
- **Ollama API**: Ensure that you have access to the Ollama API and set up your API credentials in the environment variables.
- **WebSocket Settings**: By default, SimplexGPT connects to `ws://localhost:5225`. Update the `SIMPLEX_WS_URL` in the Python script if needed.

## Contributing
Feel free to contribute by opening issues or submitting pull requests. We welcome enhancements and bug fixes.

### TODOs:
- Implement command handlers for more interactive commands.
- Add support for memory and knowledge storage using Phidata.
- Expand chatbot functionality to include additional integrations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **SimpleX Chat** for providing a privacy-respecting chat platform.
- **Ollama API** for powering the chatbot responses.
- **Phidata** for offering tools to extend LLM functionality with additional features like long-term memory and web browsing.

## Links
- [SimpleX Chat](https://simplex.chat/)
- [Ollama API](https://ollama.com/)
- [Phidata on GitHub](https://github.com/phidatahq/phidata)

