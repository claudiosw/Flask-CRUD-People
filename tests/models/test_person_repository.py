from faker import Faker
from src.models.config import DBConnectionHandler
from src.models.person_repository import PersonRepository
from src.models.entities import PersonsModel

faker = Faker()
person_repository = PersonRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_person():
    """ Should Insert Person """

    name = faker.name()
    age = faker.random_number(digits=2)
    neighbourhood = faker.city()
    profession = faker.job()

    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_person = person_repository.insert_person(name, age, neighbourhood, profession)
    query_person = engine.execute(
        f"SELECT * FROM persons WHERE id='{new_person.id}';"
    ).fetchone()

    engine.execute(f"DELETE FROM persons WHERE id='{new_person.id}'")

    assert new_person.id == query_person.id
    assert new_person.name == query_person.name


def test_select_person():
    """ Should select a person in Persons table and compare it """

    person_id = faker.random_number(digits=5)
    name = faker.name()
    age = faker.random_number(digits=2)
    neighbourhood = faker.city()
    profession = faker.job()
    data = PersonsModel(id=person_id, name=name, age=age, neighbourhood=neighbourhood, profession=profession)

    engine = db_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO persons (id, name, age, neighbourhood, profession) \
        VALUES ('{person_id}','{name}', {age}, '{neighbourhood}', '{profession}');"
    )

    query_person1 = person_repository.select_person(name=name)

    assert data.name == query_person1[0].name

    engine.execute(f"DELETE FROM persons WHERE id='{person_id}';")
