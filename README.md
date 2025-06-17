# AI Assistant Pro - Ollama Chatbot

A ChatGPT-style interface for interacting with Ollama models, featuring a modern UI and persistent chat history.

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Qwen2.5-vl model pulled in Ollama

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ollama-chatbot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure Ollama is running and the model is pulled:
```bash
ollama run qwen2.5vl:3b
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Start chatting with the AI assistant!

## Features

- 🎨 Modern ChatGPT-style interface
- 💬 Real-time chat interactions
- 🚀 Fast responses using Ollama backend
- ⌨️ Enter key support for sending messages
- 🎯 Error handling and user feedback

## Keyboard Shortcuts

- `Enter`: Send message
- `Shift + Enter`: New line in input

## Troubleshooting

1. If you get connection errors, ensure Ollama is running:
```bash
ollama serve
```

2. If the model is not responding, verify the model is installed:
```bash
ollama list
```

3. Common error messages and solutions:
   - "Connection refused": Ollama is not running
   - "Model not found": Need to pull the model first
   - "Error from Ollama": Check Ollama logs for details

## Technical Details

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- AI Model: Qwen2.5-vl (3B parameters)
- API: Ollama API (localhost:11434)

## Configuration

The default configuration uses:
- Host: localhost
- Port: 5000
- Model: qwen2.5vl:3b

To modify these settings, edit the `app.py` file.

## License

[Your License Here]
