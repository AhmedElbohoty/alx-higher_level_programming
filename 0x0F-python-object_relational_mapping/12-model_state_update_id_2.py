#!/usr/bin/python3
'''Script that changes the name of a State object from the database
hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def state_update_id(s):
    '''Script that changes the name of a State object from the database
    hbtn_0e_6_usa

    Args:
        s (session): the session
    '''

    state = s.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    s.commit()


if __name__ == "__main__":
    args = sys.argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state_update_id(session)

    session.close()
