#!/usr/bin/python3
'''script that prints the first State object from database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    args = sys.argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).order_by(State.id).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    session.close()
