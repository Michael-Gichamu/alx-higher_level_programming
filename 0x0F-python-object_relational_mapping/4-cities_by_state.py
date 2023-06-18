#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa

Usage: ./4-cities_by_state.py <mysql username>
                                <mysql password>
                                <database name>
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    query = "SELECT c.id, c.name, s.name \
                FROM cities as c \
                INNER JOIN states as s \
                ON c.state_id = s.id \
                ORDER BY c.id"

    cur.execute(query)

    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
