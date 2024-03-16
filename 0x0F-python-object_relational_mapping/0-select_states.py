#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


def list_states(username, password, database_name):
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

    cursor.execute('SELECT * FROM `states`')

    states = cursor.fetchall()

    for state in states:
        print(state)

    # Clear up the cursor and connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    args = sys.argv
    list_states(args[1], args[2], args[3])
