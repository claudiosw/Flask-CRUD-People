from faker import Faker
from src.controllers.registry_person_controller import RegistryPersonController
from tests.models.spy.person_repository_spy import PersonRepositorySpy

faker = Faker()


def test_register():
    """ Testing registry method """

    person_repo = PersonRepositorySpy()
    register_person = RegistryPersonController(person_repo)

    attributes = {
        "name": faker.name(),
        "age": faker.random_number(digits=2),
        "neighbourhood": faker.city(),
        "profession": faker.job()
    }

    response = register_person.registry(
        attributes
    )

    # Testing inputs
    assert person_repo.insert_person_params["name"] == attributes["name"]

    # Testing outputs
    assert response["success"] is True
    assert response["person_registry"]


def test_register_fail():
    """ Testing registry method in fail """

    person_repo = PersonRepositorySpy()
    register_person = RegistryPersonController(person_repo)

    attributes = {
        "name": faker.name(),
        "age": faker.name()
    }

    response = register_person.registry(
        attributes
    )

    print(response)

    # Testing inputs
    assert person_repo.insert_person_params == {}

    # Testing outputs
    assert response["success"] is False
    # assert response["person_registry"] is None
