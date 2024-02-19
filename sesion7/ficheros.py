#ficheros


""" Los Ficheros en Python
En Python, un fichero es un conjunto de datos almacenados en un dispositivo de almacenamiento, como un disco duro o una memoria USB. 
Los ficheros se pueden usar para almacenar una gran variedad de información, como texto, código, imágenes, audio y video.

Python proporciona una serie de herramientas para trabajar con ficheros. Estas herramientas te permiten:

Abrir y cerrar ficheros.
Leer y escribir datos en ficheros.
Mover y eliminar ficheros.
Cambiar los permisos de los ficheros.
Los ficheros se pueden clasificar en dos tipos:

Ficheros de texto: Contienen texto plano, como código fuente, documentos o páginas web.
Ficheros binarios: Contienen datos binarios, como imágenes, audio o video.
Para trabajar con ficheros en Python, se utilizan las siguientes funciones:

open(): Abre un fichero y devuelve un objeto de fichero.
read(): Lee datos de un fichero.
write(): Escribe datos en un fichero.
close(): Cierra un fichero.

* Ventajas:
Almacenamiento permanente: Los datos almacenados en ficheros se conservan incluso después de cerrar el programa.
Acceso rápido: Los ficheros permiten acceder a los datos de forma rápida y eficiente.
Compartición de datos: Los ficheros se pueden compartir fácilmente con otros programas o usuarios.
Reutilización de datos: Los datos almacenados en ficheros se pueden reutilizar en diferentes programas.

* Desventajas:
Complejidad: Trabajar con ficheros puede ser más complejo que trabajar con datos en memoria.
Eficiencia: El acceso a datos en ficheros puede ser menos eficiente que el acceso a datos en memoria.
Seguridad: Los ficheros pueden ser vulnerables a ataques de seguridad.

* Cuándo usar ficheros:
Cuando necesitas almacenar datos de forma permanente.
Cuando necesitas acceder a datos de forma rápida y eficiente.
Cuando necesitas compartir datos con otros programas o usuarios.
Cuando necesitas reutilizar datos en diferentes programas.

* Ejemplos de cuándo usar ficheros:
Almacenar la configuración de un programa.
Almacenar datos de usuario.
Almacenar imágenes, audio o video.
Intercambiar datos con otros programas.

* En resumen, los ficheros son una herramienta poderosa que te permite almacenar y recuperar datos de forma permanente. 
Sin embargo, es importante tener en cuenta las ventajas y desventajas de usar ficheros antes de decidir si son la mejor opción para tu programa. """

def escribir_data(nombre_fichero: str, *mensajes):
    f = open(f'./data/{nombre_fichero}', 'w')
    for mensaje in mensajes:
        f.write(f"{mensaje}\n")
    
    f.close()


def escribir_data_v2(nombre_fichero: str, *mensajes):
    with open(f'./data/{nombre_fichero}', 'w') as f:
        for mensaje in mensajes:
            f.write(f"{mensaje}\n")
            
"""  
Cuando asignamos "None" a una variable en Python, estamos indicando que la variable no tiene ningún valor. 
None es un tipo de datos en Python que representa la ausencia de valor o la falta de definición de un valor. 
Es similar a null en otros lenguajes de programación.   """         
    
def leer_data(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        f = open(f"./data/{nombre_fichero}", 'r')
        data = f.read()
    except Exception as fnfex:
        print(fnfex)
    finally:
        if f:
            f.close()

    return data

""" 
Usamos None en varias situaciones:

*Para inicializar variables que más tarde se asignarán a un valor específico.
*Como un valor de retorno para indicar que una función no devuelve ningún resultado.
*Como un valor predeterminado para un argumento de función para indicar que no se ha proporcionado ningún valor.

Es importante tener en cuenta que None es un valor que evalúa a False en contextos booleanos, 
lo que significa que si evaluamos una variable que contiene None en un contexto booleano, el resultado será False. """

def leer_data_v2(nombre_fichero: str) -> str:

    f = None
    data = None
    try:
        with open(f"./data/{nombre_fichero}", 'r') as f:
            data = f.read()

    except FileNotFoundError as fnfex:
        print(fnfex)
    
    return data

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