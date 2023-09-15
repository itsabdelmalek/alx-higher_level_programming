#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""

import sys
import MySQLdb


def search_states(username, password, db_name, state_name):
    """
    Displays all values in the states table where name matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search.

    Returns:
        None
    """
    try:
        with MySQLdb.connect(user=username, passwd=password, db=db_name) as db:
            cursor = db.cursor()
            cursor.execute(
                "SELECT * FROM states WHERE name = %s ORDER BY id ASC LIMIT 1",
                (state_name,)
            )
            state = cursor.fetchone()
            if state:
                print(state)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, db_name, state_name)
