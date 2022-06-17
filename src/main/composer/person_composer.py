from src.views.registry_person_view import RegistryPersonView
from src.views.update_person_view import UpdatePersonView
from src.controllers.registry_person_controller import RegistryPersonController
from src.views.find_person_view import FindPersonView
from src.views.delete_person_view import DeletePersonView
from src.controllers.find_person_controller import FindPersonController
from src.controllers.update_person_controller import UpdatePersonController
from src.controllers.delete_person_controller import DeletePersonController
from src.models.person_repository import PersonRepository


def person_composer():
    person_repository = PersonRepository()
    person_controller = RegistryPersonController(person_repository)
    person_view = RegistryPersonView(person_controller)
    return person_view


def find_person_composer():
    person_repository = PersonRepository()
    person_controller = FindPersonController(person_repository)
    person_view = FindPersonView(person_controller)
    return person_view


def update_person_composer():
    person_repository = PersonRepository()
    person_controller = UpdatePersonController(person_repository)
    person_view = UpdatePersonView(person_controller)
    return person_view


def delete_person_composer():
    person_repository = PersonRepository()
    person_controller = DeletePersonController(person_repository)
    person_view = DeletePersonView(person_controller)
    return person_view
