from faker import Faker
from src.controllers.update_person_controller import UpdatePersonController
from tests.models.spy.person_repository_spy import PersonRepositorySpy

faker = Faker()


def test_update_person():
    """ Testing registry method """

    person_repo = PersonRepositorySpy()
    update_person = UpdatePersonController(person_repo)

    attributes = {
        "name": faker.name(),
        "age": faker.random_number(digits=2),
        "neighbourhood": faker.city(),
        "profession": faker.job()
    }

    response = update_person.run(
        attributes
    )

    # Testing inputs
    assert person_repo.update_person_params["name"] == attributes["name"]

    # Testing outputs
    assert response["success"] is True
    assert response["person_registry"]


'''
def test_update_person_fail():
    """ Testing registry method in fail """

    person_repo = PersonRepositorySpy()
    register_person = UpdatePersonController(person_repo)

    attributes = {
        "name": faker.name(),
        "age": faker.name()
    }

    response = register_person.run(
        attributes
    )

    print(response)

    # Testing inputs
    assert person_repo.update_person_params == {}

    # Testing outputs
    assert response["success"] is False'''
