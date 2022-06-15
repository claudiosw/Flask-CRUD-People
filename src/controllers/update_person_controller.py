from typing import Type, Dict
from src.models.person_repository import PersonRepository
from src.models.tuples import PersonsTuple
from .interface.person_interface import PersonInterface


class UpdatePersonController(PersonInterface):
    """ Class to define personcase: Register Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def run(self, person_informations: Dict) -> Dict[bool, PersonsTuple]:
        """Register person
        :param  - person_informations: person informations
        :return - Dictionary with informations of the process
        """

        try:
            self.__convert_validate(person_informations)
            new_person = self.person_repository.update_person(
                person_informations["name"],
                person_informations["age_int"],
                person_informations["neighbourhood"],
                person_informations["profession"]
            )
            return {"success": True, "person_registry": new_person}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __convert_validate(self, person_informations: Dict):
        try:
            person_informations['age_int'] = int(person_informations['age'])
            validate_entry = (
                isinstance(person_informations['name'], str)
                and isinstance(person_informations['neighbourhood'], str)
                and isinstance(person_informations['age_int'], int)
                and isinstance(person_informations['profession'], str)
            )
            if not validate_entry:
                raise
        except ValueError:
            raise ValueError("Age is not an integer")
