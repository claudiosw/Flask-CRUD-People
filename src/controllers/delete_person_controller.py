from typing import Type, Dict
from src.models.person_repository import PersonRepository
from src.models.tuples import PersonsTuple
from .interface.delete_person_interface import DeletePersonInterface
from src.errors.http_not_found import HttpNotFound


class DeletePersonController(DeletePersonInterface):
    """ Class to define personcase: Register Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def run(self, name: str) -> Dict[bool, PersonsTuple]:
        """Register person
        :param  - name: person name
        :return - Dictionary with informations of the process
        """

        person = self.person_repository.select_person(
            name
        )
        if person:
            deleted_person = self.person_repository.delete_person(
                name
            )
            return {"success": True, "person_registry": deleted_person}
        else:
            raise HttpNotFound(f"{name} not found")
