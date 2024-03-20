import sqlite3

connection = sqlite3.connect('empleados.db')

cursor = connection.cursor()

id_empleado = input("Ingrese el id del empleado: ")

sql = "UPDATE employees SET department = 'IT' WHERE id = ?;"
cursor.execute(sql, (id_empleado,))

connection.commit() #consolidar la operacion
connection.close()
