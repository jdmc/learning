import sqlite3

class Agenda:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd

    def crear_tabla_contactos(self):
        conn = sqlite3.connect(self.nombre_bd)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contactos (
                          id INTEGER PRIMARY KEY,
                          nombre TEXT NOT NULL,
                          telefono TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def agregar_contacto(self, nombre, telefono):
        conn = sqlite3.connect(self.nombre_bd)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contactos (nombre, telefono) VALUES (?, ?)', (nombre, telefono))
        conn.commit()
        conn.close()

    def mostrar_contactos(self):
        conn = sqlite3.connect(self.nombre_bd)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contactos')
        contactos = cursor.fetchall()
        conn.close()
        if contactos:
            print("Lista de contactos:")
            for contacto in contactos:
                print(contacto)
        else:
            print("No hay contactos.")

    def ejecutar(self):
        while True:
            print("\nMenú de usuario:")
            print("1. Agregar contacto")
            print("2. Mostrar contactos")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el teléfono del contacto: ")
                self.agregar_contacto(nombre, telefono)
                print("Contacto agregado correctamente.")
            elif opcion == '2':
                self.mostrar_contactos()
            elif opcion == '3':
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

# Uso del programa
agenda = Agenda('agenda.db')
agenda.crear_tabla_contactos()
agenda.ejecutar()
