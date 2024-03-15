import sqlite3


class AppContactos:

    def __init__(self) -> None:
        #conectar con la base de datos
        self.conn = sqlite3.connect('contactos.db')
        self.cursor = self.conn.cursor()

        #Crear la tabla de contactos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT NOT NULL)
        ''')
        self.conn.commit() #consolidacion

    def agregar_contacto(self):
        nombre = input('Nombre: ')
        telefono = input('Telefono: ')
        email = input('Email: ')

        if nombre and telefono and email:
            self.cursor.execute('''
                INSERT INTO contactos (nombre, telefono, email)
                VALUES (?, ?, ?)
            ''', (nombre, telefono, email))
            
            self.conn.commit()
            print('Contacto guardado')
        else:
            print('Falta algun campo por informar')
    
    def mostrar_contactos(self):
        self.cursor.execute('SELECT * FROM contactos')
        contactos = self.cursor.fetchall()

        for contacto in contactos:
            print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Telefono: {contacto[2]}, Email: {contacto[3]}")

        
    def ejecutar(self):
        """Presentar menu de usuario que permita las opciones:
        1.- Agregar contacto
        2.- Mostrar contactos
        3.- Salir
        """
        while True:
            print('\n----Menu app de contactos----')
            print("1.- Agregar contacto")
            print("2.- Mostrar contactos")
            print("3.- Salir")

            opcion = input('Opción: ')

            match opcion: 
                case "1":
                    self.agregar_contacto()
                case "2":
                    self.mostrar_contactos()
                case "3":
                    break
                case _:
                    print('Opción no válida')  
            
            """ if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.mostrar_contactos()
            elif opcion == "3":
                break 
            else:
                print('Opción no válida')  
            """


        

db_app = AppContactos()
db_app.ejecutar()