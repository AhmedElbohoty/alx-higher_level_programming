#!/usr/bin/python3
# Defines a State model.
# Inherits from SQLAlchemy Base and links to the MySQL table states.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    '''
    id: column of an auto-generated, unique integer,
        can’t be null and is a primary key.

    name: column of a string with maximum 128 characters and can’t be null.
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
