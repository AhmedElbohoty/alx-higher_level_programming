'''script that lists all State objects from the database hbtn_0e_6_usa'''
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
