import sqlite3

base = sqlite3.connect('college.db')
cur = base.cursor()

r = cur.execute('SELECT * FROM Matherboards').fetchall()
print(r)