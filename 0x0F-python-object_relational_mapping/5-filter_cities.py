#!/usr/bin/python3
"""
Lists all cities of a state using database hbtn_0e_4_usa
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    query = "SELECT c.name from cities as c \
                INNER JOIN states as s \
                ON c.state_id = s.id \
                WHERE s.name = '{:s}' \
                ORDER BY c.id".format(state)

    cur.execute(query)
    result = cur.fetchall()
    count = 0
    for row in result:
        for value in row:
            count = count + 1
            if count == len(result):
                print(f"{value}")
            else:
                print(f"{value}, ", end="")
    cur.close()
    db.close()
