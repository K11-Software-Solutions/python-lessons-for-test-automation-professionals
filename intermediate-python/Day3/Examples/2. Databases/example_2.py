import sqlite3  
con=sqlite3.connect("enterprise1.db")  
curs=con.cursor()
curs.execute('INSERT INTO zoo VALUES("Duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("Bear", 15, 0.0)')  
con.commit()
curs.close()
con.close()
