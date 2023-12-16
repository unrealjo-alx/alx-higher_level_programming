#!/usr/bin/python3
"""
    Script that lists all states from the database hbtn_0e_0_us
"""
import MySQLdb
import sys

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
    query = "SELECT * FROM states"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
