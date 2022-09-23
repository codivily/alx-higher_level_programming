#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ connect to the database """
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')

    """ create a cursor to query the database """
    cur = conn.cursor()
    sql = 'SELECT c.id, c.name, s.name'
    sql += ' FROM cities c LEFT JOIN states s'
    sql += ' ON c.state_id = s.id'
    sql += ' ORDER BY c.id ASC'
    cur.execute(sql)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()