import sqlite3  
connect=sqlite3.connect("enterprise1.db")  
curs = connect.cursor()
curs.execute("""CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY,	
count INT, damages FLOAT)""")
curs.close()  
connect.close()
