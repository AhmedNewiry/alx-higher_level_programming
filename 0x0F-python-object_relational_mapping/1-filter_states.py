#!/usr/bin/python3
""" a script that lists all states with
    the name starting with capital letter N
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
	command = db_cursor.execute("""SELECT * FROM `states` where `name` LIKE BINARY 'N%' ORDER BY `id`""")
	states = command.fetchall()
	for state in states:
		print state
    db_cursor.close()
    connection.close()