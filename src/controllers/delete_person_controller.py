from typing import Type, Dict
from src.models.person_repository import PersonRepository
from src.models.tuples import PersonsTuple
from .interface.delete_person_interface import DeletePersonInterface


class DeletePersonController(DeletePersonInterface):
    """ Class to define personcase: Register Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def run(self, name: str) -> Dict[bool, PersonsTuple]:
        """Register person
        :param  - name: person name
        :return - Dictionary with informations of the process
        """

        try:
            self.__convert_validate(name)
            new_person = self.person_repository.delete_person(
                name
            )
            return {"success": True, "person_registry": new_person}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __convert_validate(self, name: str):
        validate_entry = (
            isinstance(name, str)
        )
        if not validate_entry:
            raise
