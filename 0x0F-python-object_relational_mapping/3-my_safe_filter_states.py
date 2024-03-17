#!/usr/bin/python3
'''Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.'''
import sys
import MySQLdb


def display_states_name(username, password, database_name, state_name):
    '''
    List all states from the specified MySQL database hbtn_0e_0_usa.

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

    q = "SELECT *\
        FROM states\
        WHERE name LIKE BINARY %s\
        ORDER BY id ASC"
    cursor.execute(q, (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    # Clear up the cursor and connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    args = sys.argv
    display_states_name(args[1], args[2], args[3], args[4])
