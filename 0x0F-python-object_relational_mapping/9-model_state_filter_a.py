#!/usr/bin/python3
'''Script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def state_filter_a(s):
    '''Script that lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa

    Args:
        s (session)
    '''

    states = s.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()
    if states is not None:
        for state in states:
            print('{}: {}'.format(state.id, state.name))


if __name__ == "__main__":
    args = sys.argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state_filter_a(session)

    session.close()
