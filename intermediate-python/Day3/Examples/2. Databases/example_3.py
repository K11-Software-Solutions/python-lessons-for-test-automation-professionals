import sqlite3  
connect=sqlite3.connect("enterprise1.db")  
curs=connect.cursor()

for row in curs.execute("SELECT * FROM zoo"):
    print(row)

curs.close()
connect.close()
