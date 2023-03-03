#!/usr/bin/python3
"""
A script that takes in an argument and displays
all values in the states table where name matches
the argument and it's safe from sql injection
"""

import MySQLdb
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'
    port = 3306
    connection = MySQLdb.connect(host=host,
                                 port=port,
                                 user=user,
                                 passwd=passwd,
                                 db=db)
    argument = sys.argv[4]
    db_cursor = connection.cursor()
    command = db_cursor.execute("""SELECT * FROM `states` where `name` = %(argument)s
                                   ORDER BY `id`""", {'argument':argument})
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    connection.close()
