#!/usr/bin/python3
'''Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa '''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


def relationship_states_cities_list(s):
    '''Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa '''

    states = s.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    relationship_states_cities_list(session)