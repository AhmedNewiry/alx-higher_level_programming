#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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
    command = db_cursor.execute("""SELECT `c`.`id`, `c`.`name`, `s`.`name`
                                   from `states` AS s inner join `cities`
                                   AS c ON `s`.`id` = `c`.`state_id`
                                   ORDER BY `c`.`id`""")
    cities = db_cursor.fetchall()
    for city in cities:
        print(city)
    db_cursor.close()
    connection.close()
