from faker import Faker
from src.views.registry_person_view import RegistryPersonView
from tests.controllers.spy.person_controller_spy import RegisterPersonControllerSpy
from src.views.http_types.http_request import HttpRequest

faker = Faker()


def test_register_person_view():
    """ Testing registry method """

    attributes = {
        "name": faker.name(),
        "age": faker.random_number(digits=2),
        "neighbourhood": faker.city(),
        "profession": faker.job()
    }
    http_request = HttpRequest(None, attributes)
    register_person_controller = RegisterPersonControllerSpy()
    register_person = RegistryPersonView(register_person_controller)

    response = register_person.handle(
        http_request
    )

    # Testing inputs
    assert register_person_controller.insert_person_params["name"] == attributes["name"]

    # Testing outputs
    assert response.status_code == 200
    assert response.body["response"]


'''
def test_register_person_fail():
    """ Testing registry method in fail """

    person_repo = PersonRepositorySpy()
    register_person = RegistryPersonController(person_repo)

    attributes = {
        "name": faker.name(),
        "age": faker.name()
    }

    response = register_person.run(
        attributes
    )

    print(response)

    # Testing inputs
    assert person_repo.insert_person_params == {}

    # Testing outputs
    assert response["success"] is False'''
