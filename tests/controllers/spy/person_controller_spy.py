from typing import Dict
from src.models.tuples import PersonsTuple
from tests.models.mock_persons import mock_persons


class RegisterPersonControllerSpy:
    """ Spy to Person Controller """

    def __init__(self):
        self.insert_person_params = {}

    def run(self, person_informations: Dict) -> PersonsTuple:
        """ Spy to all the attributes """

        self.insert_person_params["name"] = person_informations['name']
        self.insert_person_params["age"] = person_informations['age']
        self.insert_person_params["neighbourhood"] = person_informations['neighbourhood']
        self.insert_person_params["profession"] = person_informations['profession']

        return {"success": True, "person_registry": mock_persons()}
