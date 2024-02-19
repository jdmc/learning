""" La construcción with open() en Python se utiliza para abrir un archivo y asegurar que se cierre correctamente después de que se termine de usar, incluso si ocurren excepciones durante la ejecución.

La sintaxis general es la siguiente:

with open(nombre_archivo, modo) as variable:
    # código para trabajar con el archivo usando la variable
Donde:

nombre_archivo = nombre del archivo que se va a abrir.
modo = modo en que se abrirá el archivo ('r' para lectura, 'w' para escritura, 'a' para añadir, 'r+' para lectura y escritura, etc.).
variable = nombre de la variable que se utilizará para hacer referencia al archivo dentro del bloque with.

El uso de with garantiza que el archivo se cierre correctamente al salir del bloque with, lo que es útil porque libera recursos y previene posibles problemas si se olvida cerrar el archivo manualmente. Además, with maneja automáticamente las excepciones que puedan ocurrir dentro del bloque, asegurándose de que el archivo se cierre incluso si se produce un error.

En resumen, with open() es una forma conveniente y segura de trabajar con archivos en Python. """

import os

script_directory = os.path.dirname(__file__) # gestionar ruta de app.py

def sanitizar_cadena(cadena: str) -> str: # devolvemos cadena de entrada limpia
    return cadena.strip() #quita elementos espacio, tabs, etc de izq  a derech si solo derecha "rstrip" / solo izq "lstrip"

def sanitizar_data( data: list) -> list: #1 uso de la tec > CEBOLLA de dentro a fuera
    data_limpia = list() #3
    for cadena in data: #2
        sanitizar_cadena(cadena)
        data_limpia.append(sanitizar_cadena(cadena)) #4
    else: #5
        return data_limpia

def escribir_data(nombre_fichero: str, *mensajes):
    #with open(f'./sesion8/data/{nombre_fichero}', 'w') as f:
    with open(f'{script_directory}/data/{nombre_fichero}', 'w') as f:
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")
    


def leer_data(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        #with open(f"./sesion8/data/{nombre_fichero}", 'r') as f:
        with open(f"{script_directory}/data/{nombre_fichero}", 'r') as f:
            data = sanitizar_data(f.readlines())

    except FileNotFoundError as fnfex:
        print(fnfex)
    
    return data

#crear una lista de tuplas formadas por el nombre y el apellido
""" 
  # Abrir el fichero en modo lectura
fichero = open("./data/alumnos.txt", "r")

  # Leer el contenido del fichero
contenido = fichero.read()
  
    # Cerrar el fichero
fichero.close()

# Dividir el contenido del fichero en una lista de cadenas
lista_cadenas = contenido.split("\n")

# Convertir la lista de cadenas en una lista de tuplas
lista_tuplas = [(nombre, apellido) for nombre, apellido in map(lambda cadena: cadena.split(","), lista_cadenas)]

print(lista_tuplas) """

#gonzalo congetension
# return [tuple(nombre.split()) for nombre in data]

# Ricardo >> TRANSFORMERS





