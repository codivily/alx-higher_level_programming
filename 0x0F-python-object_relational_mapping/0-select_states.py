#!/usr/bin/env python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    [user, passwd, db] = sys.argv[1:]

    conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset='utf8')

    cur = conn.cursor()
    cur.execute('SELECT id, name FROM states ORDER BY id ASC')
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
