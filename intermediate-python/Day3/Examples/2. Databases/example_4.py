import sqlite3  
conn = sqlite3.connect('enterprise1.db')  
c = conn.cursor()
data3 = str(input('Please enter name: '))
mydata = c.execute('DELETE FROM zoo WHERE Name=?', (data3))
conn.commit()
c.close
