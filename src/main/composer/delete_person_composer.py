from src.views.delete_person_view import DeletePersonView
from src.controllers.delete_person_controller import DeletePersonController
from src.models.person_repository import PersonRepository


def delete_person_composer():
    person_repository = PersonRepository()
    person_controller = DeletePersonController(person_repository)
    person_view = DeletePersonView(person_controller)
    return person_view
