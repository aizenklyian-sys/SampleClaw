from typing import List, Dict, Any

class ShortTermMemory:
    def __init__(self, max_entries: int = 100):
        self.memory: List[Dict[str, Any]] = []
        self.max_entries = max_entries

    def add_observation(self, observation: Any):
        self.memory.append({"type": "observation", "content": observation})
        if len(self.memory) > self.max_entries:
            self.memory.pop(0) # Remove oldest entry

    def add_thought(self, thought: str):
        self.memory.append({"type": "thought", "content": thought})
        if len(self.memory) > self.max_entries:
            self.memory.pop(0)

    def get_context(self) -> List[Dict[str, Any]]:
        return self.memory

    def clear(self):
        self.memory = []
