#!/usr/bin/python3
'''Script that lists all City objects from the database hbtn_0e_101_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


def relationship_cities_states_list(s):
    '''Script that lists all City objects from the database hbtn_0e_101_usa'''

    citites = s.query(City).order_by(City.id)
    for city in citites:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    relationship_cities_states_list(session)
