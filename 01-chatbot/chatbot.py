"""
Gen AI Project 1: Conversational Chatbot
=========================================
Concepts covered:
  - Connecting to the Claude API
  - System prompts (giving the AI a persona/role)
  - Conversation history (how the AI remembers context)
  - Multi-turn chat loops
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# CONCEPT 1: The Client
# The Anthropic client is your connection to the AI model.
# It reads ANTHROPIC_API_KEY from your .env file automatically.
# ---------------------------------------------------------------------------
client = Anthropic()

# ---------------------------------------------------------------------------
# CONCEPT 2: System Prompt
# A system prompt tells the AI WHO it is and HOW it should behave.
# You set this once at the start — the user never sees it directly.
# Try changing this to make the bot take on a different persona.
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a friendly and patient Gen AI tutor.
Your job is to help beginners learn about Generative AI concepts.
Keep explanations simple, use real-world analogies, and encourage curiosity.
When asked something outside Gen AI, gently steer the conversation back."""

# ---------------------------------------------------------------------------
# CONCEPT 3: Conversation History
# LLMs are stateless — they don't remember previous messages on their own.
# We maintain a list of messages and send the full history with each request.
# Each message has a "role": either "user" or "assistant".
# ---------------------------------------------------------------------------
conversation_history = []


def chat(user_message: str) -> str:
    """Send a message and get a reply, preserving conversation context."""

    # Add the user's message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # ---------------------------------------------------------------------------
    # CONCEPT 4: The API Call
    # We send:
    #   - model: which Claude model to use
    #   - max_tokens: the maximum length of the response
    #   - system: the system prompt (the AI's instructions)
    #   - messages: the full conversation so far
    # ---------------------------------------------------------------------------
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Fast and cost-effective for learning
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    # Extract the assistant's reply text
    assistant_message = response.content[0].text

    # Add the assistant's reply to history so future turns have full context
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def show_welcome():
    print("=" * 60)
    print("  Gen AI Tutor Chatbot")
    print("  Your personal guide to Generative AI")
    print("=" * 60)
    print("  Type your question and press Enter.")
    print("  Commands: 'history' | 'clear' | 'quit'")
    print("=" * 60)
    print()


def main():
    show_welcome()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        # --- Built-in commands ---
        if user_input.lower() == "quit":
            print("Goodbye! Keep learning!")
            break

        elif user_input.lower() == "clear":
            # Reset history — the bot forgets everything
            conversation_history.clear()
            print("[Conversation cleared. Starting fresh.]\n")
            continue

        elif user_input.lower() == "history":
            # Show the raw message history — great for understanding how context works
            if not conversation_history:
                print("[No messages yet.]\n")
            else:
                print("\n--- Conversation History ---")
                for i, msg in enumerate(conversation_history, 1):
                    role = msg["role"].upper()
                    preview = msg["content"][:120].replace("\n", " ")
                    print(f"  {i}. [{role}] {preview}...")
                print("----------------------------\n")
            continue

        # --- Send to AI ---
        print("Bot: ", end="", flush=True)
        reply = chat(user_input)
        print(reply)
        print()


if __name__ == "__main__":
    main()
