"""
Conversation memory for storing and retrieving conversation history.
Responsibilities:
- Store user messages
- Store AI responses
- Retrieve complete conversation history
- Build conversation context for AI agents
"""

from typing import List

class ConversationMemory:
    def __init__(self):
        """Initialize the conversation memory."""
        self._messages: List[str] = []

    def add_message(self, message: str):
        """Add a user message to the conversation memory."""
        self._messages.append(f"User: {message}")

    def add_response(self, response: str):
        """Add an AI response to the conversation memory."""
        self._messages.append(f"AI: {response}")

    def get_context(self) -> str:
        """Retrieve the complete conversation history as a single string."""
        return "\n".join(self._messages)

    def clear(self):
        """Clear the conversation memory."""
        self._messages.clear()

    def display(self, max_len: int = 120):
        """Display the conversation history."""
        if not self._messages:
            print("No conversation history.")
        else:
            for message in self._messages:
                preview = message[:max_len] + "..."
                print(preview)