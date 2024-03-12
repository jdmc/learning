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

# Pathlib

**pathlib** es un módulo de la biblioteca estándar de Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios de manera más intuitiva y portátil. Fue introducido en Python 3.4 como una forma más moderna y eficiente de manejar rutas de archivos en comparación con los métodos tradicionales proporcionados por los módulos 'os.path' y 'os'.

Algunas características importantes de pathlib son:

1. Interfaz orientada a objetos: pathlib utiliza objetos para representar rutas de archivos y directorios en lugar de manipularlas como cadenas de texto. Esto facilita la manipulación y navegación de rutas utilizando métodos y atributos de objetos.

2. Compatibilidad con múltiples sistemas operativos: pathlib abstrae las diferencias entre diferentes sistemas operativos en cuanto a la representación de rutas de archivos y directorios. Esto significa que puedes escribir código que funcione de la misma manera en diferentes plataformas sin preocuparte por las diferencias en la estructura de las rutas.

3. Sintaxis más clara y concisa: La sintaxis proporcionada por pathlib es más legible y concisa que la sintaxis basada en cadenas de texto utilizada por los métodos tradicionales como os.path. Esto hace que el código sea más fácil de entender y mantener.

4. Seguridad incorporada: pathlib proporciona métodos para realizar operaciones seguras en rutas de archivos y directorios, como la resolución de rutas relativas y la manipulación de rutas absolutas de manera segura.

Aquí tienes un ejemplo básico de cómo usar pathlib:

```python
from pathlib import Path

# Crear una ruta
ruta = Path('/ruta/a/mi/archivo.txt')

# Comprobar si la ruta existe
print(ruta.exists())

# Obtener el nombre del archivo
print(ruta.name)

# Obtener el directorio padre
print(ruta.parent)

# Unirse a otra ruta
otra_ruta = ruta.parent / 'otro_archivo.txt'

# Resolver la ruta absoluta
print(ruta.resolve())

# Iterar sobre los archivos en un directorio
for archivo in Path('/mi/directorio').iterdir():
    print(archivo)

```

>En resumen, pathlib es una herramienta poderosa y moderna para trabajar con rutas de archivos y directorios en Python, que ofrece una sintaxis más clara y concisa, junto con una mayor portabilidad y seguridad. Es especialmente útil en aplicaciones donde se manipulan muchas rutas de archivos y directorios.

### Manipulación de archivos y directorios

**pathlib** está estrechamente relacionado con la manipulación de archivos y directorios en Python, ya que proporciona una forma más conveniente y eficiente de trabajar con rutas de archivos y directorios. Aunque pathlib en sí mismo no maneja la lectura o escritura de archivos, simplifica significativamente la tarea de acceder y manipular rutas de archivos, lo que a su vez facilita el trabajo con archivos en general.

Aquí hay algunas formas en que pathlib se relaciona con la manipulación de archivos:

1. Creación de rutas de archivos y directorios: pathlib facilita la creación de objetos que representan rutas de archivos y directorios utilizando la clase Path. Estos objetos proporcionan una forma más intuitiva y segura de especificar rutas en lugar de trabajar directamente con cadenas de texto.

2. Navegación de directorios: Puedes utilizar métodos proporcionados por pathlib para navegar a través de directorios, obtener listas de archivos en un directorio, verificar si un archivo o directorio existe, etc. Esto es útil al leer múltiples archivos de un directorio o al verificar la existencia de un archivo antes de realizar operaciones en él.

3. Resolución de rutas: pathlib facilita la resolución de rutas relativas y absolutas, lo que es útil al trabajar con rutas de archivos en diferentes ubicaciones. Esto puede ser especialmente útil al manipular archivos en sistemas de archivos complejos o al construir rutas dinámicamente.

4. Manipulación de rutas: Puedes utilizar métodos y operadores proporcionados por pathlib para manipular rutas de archivos de manera segura y conveniente, como unir rutas, obtener partes de una ruta, cambiar la extensión de un archivo, etc.

>En resumen, aunque pathlib no maneja directamente la lectura o escritura de archivos, es una herramienta esencial para trabajar con archivos en Python, ya que simplifica la tarea de manipular y navegar por rutas de archivos y directorios, lo que a su vez facilita el trabajo con archivos en general.

## Path

**pathlib.Path** es la clase principal del **módulo pathlib** de Python. Esta clase se utiliza para representar rutas de archivos y directorios en el sistema de archivos de manera más conveniente y orientada a objetos. Proporciona una serie de métodos y atributos para trabajar con estas rutas de una manera más eficiente y legible que los métodos tradicionales proporcionados por los módulos os.path.

Cuando creas un objeto Path, estás creando una instancia de la clase Path que representa una ruta en el sistema de archivos. Puedes utilizar este objeto para realizar diversas operaciones relacionadas con esa ruta, como verificar si el archivo o directorio existe, obtener información sobre la ruta, navegar por el sistema de archivos, manipular la ruta y más.

Aquí hay algunos ejemplos de cómo crear y utilizar objetos Path:

```python
from pathlib import Path

# Crear una ruta de archivo
ruta_archivo = Path('/ruta/a/mi/archivo.txt')

# Crear una ruta de directorio
ruta_directorio = Path('/mi/directorio')

# Verificar si la ruta de archivo existe
print(ruta_archivo.exists())

# Obtener el nombre del archivo o directorio
print(ruta_archivo.name)

# Obtener el directorio padre
print(ruta_archivo.parent)

# Unirse a otra ruta
otra_ruta = ruta_directorio / 'otro_archivo.txt'

# Resolver la ruta absoluta
print(ruta_archivo.resolve())

# Iterar sobre los archivos en un directorio
for archivo in ruta_directorio.iterdir():
    print(archivo)

```

En este ejemplo, **Path** es la clase que se utiliza para crear objetos que representan rutas de archivos y directorios. Luego, se pueden utilizar varios métodos y atributos proporcionados por esta clase para realizar diferentes operaciones relacionadas con esas rutas, como verificar la existencia de un archivo, obtener información sobre la ruta, unirse a otras rutas, resolver rutas absolutas, iterar sobre archivos en un directorio, entre otras cosas.

>En resumen, pathlib.Path es una clase fundamental en el módulo pathlib que se utiliza para manipular rutas de archivos y directorios en Python de manera más conveniente y orientada a objetos.

# shutil

**shutil** es un módulo de la biblioteca estándar de Python que proporciona funciones para operaciones de alto nivel en archivos y directorios. Este módulo simplifica tareas comunes como copiar, mover y eliminar archivos y directorios, así como trabajar con archivos comprimidos.

Aunque **shutil** no está directamente relacionado con la manipulación de rutas de archivos y directorios como pathlib, ambos módulos se utilizan a menudo en conjunto para realizar operaciones relacionadas con archivos de manera eficiente y conveniente.

Aquí tienes algunos ejemplos de cómo usar shutil y cómo puede relacionarse con pathlib:

* Copiar un archivo:

```python
import shutil
from pathlib import Path

# Rutas de origen y destino utilizando Path
ruta_origen = Path('archivo_origen.txt')
ruta_destino = Path('directorio_destino/archivo_destino.txt')

# Copiar el archivo
shutil.copy(ruta_origen, ruta_destino)

```
En este ejemplo, utilizamos pathlib.Path para representar las rutas de origen y destino del archivo que queremos copiar, y luego usamos **shutil.copy()** para realizar la operación de copia.

* Mover un archivo:

```python
import shutil
from pathlib import Path

# Rutas de origen y destino utilizando Path
ruta_origen = Path('archivo.txt')
ruta_destino = Path('nuevo_directorio/archivo.txt')

# Mover el archivo
shutil.move(ruta_origen, ruta_destino)

```

Aquí, nuevamente, usamos pathlib.Path para definir las rutas de origen y destino del archivo que queremos mover, y luego usamos **shutil.move()** para realizar la operación de mover.

* Eliminar un archivo o directorio:

```python
import shutil
from pathlib import Path

# Ruta del archivo o directorio a eliminar
ruta_eliminar = Path('archivo_o_directorio')

# Eliminar el archivo o directorio
shutil.rmtree(ruta_eliminar)

```

En este caso, **pathlib.Path** se utiliza para especificar la ruta del archivo o directorio que queremos eliminar, y luego **shutil.rmtree()** se utiliza para realizar la operación de eliminación recursiva.

>En resumen, aunque shutil y pathlib son módulos diferentes con propósitos diferentes, se pueden utilizar juntos para realizar operaciones avanzadas en archivos y directorios de manera más eficiente y conveniente en Python. Mientras que pathlib se enfoca en la manipulación y representación de rutas de archivos y directorios, shutil proporciona funciones para realizar operaciones de alto nivel en estos archivos y directorios.

# with open()

La expresión **with open()** en Python se utiliza para abrir un archivo en un bloque de código, proporcionando una forma más segura y eficiente de trabajar con archivos. El uso de with open() garantiza que el archivo se cierre correctamente después de que el bloque de código termine, incluso si ocurre una excepción dentro del bloque.

La sintaxis general es la siguiente:

```python
with open('nombre_archivo', 'modo') as archivo:
    # Código para trabajar con el archivo

```

Donde:

* 'nombre_archivo' es el nombre o la ruta del archivo que deseas abrir.
* 'modo' es el modo en el que deseas abrir el archivo (por ejemplo, 'r' para lectura, 'w' para escritura, 'a' para añadir contenido al final del archivo, etc.).
* archivo es el identificador que utilizas dentro del bloque de código para referirte al archivo abierto.


Aquí hay un ejemplo de cómo usar with open() para leer el contenido de un archivo:

```python
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

```
En este ejemplo, el archivo 'archivo.txt' se abre en modo de lectura ('r') y se asocia con el identificador archivo. Dentro del bloque with, puedes realizar operaciones de lectura en el archivo, como leer el contenido completo con archivo.read(). Una vez que el bloque de código dentro de with termina, el archivo se cierra automáticamente, liberando los recursos asociados.

Usar with open() es una práctica recomendada al trabajar con archivos en Python, ya que garantiza que los recursos del sistema se manejen adecuadamente y evita posibles problemas de pérdida de datos o corrupción de archivos debido a archivos que no se cierran correctamente.

## modos para abrir el archivo

Dentro de la construcción with open(), el modo especifica cómo deseas abrir el archivo. Aquí están los modos más comunes que puedes utilizar con la función open() en Python:

1. 'r': Modo de solo lectura. Abre el archivo para leer. Genera un error si el archivo no existe.

2. 'w': Modo de escritura. Abre el archivo para escribir. Si el archivo ya existe, se trunca (se borra su contenido). Si el archivo no existe, se crea uno nuevo.

3. 'a': Modo de añadir (append). Abre el archivo para añadir datos al final. Si el archivo no existe, se crea uno nuevo.

4. 'b': Modo binario. Abre el archivo en modo binario, útil para trabajar con archivos binarios como imágenes, videos, etc. (por ejemplo, 'rb', 'wb', 'ab').

5. '+': Modo de lectura y escritura. Abre el archivo para leer y escribir. (por ejemplo, 'r+', 'w+', 'a+'). Ten en cuenta que este modo puede ser confuso y es más propenso a errores.

6. 'x': Modo exclusivo. Crea un nuevo archivo y genera un error si el archivo ya existe.

Estos son los modos más comunes que puedes utilizar con la función open(), pero hay otros modos más específicos para casos particulares. Al utilizar with open(), debes especificar al menos el modo y el nombre del archivo que deseas abrir. Por ejemplo:

```python
# Abrir un archivo para lectura
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

# Abrir un archivo para escritura
with open('nuevo_archivo.txt', 'w') as archivo:
    archivo.write("Este es un nuevo archivo.")

```
Siempre es importante recordar cerrar el archivo después de que hayas terminado de trabajar con él, y with open() te proporciona una forma conveniente de hacerlo automáticamente.

# stream

En el contexto de la programación y el manejo de datos, un "stream" (flujo) se refiere a una secuencia de datos que se transfiere de un lugar a otro de manera continua y progresiva. Un stream puede representar datos que se están leyendo desde una fuente, como un archivo, una conexión de red o la entrada estándar del usuario, o datos que se están escribiendo en un destino, como un archivo de salida, una conexión de red o la salida estándar del usuario.

Los streams son utilizados comúnmente en muchos lenguajes de programación para procesar grandes cantidades de datos de manera eficiente, ya que permiten leer o escribir datos a medida que están disponibles, en lugar de tener que cargarlos todos en la memoria al mismo tiempo.

Hay dos tipos principales de streams:

1. Flujos de entrada (input streams): Representan una secuencia de datos que se está leyendo de una fuente externa. Por ejemplo, cuando estás leyendo datos desde un archivo, desde el teclado o desde una conexión de red, estás trabajando con un flujo de entrada.

2. Flujos de salida (output streams): Representan una secuencia de datos que se está escribiendo en un destino externo. Por ejemplo, cuando estás escribiendo datos en un archivo, enviándolos a través de una conexión de red o mostrándolos en la pantalla, estás trabajando con un flujo de salida.

>En resumen, un stream es una abstracción que permite la transferencia continua de datos entre una fuente y un destino, lo que facilita el procesamiento eficiente de datos en tiempo real o de grandes conjuntos de datos sin necesidad de cargar todo en la memoria al mismo tiempo. Los streams son fundamentales en la programación de sistemas de entrada/salida (I/O) en muchos entornos de programación y aplicaciones.

Supongamos que tienes un archivo llamado entrada.txt con el siguiente contenido:

<!-- Este es un ejemplo de un archivo de entrada.
Contiene algunas líneas de texto que queremos copiar.
 -->

Ahora queremos leer este archivo línea por línea y escribir su contenido en otro archivo llamado salida.txt. Podemos hacerlo utilizando streams de la siguiente manera:
```python
# Abrir el archivo de entrada en modo lectura
with open('entrada.txt', 'r') as archivo_entrada:
    # Abrir el archivo de salida en modo escritura
    with open('salida.txt', 'w') as archivo_salida:
        # Leer cada línea del archivo de entrada
        for linea in archivo_entrada:
            # Escribir la línea en el archivo de salida
            archivo_salida.write(linea)

```

En este ejemplo:

* Abrimos el archivo de entrada entrada.txt en modo lectura ('r') utilizando la declaración with, lo que garantiza que el archivo se cierre correctamente después de su uso.
* Abrimos el archivo de salida salida.txt en modo escritura ('w') utilizando la declaración with, lo que también garantiza que el archivo se cierre correctamente después de su uso.
* Iteramos sobre cada línea del archivo de entrada utilizando un bucle for.
* Escribimos cada línea en el archivo de salida utilizando el método write().

Al finalizar el bloque with, ambos archivos se cierran automáticamente. Como resultado, el contenido del archivo de entrada se copia línea por línea en el archivo de salida.

Este es un ejemplo básico de cómo usar streams en Python para leer datos de un archivo y escribirlos en otro archivo. Los streams son una parte fundamental de la programación en Python cuando trabajas con archivos y operaciones de entrada/salida (I/O).

# mkdir 

En Python, mkdir no es una función específica del lenguaje, pero es comúnmente asociada con la creación de directorios en el sistema de archivos.

Para crear un directorio en Python, puedes utilizar el método mkdir() proporcionado por la clase Path del módulo pathlib, o la función os.mkdir() del módulo os. Ambas opciones son válidas y tienen el mismo propósito, pero pathlib proporciona una interfaz más orientada a objetos y moderna para trabajar con rutas de archivos y directorios.

Aquí tienes ejemplos de cómo crear un directorio usando ambas opciones:

* Usando pathlib.Path.mkdir():

```python
from pathlib import Path

# Define la ruta del nuevo directorio
ruta_nuevo_directorio = Path('/ruta/a/mi/nuevo/directorio')

# Crea el directorio si no existe
ruta_nuevo_directorio.mkdir(parents=True, exist_ok=True)

```
En este ejemplo, Path('/ruta/a/mi/nuevo/directorio') define la ruta del nuevo directorio que queremos crear. Luego, llamamos al método mkdir() de la instancia de Path para crear el directorio. El argumento parents=True indica que se deben crear todos los directorios padres necesarios si aún no existen, y exist_ok=True indica que no se debe lanzar una excepción si el directorio ya existe.

* Usando os.mkdir():

```python
import os

# Define la ruta del nuevo directorio
ruta_nuevo_directorio = '/ruta/a/mi/nuevo/directorio'

# Crea el directorio si no existe
os.mkdir(ruta_nuevo_directorio)

```
En este ejemplo, 'ruta/a/mi/nuevo/directorio' define la ruta del nuevo directorio que queremos crear. Luego, llamamos a la función os.mkdir() y le pasamos la ruta del directorio como argumento para crear el directorio.

Ambas opciones logran el mismo resultado: crear un nuevo directorio en el sistema de archivos. La elección entre usar pathlib o os depende de tus preferencias personales y del estilo de programación que estés utilizando en tu código.

# platform 

En Python, **platform** es un módulo de la biblioteca estándar que proporciona funciones y herramientas para obtener información sobre la plataforma en la que se está ejecutando el código Python. Esta información incluye detalles sobre el sistema operativo, el hardware y el entorno de ejecución.

El módulo **platform** se utiliza cuando necesitas escribir código que sea portátil entre diferentes plataformas, es decir, cuando deseas que tu programa funcione de manera consistente independientemente del sistema operativo o el hardware en el que se ejecute. Puedes utilizar las funciones proporcionadas por platform para obtener información sobre la plataforma y tomar decisiones basadas en esta información, como ajustar el comportamiento del programa para adaptarse a las diferencias entre sistemas operativos.

Algunas funciones útiles proporcionadas por el módulo **platform** incluyen:

* platform.system(): Devuelve el nombre del sistema operativo.
* platform.release(): Devuelve la versión del sistema operativo.
* platform.machine(): Devuelve el nombre de la arquitectura del hardware.
* platform.version(): Devuelve información adicional sobre la versión del sistema operativo.
* platform.platform(): Devuelve una cadena más detallada que describe la plataforma completa.

Aquí hay un ejemplo de cómo usar el módulo platform:

```python
import platform

print("Sistema operativo:", platform.system())
print("Versión del sistema operativo:", platform.release())
print("Arquitectura del hardware:", platform.machine())
print("Información completa de la plataforma:", platform.platform())

```

Dependiendo de la plataforma en la que se ejecute el código, este script imprimirá información relevante sobre el sistema operativo y el hardware.

>En resumen, el módulo platform en Python es útil cuando necesitas obtener información sobre la plataforma en la que se está ejecutando tu programa, y esta información puede ser utilizada para tomar decisiones o ajustar el comportamiento del programa para adaptarse a las diferencias entre sistemas operativos y hardware.

# Context Manager (lib)