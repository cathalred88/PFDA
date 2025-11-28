#getall.py
#author Andrew Beatty, Transcribed by Cathal Redmond 27/Nov/2025 

import sqlite3
con = sqlite3.connect("lecture.db") 
cur = con.cursor()

sql = "select * from student"
result = cur.execute(sql)
for row in result.fetchall():
    print(row)
