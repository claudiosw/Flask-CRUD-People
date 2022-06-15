from typing import Type, Dict
from src.models.person_repository import PersonRepository
from src.models.tuples import PersonsTuple
from .interface.person_interface import PersonInterface


class FindPersonController(PersonInterface):
    """ Class to define personcase: Find Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def run(self, person_informations: Dict) -> Dict[bool, PersonsTuple]:
        """Register person
        :param  - person_informations: person informations
        :return - Dictionary with informations of the process
        """

        try:
            self.__convert_validate(person_informations)
            person = self.person_repository.select_person(
                person_informations["name"]
            )
            return {"success": True, "person_registry": person}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __convert_validate(self, person_informations: Dict):

        validate_entry = (
            isinstance(person_informations['name'], str)
        )
        if not validate_entry:
            raise
