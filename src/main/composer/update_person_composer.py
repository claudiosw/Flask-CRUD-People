from src.views.update_person_view import UpdatePersonView
from src.controllers.update_person_controller import UpdatePersonController
from src.models.person_repository import PersonRepository


def update_person_composer():
    person_repository = PersonRepository()
    person_controller = UpdatePersonController(person_repository)
    person_view = UpdatePersonView(person_controller)
    return person_view
