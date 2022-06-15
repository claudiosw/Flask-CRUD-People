from typing import List
from sqlalchemy.orm.exc import NoResultFound
from .entities import PersonsModel
from .config import DBConnectionHandler
from .tuples import PersonsTuple


class PersonRepository:
    """ Class to manage Person Repository """

    def insert_person(self, name: str, age: int, neighbourhood: str, profession: str) -> PersonsTuple:
        """insert data in person entity
        :param  - name: person's name
                - age: person's age
                - neighbourhood: person's neighbourhood
                - profession: person's profession
        :return - tuple with new person inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_person = PersonsModel(name=name, age=age, neighbourhood=neighbourhood, profession=profession)
                db_connection.session.add(new_person)
                db_connection.session.commit()

                return PersonsTuple(
                    id=new_person.id,
                    name=new_person.name,
                    age=new_person.age,
                    neighbourhood=new_person.neighbourhood,
                    profession=new_person.profession
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    def select_person(self, name: str = None) -> List[PersonsTuple]:
        """
        Select data in person entity by name
        :param - name: person's name
        :return - List with Persons selected
        """

        try:

            if name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PersonsModel)
                        .filter_by(name=name)
                        .one()
                    )

                return PersonsTuple(
                    id=data.id,
                    name=data.name,
                    age=data.age,
                    neighbourhood=data.neighbourhood,
                    profession=data.profession
                )

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
