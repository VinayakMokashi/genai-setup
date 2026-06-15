# GenAI Setup

A Groq API connection test and a simple Gradio chatbot powered by LLaMA.

## Prerequisites

- Python 3.10+
- A virtual environment (recommended)

## Installation

In your activated Python environment, install the required packages:

```bash
pip install groq python-dotenv gradio
```

## Groq API Key

1. Visit [Groq's platform](https://console.groq.com), create an account, and generate an API key.
2. Create a file named `.env` in this folder:

```
GROQ_API_KEY="your-api-key-here"
```

> The `.env` file is listed in `.gitignore` and will never be committed.

## Files

| File | Purpose |
|------|---------|
| `verify_groq.py` | Verifies your Groq API key works by calling `llama-3.1-8b-instant` |
| `app_chatbot.py` | A streaming Gradio chatbot using `llama-3.3-70b-versatile` |

## Step 1 — Verify your API key

```bash
python verify_groq.py
```

Expected output: a short "Hello World" style message from the model.

## Step 2 — Run the chatbot

```bash
python app_chatbot.py
```

Open the local URL printed in your terminal (e.g. `http://127.0.0.1:7860`) in your browser. You'll see a full chat interface with conversation history.

## How it works

- `verify_groq.py` makes a single chat completion request and prints the response.
- `app_chatbot.py` uses Gradio's `ChatInterface` with streaming enabled. Each user message is sent along with the full conversation history and a system prompt (`"You are a helpful assistant"`), so the model maintains context across turns.
