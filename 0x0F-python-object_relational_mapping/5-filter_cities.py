#!/usr/bin/python3
"""Usage: 0-select_states.py <mysql_user> <mysql_pass> <db_name>"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    state = argv[4].split(';')[0]
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM cities\
                WHERE state_id = (\
                SELECT id FROM states\
                WHERE name = '{state}')")
    query_rows = cur.fetchall()
    comma = ''
    for row in query_rows:
        print(f"{comma}{row[0]}", end='')
        comma = ', '
    print()
    cur.close()
    conn.close()
