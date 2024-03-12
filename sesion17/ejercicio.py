import sqlite3

class Agenda:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd

    def crear_tabla_contactos(self):
        # Conectarse a la base de datos
        conn = sqlite3.connect(self.nombre_bd)
        # Crear un cursor
        cursor = conn.cursor()
        # Crear la tabla de contactos si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS contactos (
                          id INTEGER PRIMARY KEY,
                          nombre TEXT NOT NULL,
                          telefono TEXT NOT NULL)''')
        # Confirmar los cambios
        conn.commit()
        # Cerrar la conexión
        conn.close()

    def agregar_contacto(self, nombre, telefono):
        # Conectarse a la base de datos
        conn = sqlite3.connect(self.nombre_bd)
        # Crear un cursor
        cursor = conn.cursor()
        # Insertar el nuevo contacto en la tabla
        cursor.execute('INSERT INTO contactos (nombre, telefono) VALUES (?, ?)', (nombre, telefono))
        # Confirmar los cambios
        conn.commit()
        # Cerrar la conexión
        conn.close()

    def mostrar_contactos(self):
        # Conectarse a la base de datos
        conn = sqlite3.connect(self.nombre_bd)
        # Crear un cursor
        cursor = conn.cursor()
        # Obtener todos los contactos de la tabla
        cursor.execute('SELECT * FROM contactos')
        contactos = cursor.fetchall()
        # Cerrar la conexión
        conn.close()
        # Mostrar los contactos
        if contactos:
            print("Lista de contactos:")
            for contacto in contactos:
                print(contacto)
        else:
            print("No hay contactos.")

    def ejecutar(self):
        while True:
            # Mostrar el menú de usuario
            print("\nMenú de usuario:")
            print("1. Agregar contacto")
            print("2. Mostrar contactos")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                # Agregar un nuevo contacto
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el teléfono del contacto: ")
                self.agregar_contacto(nombre, telefono)
                print("Contacto agregado correctamente.")
            elif opcion == '2':
                # Mostrar todos los contactos
                self.mostrar_contactos()
            elif opcion == '3':
                # Salir del programa
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

# Uso del programa
agenda = Agenda('agenda.db')
agenda.crear_tabla_contactos()
agenda.ejecutar()

