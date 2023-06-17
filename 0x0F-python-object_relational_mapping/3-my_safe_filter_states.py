#!/usr/bin/python3
"""
Displays all value in the states table of hbtn_0e_0_usa
where name matches the argument.

Use of parameterized queries with placeholders to protect
against SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cur.execute(query, (state_name,))

    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()
