#!/usr/bin/python3
'''Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def state_my_get(s, state_name):
    '''Script that lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa

    Args:
        s (session): the session
        state_name (str): the state name
    '''

    state = s.query(State).filter(State.name == state_name).first()
    if not state:
        print('Not found')
    else:
        print(state.id)


if __name__ == "__main__":
    args = sys.argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state_my_get(session, args[4])

    session.close()
