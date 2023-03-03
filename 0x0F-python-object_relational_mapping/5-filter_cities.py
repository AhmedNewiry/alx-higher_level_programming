#!/usr/bin/python3
"""
a script that takes in the name of a state as an
argument and lists all cities of that state
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
    db_cursor = connection.cursor()
    argument = sys.argv[4]
    command = db_cursor.execute("""SELECT `c`.`name`from `states` AS s inner
                                   join `cities` AS c ON `s`.`id` =
                                   `c`.`state_id` WHERE `s`.`name` =
                                   %(argument)s ORDER BY `c`.`id`""",
                                {'argument': argument})
    cities = db_cursor.fetchall()
    for i in range(len(cities)):
        if i == len(cities) - 1:
            print(''.join(cities[i]))
        else:    
            print(''.join(cities[i]), end=', ')
    db_cursor.close()
    connection.close()
