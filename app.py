"""
AI Career Coach
Entry point for the AI Career Coach application
"""


from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from memory.shared_memory import SharedMemory
from services.gemini_service import GeminiService

def main() -> None:
    print("="*30)
    print("Welcome to the AI Career Coach!")
    print("="*30)

    user_query = input("Please enter your career goal: \n")
    memory = SharedMemory()
    gemini_service = GeminiService()

    memory.add("user_query", user_query)

    planner = PlannerAgent(memory, gemini_service)
    research = ResearchAgent(memory, gemini_service)
    writer = WriterAgent(memory, gemini_service)
    reviewer = ReviewerAgent(memory, gemini_service)

    print("\n Planning career roadmap...")
    planner.execute()

    print("\n Conducting research...")
    research.execute()

    print("\n Writing career roadmap...")
    writer.execute()

    print("\n Reviewing career roadmap...")
    reviewer.execute()

    final_response = memory.get("reviewer")
    print("="*30)
    print("Final Career Roadmap:")
    print("="*30)
    print(final_response.output)

if __name__ == "__main__":
    main()
