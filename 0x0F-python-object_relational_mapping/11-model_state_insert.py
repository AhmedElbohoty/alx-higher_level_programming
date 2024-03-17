#!/usr/bin/python3
'''Script adds the State object “Louisiana” to the database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def state_insert(s):
    '''Script that lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa

    Args:
        s (session): the session
    '''

    new_state = State(name='Louisiana')
    s.add(new_state)
    s.commit()
    print(new_state.id)


if __name__ == "__main__":
    args = sys.argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state_insert(session)

    session.close()
