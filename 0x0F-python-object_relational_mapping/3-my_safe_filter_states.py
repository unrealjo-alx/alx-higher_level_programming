#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
