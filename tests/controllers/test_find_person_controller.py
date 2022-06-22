from faker import Faker
from src.controllers.find_person_controller import FindPersonController
from tests.models.spy.person_repository_spy import PersonRepositorySpy

faker = Faker()


def test_find_person():
    """ Testing find controller """

    person_repo = PersonRepositorySpy()
    find_person = FindPersonController(person_repo)

    name = faker.name()

    response = find_person.run(
        name
    )

    # Testing inputs
    assert person_repo.select_person_params["name"] == name

    # Testing outputs
    assert response["success"] is True
    assert response["person_registry"]


'''
def test_find_person_fail():
    """ Testing find controller in fail """

    person_repo = PersonRepositorySpy()
    find_person = FindPersonController(person_repo)

    name = faker.random_number(digits=2)

    response = find_person.run(
        name
    )

    print(response)

    # Testing inputs
    assert person_repo.select_person_params == {}

    # Testing outputs
    assert response["success"] is False
'''
