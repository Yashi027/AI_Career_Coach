"""
Reviewer Agent
It reviews and improves career roadmap
"""

from agents.base_agent import BaseAgent
from prompts.reviewer_prompt import REVIEWER_PROMPT

class ReviewerAgent(BaseAgent):
    def get_agent_name(self):
        return "Reviewer Agent"

    def get_memory_key(self):
        return "reviewer"

    def build_prompt(self):
        writer_response = self.memory.get("writer")
        return REVIEWER_PROMPT.format(roadmap=writer_response)