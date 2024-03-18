#!/usr/bin/python3
'''Prints all City objects from the database'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def city_fetch_by_state(s):
    '''Prints all City objects from the database

    Args:
        s (session): the session
    '''

    result = s.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    args = sys.argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    city_fetch_by_state(session)

    session.close()
