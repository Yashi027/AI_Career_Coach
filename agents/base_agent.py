"""
Base agent
Every AI agent inherits from this class
"""

from abc import ABC, abstractmethod
from services.gemini_service import GeminiService
from memory.shared_memory import SharedMemory


class BaseAgent :
    """
    Abstract base class for all AI agents
    """
    def __init__(self, memory: SharedMemory):
        super().__init__()
        self.memory = memory
        self.gemini_service = GeminiService()

    @abstractmethod
    def execute(self) -> str:
        """
        Execute the agent's main logic
        :return: The result of the execution
        """
        pass

    def ask_gemini(self, prompt: str) -> str:
        """
        Ask Gemini for a response to the given prompt
        :param prompt: The prompt to send to Gemini
        :return: The response from Gemini
        """
        return self.gemini_service.ask_gemini(prompt)


