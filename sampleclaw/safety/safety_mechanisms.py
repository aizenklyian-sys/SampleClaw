import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class SafetyMechanisms:
    def __init__(self, forbidden_actions: Optional[List[str]] = None):
        self.forbidden_actions = forbidden_actions if forbidden_actions is not None else []
        logger.info(f"Safety mechanisms initialized with forbidden actions: {self.forbidden_actions}")

    def pre_action_check(self, action: str, parameters: Dict[str, Any]) -> bool:
        """Performs checks before an action is executed."""
        if action in self.forbidden_actions:
            logger.warning(f"Action \'{action}\' is forbidden by safety mechanisms.")
            return False

        # Example: Prevent code execution if it contains dangerous keywords
        if action == "execute_code" and "code" in parameters:
            dangerous_keywords = ["rm -rf", "format c:", "sudo"]
            for keyword in dangerous_keywords:
                if keyword in parameters["code"].lower():
                    logger.warning(f"Code execution blocked due to dangerous keyword: {keyword}")
                    return False

        # Add more sophisticated checks here (e.g., content moderation, resource limits)

        return True

    def post_action_check(self, action: str, result: Any) -> bool:
        """Performs checks after an action has been executed."""
        # Example: Check if the result contains sensitive information that should not be logged
        if "sensitive_data" in str(result).lower():
            logger.warning(f"Sensitive data detected in post-action result for \'{action}\'.")
            # Potentially redact or flag the result

        return True


    def update_forbidden_actions(self, new_forbidden_actions: List[str]):
        self.forbidden_actions = new_forbidden_actions
        logger.info(f"Forbidden actions updated to: {self.forbidden_actions}")
