from src.views.person_view import PersonView
from src.controllers.registry_person_controller import RegistryPersonController
from src.views.find_person_view import FindPersonView
from src.controllers.find_person_controller import FindPersonController
from src.controllers.update_person_controller import UpdatePersonController
from src.models.person_repository import PersonRepository


def person_composer():
    person_repository = PersonRepository()
    person_controller = RegistryPersonController(person_repository)
    person_view = PersonView(person_controller)
    return person_view


def find_person_composer():
    person_repository = PersonRepository()
    person_controller = FindPersonController(person_repository)
    person_view = FindPersonView(person_controller)
    return person_view


def update_person_composer():
    person_repository = PersonRepository()
    person_controller = UpdatePersonController(person_repository)
    person_view = PersonView(person_controller)
    return person_view
