from sqlalchemy import Column, String, Integer
from src.models.config import Base


class PersonsModel(Base):
    """ Persons Model """

    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=True)
    neighbourhood = Column(String, nullable=True)
    profession = Column(String, nullable=True)

    def __repr__(self):
        return f"Person [name={self.name}]"
