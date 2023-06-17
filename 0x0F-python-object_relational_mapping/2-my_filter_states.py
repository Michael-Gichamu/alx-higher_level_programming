#!/usr/bin/python3
"""
Displays all values in states table of hbtn_0e_0_usa
where name matches the argument.

Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(state_name)

    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
