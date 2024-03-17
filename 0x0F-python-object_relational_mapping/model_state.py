#!/usr/bin/python3
'''class definition of a State and an instance Base = declarative_base()'''
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    '''
    id: column of an auto-generated, unique integer,
        can’t be null and is a primary key.

    name: column of a string with maximum 128 characters and can’t be null.
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    args = sys.argv
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(args[1], args[2], args[3]))
    Base.metadata.create_all(engine)
