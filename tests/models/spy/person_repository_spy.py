from typing import List
from src.models.tuples import PersonsTuple
from tests.models.mock_persons import mock_persons


class PersonRepositorySpy:
    """ Spy to Person Repository """

    def __init__(self):
        self.insert_person_params = {}
        self.select_person_params = {}
        self.update_person_params = {}
        self.delete_person_params = {}

    def insert_person(self, name: str, age: int, neighbourhood: str, profession: str) -> PersonsTuple:
        """ Spy to all the attributes """

        self.insert_person_params["name"] = name
        self.insert_person_params["age"] = age
        self.insert_person_params["neighbourhood"] = neighbourhood
        self.insert_person_params["profession"] = profession

        return mock_persons()

    def select_person(self, name: str = None) -> List[PersonsTuple]:
        """ Spy to all the attributes """

        self.select_person_params["name"] = name

        return [mock_persons()]

    def update_person(self, name: str, age: int, neighbourhood: str, profession: str) -> PersonsTuple:
        """ Spy to all the attributes """

        self.update_person_params["name"] = name
        self.update_person_params["age"] = age
        self.update_person_params["neighbourhood"] = neighbourhood
        self.update_person_params["profession"] = profession

        return mock_persons()

    def delete_person(self, name: str = None) -> List[PersonsTuple]:
        """ Spy to all the attributes """

        self.delete_person_params["name"] = name

        return [mock_persons()]
