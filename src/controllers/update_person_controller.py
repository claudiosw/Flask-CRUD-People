from typing import Type, Dict
from src.models.person_repository import PersonRepository
from src.models.tuples import PersonsTuple
from .interface.update_person_interface import UpdatePersonInterface


class UpdatePersonController(UpdatePersonInterface):
    """ Class to define personcase: Register Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def run(self, person_informations: Dict) -> Dict[bool, PersonsTuple]:
        """Register person
        :param  - person_informations: person informations
        :return - Dictionary with informations of the process
        """

        new_person = self.person_repository.update_person(
            person_informations["name"],
            person_informations["age"],
            person_informations["neighbourhood"],
            person_informations["profession"]
        )
        return {"success": True, "person_registry": new_person}
