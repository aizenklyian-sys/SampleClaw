from .core.agent import Agent
from .memory.short_term_memory import ShortTermMemory
from .memory.long_term_memory import LongTermMemory
from .skills.skill_manager import SkillManager
from .skills.example_skills import search_web, execute_code, think, write_file, read_file
from .safety.safety_mechanisms import SafetyMechanisms

class AgentFactory:
    @staticmethod
    def create_default_agent(name: str, goal: str) -> Agent:
        """Creates an agent with default skills and settings."""
        sm = SkillManager()
        sm.register_skill("search_web", "Searches the web for information.", search_web)
        sm.register_skill("execute_code", "Executes Python code snippets.", execute_code)
        sm.register_skill("think", "Expresses a thought or internal monologue.", think)
        sm.register_skill("write_file", "Writes content to a file.", write_file)
        sm.register_skill("read_file", "Reads content from a file.", read_file)

        return Agent(
            name=name,
            goal=goal,
            short_term_memory=ShortTermMemory(),
            long_term_memory=LongTermMemory(),
            skill_manager=sm,
            safety_mechanisms=SafetyMechanisms()
        )
