'''script that lists all State objects from the database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(db):
    '''script that lists all State objects from the database hbtn_0e_6_usa'''

    Session = sessionmaker(bind=db)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    args = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(args[1], args[2], args[3]))
    list_states(engine)
