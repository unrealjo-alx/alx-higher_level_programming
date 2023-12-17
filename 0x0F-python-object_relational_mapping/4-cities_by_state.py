#!/usr/bin/python3
"""
    Script that lists all cities from the database hbtn_0e_4_usa.
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

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON states.id = cities.state_id "
        "ORDER BY cities.id ASC;"
    )
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
