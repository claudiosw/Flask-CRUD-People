from faker import Faker
from src.controllers.delete_person_controller import DeletePersonController
from tests.models.spy.person_repository_spy import PersonRepositorySpy

faker = Faker()


def test_delete_person():
    """ Testing registry method """

    person_repo = PersonRepositorySpy()
    delete_person = DeletePersonController(person_repo)

    name = faker.name()

    response = delete_person.run(
        name
    )

    # Testing inputs
    assert person_repo.delete_person_params["name"] == name

    # Testing outputs
    assert response["success"] is True
    assert response["person_registry"]


'''
def test_delete_person_fail():
    """ Testing registry method in fail """

    person_repo = PersonRepositorySpy()
    register_person = DeletePersonController(person_repo)

    name = faker.random_number(digits=2)

    response = register_person.run(
        name
    )

    print(response)

    # Testing inputs
    assert person_repo.insert_person_params == {}

    # Testing outputs
    assert response["success"] is False
'''
