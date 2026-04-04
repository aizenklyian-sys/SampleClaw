import json
import os
from typing import Dict, Any, List

class LongTermMemory:
    def __init__(self, storage_path: str = "./long_term_memory.json"):
        self.storage_path = storage_path
        self.knowledge_base: List[Dict[str, Any]] = self._load_knowledge_base()

    def _load_knowledge_base(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                return json.load(f)
        return []

    def _save_knowledge_base(self):
        with open(self.storage_path, "w") as f:
            json.dump(self.knowledge_base, f, indent=4)

    def add_knowledge(self, knowledge_entry: Dict[str, Any]):
        self.knowledge_base.append(knowledge_entry)
        self._save_knowledge_base()

    def retrieve_relevant_knowledge(self, query: str) -> List[Dict[str, Any]]:
        # In a real-world scenario, this would involve more sophisticated retrieval
        # mechanisms like vector embeddings and similarity search.
        # For now, a simple keyword-based search or returning all knowledge is used.
        relevant_entries = []
        for entry in self.knowledge_base:
            if query.lower() in json.dumps(entry).lower():
                relevant_entries.append(entry)
        return relevant_entries if relevant_entries else self.knowledge_base # Return all if no specific match

    def clear(self):
        self.knowledge_base = []
        self._save_knowledge_base()
