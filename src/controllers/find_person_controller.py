from typing import Type, Dict
from src.models.person_repository import PersonRepository
from src.models.tuples import PersonsTuple
from .interface.find_person_interface import FindPersonInterface


class FindPersonController(FindPersonInterface):
    """ Class to define personcase: Find Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def run(self, name: str) -> Dict[bool, PersonsTuple]:
        """Register person
        :param  - name: person name
        :return - Dictionary with informations of the process
        """

        try:
            self.__convert_validate(name)
            person = self.person_repository.select_person(
                name
            )
            return {"success": True, "person_registry": person}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __convert_validate(self, name: str):

        validate_entry = (
            isinstance(name, str)
        )
        if not validate_entry:
            raise
