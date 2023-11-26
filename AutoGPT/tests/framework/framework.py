from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from ..sandbox.sandbox import execute_program_routine_python

@dataclass
class Framework:
    """
    Framework class to store framework information.
    """
    name: str
    description: str
    text_routine: str
    program_routine: str
    program_instructions: str
    knowledge_of_task: List[str] = field(default_factory=list) #contains the info gathered by running the
    # framework multiple times (code errors, task solved in how many attempts, etc)
    parent_frameworks: List[str] = field(default_factory=list)
    child_frameworks: List[str] = field(default_factory=list)

    def test_program_routine(self, program_routine: str):
        """
        tests the program routine of the framework.

        Args:
            program_routine: Program routine to test.

        Returns:
            Tuple[str, str]: Output and error of the program routine.
        """



    def add_knowledge_of_task(self, knowledge: str) -> None:
        """
        Adds knowledge of the task to the framework.

        Args:
            knowledge: Knowledge of the task.
        """
        self.knowledge_of_task.append(knowledge)

    def add_parent_framework(self, parent_framework: str) -> None:
        """
        Adds a parent framework to the framework.

        Args:
            parent_framework: Name of the parent framework.
        """
        self.parent_frameworks.append(parent_framework)

    def add_child_framework(self, child_framework: str) -> None:
        """
        Adds a child framework to the framework.

        Args:
            child_framework: Name of the child framework.
        """
        self.child_frameworks.append(child_framework)

    def remove_parent_framework(self, parent_framework: str) -> None:
        """
        Removes a parent framework from the framework.

        Args:
            parent_framework: Name of the parent framework.

        Raises:
            ValueError: If the parent framework is not found.
        """
        try:
            self.parent_frameworks.remove(parent_framework)
        except ValueError:
            raise ValueError(f"Parent framework '{parent_framework}' not found.")

    def remove_child_framework(self, child_framework: str) -> None:
        """
        Removes a child framework from the framework.

        Args:
            child_framework: Name of the child framework.

        Raises:
            ValueError: If the child framework is not found.
        """
        try:
            self.child_frameworks.remove(child_framework)
        except ValueError:
            raise ValueError(f"Child framework '{child_framework}' not found.")

    def to_json(self) -> Dict[str, List[str]]:
        """
        Converts the framework to a JSON object.

        Returns:
            Dict[str, List[str]]: JSON object representing the framework.
        """
        return {
            "name": self.name,
            "description": self.description,
            "parent_frameworks": self.parent_frameworks,
            "child_frameworks": self.child_frameworks
        }

    def __str__(self) -> str:
        return f"Framework: {self.name}, Description: {self.description}"

    def __repr__(self) -> str:
        return (f"Framework(name={self.name!r}, description={self.description!r}, "
                f"parent_frameworks={self.parent_frameworks!r}, child_frameworks={self.child_frameworks!r})")

