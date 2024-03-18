#!/usr/bin/python3
'''class definition of a State and an instance Base = declarative_base()'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    '''
    id: column of an auto-generated, unique integer,
        can’t be null and is a primary key.

    name: column of a string with maximum 128 characters and can’t be null.
    '''
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
