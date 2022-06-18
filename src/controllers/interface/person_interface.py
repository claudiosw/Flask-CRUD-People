from abc import ABC, abstractmethod
from typing import Dict
from src.models.tuples import PersonsTuple


class FindPersonInterface(ABC):

    @abstractmethod
    def run(self, name: str) -> Dict[bool, PersonsTuple]:
        pass
