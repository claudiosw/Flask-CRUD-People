from src.views.registry_person_view import RegistryPersonView
from src.controllers.registry_person_controller import RegistryPersonController
from src.models.person_repository import PersonRepository


def registry_person_composer():
    person_repository = PersonRepository()
    person_controller = RegistryPersonController(person_repository)
    person_view = RegistryPersonView(person_controller)
    return person_view
