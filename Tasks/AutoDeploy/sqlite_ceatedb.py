import sqlite3

conn = sqlite3.connect('DockerCodis.db')
cursor = conn.execute('''
CREATE TABLE hostinfo (
     hostid  integer primary key autoincrement,
     hostname text,
     ip       text,
     used     int)''')

conn.commit()
conn.close()
