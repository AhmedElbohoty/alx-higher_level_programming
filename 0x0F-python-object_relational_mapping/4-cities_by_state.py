#!/usr/bin/python3
'''Script that lists all cities from the database hbtn_0e_4_usa'''
import sys
import MySQLdb


def display_states_name(username, password, database_name):
    '''
    List all states from the specified MySQL database hbtn_0e_0_usa.

    Args:
        username (str): The user name.
        password (str): The password.
        database_name (str): The database name.

    Returns:
        None
    '''
    connection = MySQLdb.connect(host='localhost', user=username,
                                 passwd=password, db=database_name,
                                 port=3306)

    cursor = connection.cursor()

    q = "SELECT cities.id, cities.name, states.name\
        FROM cities\
        JOIN states\
        ON states.id = cities.state_id\
        ORDER BY cities.id ASC"
    cursor.execute(q)

    states = cursor.fetchall()

    for state in states:
        print(state)

    # Clear up the cursor and connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    args = sys.argv
    display_states_name(args[1], args[2], args[3])
