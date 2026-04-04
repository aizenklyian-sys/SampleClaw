import asyncio
import logging
from typing import List, Dict, Any, Optional

from ..memory.short_term_memory import ShortTermMemory
from ..memory.long_term_memory import LongTermMemory
from ..skills.skill_manager import SkillManager
from ..safety.safety_mechanisms import SafetyMechanisms

logger = logging.getLogger(__name__)

class Agent:
    def __init__(
        self,
        name: str,
        goal: str,
        short_term_memory: ShortTermMemory,
        long_term_memory: LongTermMemory,
        skill_manager: SkillManager,
        safety_mechanisms: SafetyMechanisms,
        llm_model: Any = None, # Placeholder for LLM integration
    ):
        self.name = name
        self.goal = goal
        self.short_term_memory = short_term_memory
        self.long_term_memory = long_term_memory
        self.skill_manager = skill_manager
        self.safety_mechanisms = safety_mechanisms
        self.llm_model = llm_model
        self.current_plan: List[Dict[str, Any]] = []
        self.status: str = "initialized"

    async def _plan(self) -> List[Dict[str, Any]]:
        """Generates a plan based on the current goal, memory, and available skills."""
        context = self.short_term_memory.get_context()
        knowledge = self.long_term_memory.retrieve_relevant_knowledge(self.goal)
        available_skills = self.skill_manager.list_skills()

        prompt = f"""You are {self.name}, an autonomous AI agent. Your current goal is: {self.goal}.

        Current Context:
        {context}

        Relevant Knowledge:
        {knowledge}

        Available Skills:
        {available_skills}

        Based on the above, generate a detailed plan to achieve your goal. The plan should be a list of steps, where each step is a dictionary containing 'action' (the skill to use) and 'parameters' (a dictionary of arguments for the skill). If no specific skill is needed, use 'think' as the action.
        Example plan format: 
        [{{"action": "think", "parameters": {{"thought": "I need to break down the problem."}}}},
         {{"action": "search_web", "parameters": {{"query": "how to achieve X"}}}},
         {{"action": "execute_code", "parameters": {{"code": "print('hello')"}}}}]
        """
        
        # Placeholder for LLM call to generate plan
        # In a real implementation, this would call the LLM with the prompt
        logger.info(f"Agent {self.name} is planning...")
        # For now, return a dummy plan for demonstration
        await asyncio.sleep(0.5) # Simulate LLM delay
        return [
            {"action": "think", "parameters": {"thought": "I will start by analyzing the goal and formulating a strategy."}},
            {"action": "search_web", "parameters": {"query": f"best ways to achieve {self.goal}"}},
            {"action": "think", "parameters": {"thought": "I will now proceed with the gathered information."}}
        ]

    async def _act(self, action: str, parameters: Dict[str, Any]) -> Any:
        """Executes a given action using the skill manager."""
        logger.info(f"Agent {self.name} is acting: {action} with parameters {parameters}")
        if not self.safety_mechanisms.pre_action_check(action, parameters):
            logger.warning(f"Safety mechanism blocked action: {action}")
            return {"status": "blocked", "reason": "Safety mechanism"}

        try:
            # Skill execution could be async as well
            if asyncio.iscoroutinefunction(self.skill_manager.skills.get(action)):
                result = await self.skill_manager.execute_skill(action, parameters)
            else:
                result = self.skill_manager.execute_skill(action, parameters)
            
            self.safety_mechanisms.post_action_check(action, result)
            return result
        except Exception as e:
            logger.error(f"Error executing action {action}: {e}")
            return {"status": "error", "message": str(e)}

    def _observe(self, result: Any):
        """Observes the result of an action and updates short-term memory."""
        logger.info(f"Agent {self.name} observed: {result}")
        self.short_term_memory.add_observation(result)

    async def _reflect_and_recover(self, last_action_result: Any) -> bool:
        """Performs self-reflection and attempts error recovery."""
        if isinstance(last_action_result, dict) and (last_action_result.get("status") == "error" or last_action_result.get("status") == "blocked"):
            logger.warning(f"Agent {self.name} needs to recover from: {last_action_result}")
            # In a real implementation, the LLM would be used to analyze the error
            # and suggest recovery steps or a new plan.
            self.short_term_memory.add_observation(f"Error encountered: {last_action_result}. Reflecting on how to recover.")
            await asyncio.sleep(0.5) # Simulate reflection time
            return False # Indicate that a new plan is needed
        return True # Indicate success, continue with current plan or re-plan if goal achieved

    async def run(self):
        """Starts the agent's autonomous loop."""
        self.status = "running"
        logger.info(f"Agent {self.name} started with goal: {self.goal}")
        while self.status == "running":
            if not self.current_plan:
                self.current_plan = await self._plan()
                if not self.current_plan:
                    logger.info(f"Agent {self.name} has no plan and cannot proceed. Stopping.")
                    self.status = "stopped"
                    break

            next_step = self.current_plan.pop(0)
            action = next_step.get("action")
            parameters = next_step.get("parameters", {})

            action_result = await self._act(action, parameters)
            self._observe(action_result)

            if not await self._reflect_and_recover(action_result):
                logger.info(f"Agent {self.name} is re-planning due to error recovery.")
                self.current_plan = [] # Clear current plan to force re-planning

            # Check if the goal is achieved (simulated)
            if not self.current_plan and self.status == "running":
                logger.info(f"Agent {self.name} completed all planned steps. Goal achieved!")
                self.status = "completed"

        logger.info(f"Agent {self.name} finished with status: {self.status}")
        return self.status
