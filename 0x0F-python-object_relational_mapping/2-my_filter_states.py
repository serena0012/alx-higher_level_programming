#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""
if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

import MySQLdb
from sys import argv
db = MySQLdb.connect(host='localhost', port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3])

cur = db.cursor()
cur.execute("SELECT * \
               FROM states \
               WHERE name LIKE BINARY '{}' \
               ORDER BY states.id ASC".format(argv[4]))

lines = cur.fetchall()
for line in lines:
    print(line)
