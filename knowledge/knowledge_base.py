"""
Knowledge Base
Provides domain-specific knowledge to AI Agents

Responsibilities:
- Load Knowledge from a JSON file
- Retrieve the knowledge based on search key
- Hide the underlying data source from AI agents
- Prepare the project for future RAG implementation
"""

import json
from typing import Any
from pathlib import Path

class KnowledgeBase:
    """
    Loads and manages domain specific knowledge
    Currently knowledge is loaded from a json file and later ca be implemented through vector database
    """

    def __init__(self, knowledge_file: str) -> None:
        self._knowledge = self._load_knowledge(knowledge_file)

    def _load_knowledge(self, knowledge_file: str) -> dict[str, Any]:
        """
        Load knowledge database
        Args:
            knowledge_file : JSON file path
        Returns: Dictionary containing knowledge
        """

        file_path = Path(knowledge_file)
        if not file_path.exists():
            raise FileNotFoundError(f"Knowledge file not found: {knowledge_file}")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get(self, key: str) -> Any :
        """
        Retrieve knowledge for a given key
        Args:
            key: knowledge
        Returns:
            Matching knowledge or None
        """
        return self._knowledge.get(key)

    def retrieve(self, query: str) -> dict:
        query = query.lower()
        for key, value in self._knowledge.items():
            if key.lower().replace("_"," ") in query:
                return value
        return {}

    def get_all(self) -> dict[str, Any]:
        """
        Returns Complete knowledge base
        """
        return self._knowledge.copy()

    def exists(self, key: str) -> bool:
        """
        check whether a key exists
        Args: key
        Returns: true if present else not
        """
        return key in self._knowledge

    def display(self) -> None:
        """
        Display all available knowledge key
        """
        print("\n" + "="*20)
        print("KNOWLEDGE BASE")
        print("="*20)

        if not self._knowledge:
            print("No available knowledge")
        else:
            for key in self._knowledge.keys():
                print(f"- {key}")
