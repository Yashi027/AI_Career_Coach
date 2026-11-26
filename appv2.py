"""
AI Career Coach
Entry point for the AI Career Coach application
"""


from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from memory.shared_memory import SharedMemory
from memory.conversation_memory import ConversationMemory
from services.gemini_service import GeminiService
from orchestrator.agent_orchestrator import AgentOrchestrator
from knowledge.knowledge_base import KnowledgeBase

def main() -> None:
    gemini_service = GeminiService()
    conversation_memory = ConversationMemory()
    knowledge_base = KnowledgeBase("data/career_knowledge.json")
    while(True):
        print("="*30)
        print("Welcome to the AI Career Coach!")
        print("="*30)

        user_query = input("Please enter your career goal: \n")
        if(user_query.lower() == "exit" or user_query.lower() == "bye"):
            return
        memory = SharedMemory()

        conversation_memory.add_message(user_query)

        memory.add("user_query", user_query)

        planner = PlannerAgent(memory, gemini_service, conversation_memory, knowledge_base)
        research = ResearchAgent(memory, gemini_service, conversation_memory, knowledge_base)
        writer = WriterAgent(memory, gemini_service, conversation_memory, knowledge_base)
        reviewer = ReviewerAgent(memory, gemini_service, conversation_memory, knowledge_base)

        orchestrator = AgentOrchestrator(memory, conversation_memory)
        orchestrator.register(planner)
        orchestrator.register(research)
        orchestrator.register(writer)
        orchestrator.register(reviewer)

        final_response = orchestrator.execute()
        print("="*30)
        print("Final Career Roadmap:")
        print("="*30)
        print(final_response.output)
        conversation_memory.display()

if __name__ == "__main__":
    main()
