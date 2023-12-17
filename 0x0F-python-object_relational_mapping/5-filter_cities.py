#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) < 5:
        sys.exit(0)

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
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "WHERE states.name = %s ORDER BY states.id ASC"
    )
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()

    len_result = len(result)
    for i in range(len_result):
        if i < len_result - 1:
            print(result[i][0], end=", ")
        else:
            print(result[i][0])

    cursor.close()
    db.close()
