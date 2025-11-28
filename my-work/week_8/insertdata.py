# insertdata.py
# Author Andrew Beatty, Transcribed by Cathal Redmond 27/Nov/2025

import sqlite3
con = sqlite3.connect("lecture.db") 
cur = con.cursor()

sql = "select * from student"
result = cur.execute(sql)
print (f" first row: {result.fetchone()}")

sql ="insert into student values ('Joe', 'DA', 'Male')"
cur.execute(sql)
con.commit()

sql = "select * from student"
result = cur.execute(sql)
print (f" first row: {result.fetchone()}")

con.close()