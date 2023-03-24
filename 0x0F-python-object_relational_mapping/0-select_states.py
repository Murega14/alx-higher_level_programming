#!/usr/bin/python3
"""
This script lists all states from the database"""


import MySQLdb
import sys

if __name__ == '__main__':
    """
    Accesses the database to get the states"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'states'")
    [print(state) for state in c.fetchall()]
