#!/usr/bin/python3
""" a script that lists all states from the database"""

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
    db_cursor = connection.cursor()
    db_cursor.execute("""SELECT * FROM `states` ORDER BY `id`""")
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    connection.close()
