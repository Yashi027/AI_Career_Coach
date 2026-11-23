"""
Base agent
Every AI agent inherits from this class

Responsibilities:
- Built prompt
- Send prompt to Gemini Service
- Create agent response
- Store response in shared memory
- Return agent response to the caller
"""

from abc import ABC, abstractmethod
from typing import Any
from services.gemini_service import GeminiService
from memory.shared_memory import SharedMemory
from models.agent_response import AgentResponse


class BaseAgent(ABC) :
    """
    Abstract base class for all AI agents
    """
    def __init__(self, memory: SharedMemory, gemini_service: GeminiService):
        super().__init__()
        self.memory = memory
        self.gemini_service = gemini_service

    @abstractmethod
    def get_agent_name(self) -> str:
        """
        Get the name of the agent
        :return: The name of the agent
        example: planner, research
        """
        pass

    @abstractmethod
    def get_memory_key(self) -> str:
        """
        Return the memory key for this agent's data in shared memory
        :return: The memory key as a string
        """
        pass

    @abstractmethod
    def build_prompt(self) -> str:
        """
        Build the prompt to be sent to Gemini
        :return: The constructed prompt as a string
        """
        pass

    def execute(self) -> Any:
        """
        Execute the agent's main logic
        Build the prompt, send it to Gemini, store the response in shared memory, and return the response
        :return: The result of the execution
        """
        prompt = self.build_prompt()
        response = self.gemini_service.generate_response(prompt)
        agentResponse = AgentResponse(
            agent_name=self.get_agent_name(),
            output = response.text
        )
        self.memory.add(self.get_memory_key(), agentResponse)
        return agentResponse

    def ask_gemini(self, prompt: str) -> str:
        """
        Ask Gemini for a response to the given prompt
        :param prompt: The prompt to send to Gemini
        :return: The response from Gemini
        """
        return self.gemini_service.ask_gemini(prompt)


