from src.views.find_person_view import FindPersonView
from src.controllers.find_person_controller import FindPersonController
from src.models.person_repository import PersonRepository


def find_person_composer():
    person_repository = PersonRepository()
    person_controller = FindPersonController(person_repository)
    person_view = FindPersonView(person_controller)
    return person_view
