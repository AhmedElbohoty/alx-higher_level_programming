#!/usr/bin/python3
'''script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa'''
import sys
import MySQLdb


def display_states_name(username, password, database_name, state_name):
    '''
    Lists all cities of that state, using the database hbtn_0e_4_usa

    Args:
        username (str): The user name.
        password (str): The password.
        database_name (str): The database name.
        state_name (str): The state name.

    Returns:
        None
    '''
    connection = MySQLdb.connect(host='localhost', user=username,
                                 passwd=password, db=database_name,
                                 port=3306)

    cursor = connection.cursor()

    q = "SELECT DISTINCT cities.name\
         FROM cities\
         JOIN states\
         ON cities.state_id = states.id\
         WHERE states.name = %s"
    cursor.execute(q, (state_name, ))

    states = cursor.fetchall()
    names = [city[0] for city in states]
    print(*names, sep=", ")

    # Clear up the cursor and connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    args = sys.argv
    display_states_name(args[1], args[2], args[3], args[4])
