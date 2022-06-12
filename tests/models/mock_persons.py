
from faker import Faker
from src.models.tuples import PersonsTuple

faker = Faker()


def mock_persons() -> PersonsTuple:
    """ Mocking Persons """

    return PersonsTuple(
        id=faker.random_number(digits=5),
        name=faker.name(),
        age=faker.random_number(digits=2),
        neighbourhood=faker.city(),
        profession=faker.job()
    )
