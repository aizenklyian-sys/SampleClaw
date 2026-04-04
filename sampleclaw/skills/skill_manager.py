from typing import Callable, Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class SkillManager:
    def __init__(self):
        self.skills: Dict[str, Callable] = {}
        self.skill_descriptions: Dict[str, str] = {}

    def register_skill(self, name: str, description: str, func: Callable):
        if name in self.skills:
            logger.warning(f"Skill '{name}' already registered. Overwriting.")
        self.skills[name] = func
        self.skill_descriptions[name] = description
        logger.info(f"Skill '{name}' registered.")

    def execute_skill(self, name: str, parameters: Dict[str, Any]) -> Any:
        if name not in self.skills:
            raise ValueError(f"Skill '{name}' not found.")
        logger.debug(f"Executing skill '{name}' with parameters: {parameters}")
        return self.skills[name](**parameters)

    def list_skills(self) -> List[Dict[str, str]]:
        return [{
            "name": name,
            "description": self.skill_descriptions[name]
        } for name in self.skills]

    def unregister_skill(self, name: str):
        if name in self.skills:
            del self.skills[name]
            del self.skill_descriptions[name]
            logger.info(f"Skill '{name}' unregistered.")
        else:
            logger.warning(f"Skill '{name}' not found for unregistration.")
