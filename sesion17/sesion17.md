# Files

En Python, los archivos son objetos que representan archivos en el sistema de archivos de la computadora. Estos archivos pueden ser de diferentes tipos, como archivos de texto, archivos binarios, archivos CSV, archivos JSON, etc. Los archivos en Python son utilizados para leer datos desde archivos externos, escribir datos en archivos, manipular archivos existentes, entre otras operaciones relacionadas con archivos.

Aquí hay una breve descripción de algunos tipos de archivos comunes en Python y cómo se utilizan:

ZIP utilizando el módulo **zipfile**: Este módulo te permite crear, leer, escribir y extraer archivos ZIP.

```python

import zipfile

# Nombre del archivo ZIP
archivo_zip = 'archivo.zip'

# Abre el archivo ZIP en modo de lectura
with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
    # Lista los contenidos del archivo ZIP
    contenidos = zip_ref.namelist()
    print("Contenidos del archivo ZIP:", contenidos)

    # Extrae todos los archivos en el directorio actual
    zip_ref.extractall()
    print("Archivos extraídos correctamente.")

```
En este ejemplo:

* Importamos el módulo zipfile.
* Especificamos el nombre del archivo ZIP que queremos manipular.
* Abrimos el archivo ZIP en modo de lectura utilizando ZipFile y el contexto with.
* Utilizamos el método namelist() para obtener una lista de todos los archivos y directorios contenidos en el archivo ZIP.
* Utilizamos el método extractall() para extraer todos los archivos y directorios del archivo ZIP en el directorio actual.

Además de leer archivos ZIP, también puedes crear nuevos archivos ZIP, agregar archivos a archivos ZIP existentes, eliminar archivos de archivos ZIP, entre otras operaciones, utilizando las funciones proporcionadas por el módulo zipfile.

**Archivos de texto**: Estos son archivos que contienen texto sin formato. Se pueden leer y escribir utilizando funciones como open(), read(), write(), etc.

```python
# Ejemplo de lectura de un archivo de texto
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)

```

**Archivos binarios**: Estos son archivos que contienen datos binarios en lugar de texto. Se utilizan para almacenar datos que no son texto, como imágenes, videos, archivos ejecutables, etc. Se pueden leer y escribir de manera similar a los archivos de texto, pero con diferentes modos de apertura (rb para leer en modo binario, wb para escribir en modo binario, etc.).

```python
# Ejemplo de lectura de un archivo binario
with open('imagen.png', 'rb') as archivo:
    contenido = archivo.read()

```

**Archivos CSV (Comma-Separated Values)**: Son archivos que contienen datos tabulares, donde los valores están separados por comas u otros delimitadores. Python proporciona el módulo csv para leer y escribir archivos CSV de manera fácil y eficiente.

```python
import csv

# Ejemplo de lectura de un archivo CSV
with open('datos.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)

```

**Archivos JSON (JavaScript Object Notation)**: Son archivos que contienen datos en formato JSON. Python proporciona el módulo json para leer y escribir archivos JSON.

```python
import json

# Ejemplo de lectura de un archivo JSON
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
print(datos)

```

### Cuando usar archivos en Python:

* Usar archivos cuando necesitas leer o escribir datos de manera persistente en el disco.
* Para almacenar configuraciones de la aplicación.
* Para procesar grandes conjuntos de datos que no caben en la memoria.
* Para interactuar con otros programas que utilizan archivos como medio de comunicación.

Es importante tener en cuenta las buenas prácticas al trabajar con archivos en Python, como cerrar correctamente los archivos después de su uso (preferiblemente utilizando la declaración **'with'**) y manejar adecuadamente las excepciones que puedan ocurrir durante la lectura o escritura de archivos.

## Context manager

Un context manager en Python es un objeto que se utiliza para administrar un contexto, es decir, una serie de acciones que se deben realizar antes y después de una operación principal. Los context managers son comúnmente utilizados para manejar recursos como archivos, conexiones de red o bases de datos, garantizando que se realicen operaciones importantes como la apertura y el cierre de recursos de manera segura y eficiente.

En Python, los context managers se implementan utilizando dos métodos especiales: \__enter__() y \__exit__(). Cuando un objeto actúa como un context manager, el método \__enter__() se llama automáticamente al entrar en el bloque de contexto (por ejemplo, utilizando una declaración with), y el método \__exit__() se llama automáticamente al salir del bloque de contexto. Esto permite que el context manager realice acciones de inicialización antes de que comience el bloque de contexto y acciones de limpieza después de que el bloque de contexto haya finalizado, incluso si ocurre una excepción dentro del bloque de contexto.

Aquí hay un ejemplo simple de cómo se usa un context manager en Python con la declaración 'with':

```python
class MiContextManager:
    def __enter__(self):
        print("Inicializando el contexto")
        # Puede realizar cualquier inicialización necesaria aquí
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Limpiando el contexto")
        # Puede realizar cualquier limpieza necesaria aquí

# Usando el context manager con la declaración "with"
with MiContextManager() as cm:
    print("Dentro del bloque de contexto")

```

En este ejemplo:

* Al entrar en el bloque de contexto, se llama al método __enter__() del context manager, que imprime "Inicializando el contexto".
* Se ejecuta el código dentro del bloque de contexto (en este caso, simplemente imprime "Dentro del bloque de contexto").
* Al salir del bloque de contexto (ya sea normalmente o debido a una excepción), se llama al método __exit__() del context manager, que imprime "Limpiando el contexto".

Los context managers son útiles para garantizar la liberación adecuada de recursos y la gestión de situaciones excepcionales de manera elegante y concisa en Python.
