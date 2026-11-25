"""
Agent Orchestrator for managing and coordinating different AI agents.
"""

from typing import List
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory


class AgentOrchestrator:
    """
    Exectes AI agent in sequence
    """

    def __init__(self, memory: SharedMemory, conversation_memory):
        self.agents = []
        self.memory = memory
        self.conversation_memory = conversation_memory

    def register(self, agent: BaseAgent) -> None:
        """
        Register a new agent to the orchestrator.
        Args: 
            agent (BaseAgent): The agent to be registered.
        """
        self.agents.append(agent)

    def execute(self):
        print("\n Executing agents in sequence...")
        for agent in self.agents:
            print(f"\n Executing {agent.get_agent_name()}...")
            response = agent.execute()
            print(f"{response.agent_name} completed successfully")

        print("Workflow completed!")
        return self.memory.get("reviewer")  