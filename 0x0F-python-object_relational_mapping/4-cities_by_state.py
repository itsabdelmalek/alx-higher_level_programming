#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
"""

import sys
import MySQLdb

def list_cities_by_state(username, password, db_name):
    """
    Lists all cities of the database hbtn_0e_4_usa, ordered by city id.

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
                "SELECT c.id, c.name, s.name "
                "FROM cities c "
                "INNER JOIN states s "
                "ON c.state_id = s.id "
                "ORDER BY c.id"
            )
            cities = cursor.fetchall()
            [print(city) for city in cities]
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities_by_state(username, password, db_name)
