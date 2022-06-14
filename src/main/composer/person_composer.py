from src.views.person_view import PersonView
from src.controllers.registry_person_controller import RegistryPersonController


def person_composer():
    person_controller = RegistryPersonController()
    person_view = PersonView(person_controller)
    return person_view
