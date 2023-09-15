#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def list_cities_by_state(username, password, db_name, state_name):
    """
    Lists all cities of a specific state from the database hbtn_0e_4_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name of the state.

    Returns:
        None
    """
    try:
        with MySQLdb.connect(user=username, passwd=password, db=db_name) as db:
            cursor = db.cursor()
            cursor.execute(
                "SELECT DISTINCT cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.name ASC",
                (state_name,)
            )
            cities = cursor.fetchall()
            print(", ".join(city[0] for city in cities))
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

    list_cities_by_state(username, password, db_name, state_name)
