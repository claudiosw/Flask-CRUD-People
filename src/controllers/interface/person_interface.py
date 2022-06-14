from abc import ABC, abstractmethod
from typing import Dict
from src.models.tuples import PersonsTuple


class PersonInterface(ABC):

    @abstractmethod
    def run(self, person_informations: Dict) -> Dict[bool, PersonsTuple]:
        pass
