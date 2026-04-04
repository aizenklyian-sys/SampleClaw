import asyncio
import logging
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sampleclaw.core.agent import Agent
from sampleclaw.memory.short_term_memory import ShortTermMemory
from sampleclaw.memory.long_term_memory import LongTermMemory
from sampleclaw.skills.skill_manager import SkillManager
from sampleclaw.skills.example_skills import search_web, execute_code, think
from sampleclaw.safety.safety_mechanisms import SafetyMechanisms

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    # 1. Initialize Memory
    stm = ShortTermMemory()
    ltm = LongTermMemory()

    # 2. Initialize Skill Manager and Register Skills
    sm = SkillManager()
    sm.register_skill("search_web", "Searches the web for information.", search_web)
    sm.register_skill("execute_code", "Executes Python code snippets.", execute_code)
    sm.register_skill("think", "Expresses a thought or internal monologue.", think)

    # 3. Initialize Safety Mechanisms
    safety = SafetyMechanisms(forbidden_actions=["delete_database"])

    # 4. Initialize the Agent
    agent = Agent(
        name="ClawBot",
        goal="research the history of autonomous AI agents and write a summary",
        short_term_memory=stm,
        long_term_memory=ltm,
        skill_manager=sm,
        safety_mechanisms=safety
    )

    # 5. Run the Agent
    print(f"--- Starting Agent: {agent.name} ---")
    status = await agent.run()
    print(f"--- Agent {agent.name} finished with status: {status} ---")

if __name__ == "__main__":
    asyncio.run(main())
