#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def list_states_starting_with_n(username, password, db_name):
    """
    Lists all states with a name starting with N from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
    try:
        with MySQLdb.connect(user=username, passwd=password, db=db_name) as db:
            cursor = db.cursor()
            cursor.execute(
                "SELECT * FROM states WHERE id IN "
                "(SELECT MIN(id) FROM states "
                "WHERE name LIKE 'N%' GROUP BY name) "
                "ORDER BY id ASC"
            )
            states = cursor.fetchall()
            [print(state) for state in states]
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states_starting_with_n(username, password, db_name)
