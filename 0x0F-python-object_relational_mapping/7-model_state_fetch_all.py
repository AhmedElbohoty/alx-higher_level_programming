'''script that lists all State objects from the database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(engine):
    '''script that lists all State objects from the database hbtn_0e_6_usa'''

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for ind, state in enumerate(states):
        print(f'{ind}: {state.name}')

    session.close()


if __name__ == "__main__":
    args = sys.argv
    engine = create_engine(
        f'mysql://{args[1]}:{args[2]}@localhost:3306/{args[3]}')
    list_states(engine)
