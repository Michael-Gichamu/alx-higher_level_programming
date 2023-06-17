#!/usr/bin/python3
"""
List all states from database hbtn_0e_0_usa, where
name starts with N

Usage: ./1-filter_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    db.close()
