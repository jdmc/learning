import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

sql = "select * from employees"

cursor.execute(sql)

for row in cursor.fetchall():
    print(type(row))
    print(row)


cursor.close()