# Project 1: Conversational Chatbot

A beginner-friendly chatbot that teaches you the core building blocks of Gen AI apps.

## What You'll Learn

| Concept | Where in code |
|---|---|
| Connecting to an LLM API | `client = Anthropic()` |
| System prompts | `SYSTEM_PROMPT` variable |
| Conversation history | `conversation_history` list |
| Multi-turn chat | `chat()` function |

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your API key
cp .env.example .env
# Edit .env and paste your key from https://console.anthropic.com/

# 3. Run the chatbot
python chatbot.py
```

## Try These Experiments

1. **Change the persona** — Edit `SYSTEM_PROMPT` to make it a cooking assistant or fitness coach
2. **Watch the history** — Type `history` after a few messages to see how context is stored
3. **Test memory** — Ask "what was my first question?" to see conversation memory in action
4. **Clear and retest** — Type `clear`, then ask "what was my first question?" — the bot forgets!
5. **Change the model** — Swap `claude-haiku-4-5-20251001` for `claude-sonnet-4-6` for smarter replies

## Key Concepts

### Why do we send the full history every time?
LLMs are **stateless** — each API call is independent. To simulate memory, we manually
include all previous messages in every request. This is how every chatbot (ChatGPT, etc.) works.

### What is `max_tokens`?
It caps how long the response can be. 1 token ≈ 0.75 words. 1024 tokens ≈ ~750 words.

### System prompt vs user message?
- **System prompt**: Instructions for the AI (its role, rules, personality)
- **User message**: What the human types
- **Assistant message**: What the AI replies
