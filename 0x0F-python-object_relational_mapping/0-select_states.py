#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=username,
                     passwd=password, db=database)
cursor = db.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)
cursor.close()
db.close()
