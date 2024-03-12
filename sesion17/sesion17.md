[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
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

# Context Manager

Un context manager en Python es un objeto que se utiliza para administrar un contexto, es decir, una serie de acciones que se deben realizar antes y después de una operación principal. Los context managers son comúnmente utilizados para manejar recursos como **archivos**, **conexiones de red** o **bases de datos**, garantizando que se realicen operaciones importantes como la apertura y el cierre de recursos de manera segura y eficiente.

En Python, hay dos formas principales de implementar un context manager:

1. Usando la **declaración** with: Esto implica definir una clase que implemente los métodos \__enter__() y \__exit__(). El método \__enter__() se ejecuta al comienzo del bloque with y el método \__exit__() se ejecuta al final del bloque with, permitiendo así realizar operaciones de inicialización y limpieza respectivamente.

2. Usando el **decorador** contextlib.contextmanager: Este es un enfoque más simple y compacto que utiliza generadores para definir un context manager. Permite crear context managers de una manera más concisa y legible.

Aquí tienes un ejemplo de cómo implementar un context manager utilizando la declaración with:

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


Y aquí tienes un ejemplo de cómo implementar un context manager utilizando el decorador contextlib.contextmanager:

```python
from contextlib import contextmanager

@contextmanager
def mi_context_manager():
    print("Inicializando el contexto")
    # Puede realizar cualquier inicialización necesaria aquí
    try:
        yield
    finally:
        print("Limpiando el contexto")
        # Puede realizar cualquier limpieza necesaria aquí

# Usando el context manager con la declaración "with"
with mi_context_manager():
    print("Dentro del bloque de contexto")

```

Ambos enfoques son válidos y útiles en diferentes situaciones, y la elección entre ellos depende de las necesidades específicas y de la preferencia del programador. Los context managers son una herramienta poderosa y útil en Python para manejar recursos y gestionar el contexto de operaciones.

Los context managers son útiles para garantizar la liberación adecuada de recursos y la gestión de situaciones excepcionales de manera elegante y concisa en Python.

## Context manager (with, declaración)

Cuando se utiliza la declaración 'with' en Python junto con un context manager, se garantiza que ciertas operaciones de inicialización se realicen antes de entrar en el bloque with, y que las operaciones de limpieza se realicen al salir del bloque with, incluso si ocurren excepciones durante la ejecución del código dentro del bloque.

Aquí hay algunos detalles adicionales sobre cómo funciona la declaración with con un context manager:

Entrando en el contexto: Cuando se entra en el bloque with, se llama al método __enter__() del context manager, si está definido. Esto permite realizar cualquier operación de inicialización necesaria antes de comenzar a ejecutar el código dentro del bloque with.

Ejecución del código dentro del bloque with: El código dentro del bloque with se ejecuta después de entrar en el contexto proporcionado por el context manager. Cualquier operación realizada dentro de este bloque se realiza dentro de este contexto.

Manejo de excepciones: Si ocurre una excepción dentro del bloque with, se captura y se pasa al método __exit__() del context manager, si está definido. Esto permite realizar acciones de limpieza necesarias, como cerrar archivos o liberar recursos, incluso en caso de excepción.

Saliendo del contexto: Al salir del bloque with, se llama al método __exit__() del context manager, si está definido. Esto garantiza que las operaciones de limpieza se realicen adecuadamente, independientemente de si ocurrieron excepciones dentro del bloque with.

Liberación automática de recursos: Una de las principales ventajas de usar la declaración with es que garantiza que los recursos asociados con el context manager se liberen correctamente al salir del bloque with, lo que ayuda a prevenir fugas de recursos y a garantizar la integridad del sistema.

Aquí hay un ejemplo para ilustrar cómo se usa la declaración with con un context manager:

```python
class MiContextManager:
    def __enter__(self):
        print("Inicializando el contexto")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Limpiando el contexto")

# Usando el context manager con la declaración "with"
with MiContextManager() as cm:
    print("Dentro del bloque de contexto")

```
En este ejemplo, el método __enter__() imprime "Inicializando el contexto" al entrar en el bloque with, y el método __exit__() imprime "Limpiando el contexto" al salir del bloque with. El código dentro del bloque with se ejecuta dentro del contexto proporcionado por el context manager.

# Context Manager (decorador @)

Cuando se utiliza el decorador **contextlib.contextmanager** en Python, se puede crear un context manager de manera más concisa utilizando un generador. Este generador debe contener una o más instrucciones 'yield', lo que permite definir el punto de entrada y el punto de salida del contexto.

Aquí hay más detalles sobre cómo funciona el decorador contextlib.contextmanager:

1. **Definición del generador**: Se utiliza el decorador @contextmanager para decorar un generador. Este generador debe contener una instrucción yield que divide el código en dos partes: la parte que se ejecuta antes de entrar en el contexto y la parte que se ejecuta después de salir del contexto.

2. **Inicialización del contexto**: La parte del código que se encuentra antes de la instrucción yield se ejecuta cuando se entra en el bloque with. Esto permite realizar operaciones de inicialización necesarias antes de comenzar a ejecutar el código dentro del bloque with.

3. **Entrando en el contexto**: Al llamar a la instrucción yield, el control pasa al bloque de código dentro del bloque with. Esto significa que cualquier código después de la instrucción yield se ejecutará después de entrar en el contexto proporcionado por el context manager.

4. **Manejo de excepciones**: Si ocurre una excepción dentro del bloque with, se pasa al generador y se puede manejar dentro del mismo. Esto permite realizar acciones de limpieza necesarias, como cerrar archivos o liberar recursos, incluso en caso de excepción.

5. **Saliendo del contexto**: Después de salir del bloque with, el control vuelve al generador, y cualquier código después de la instrucción yield se ejecutará al salir del contexto. Esto permite realizar operaciones de limpieza o cualquier otra acción necesaria antes de finalizar el context manager.

Aquí hay un ejemplo para ilustrar cómo se utiliza el decorador **contextlib.contextmanager** para crear un context manager:

```python
from contextlib import contextmanager

@contextmanager
def mi_context_manager():
    print("Inicializando el contexto")
    try:
        yield
    finally:
        print("Limpiando el contexto")

# Usando el context manager con la declaración "with"
with mi_context_manager():
    print("Dentro del bloque de contexto")

```

En este ejemplo, la instrucción yield divide el código en dos partes: la parte antes de yield se ejecuta al entrar en el bloque with, y la parte después de yield se ejecuta al salir del bloque with. El código dentro del bloque with se ejecuta dentro del contexto proporcionado por el context manager.

## context manger declaracion VS decorador

Tanto la declaración de un context manager como el uso del decorador **contextlib.contextmanager** permiten crear context managers en Python, pero difieren en la forma en que se implementan y en su sintaxis.

Aquí están las diferencias entre ambos:

1. Declaración de un context manager:

* Sintaxis: Se define una clase que implementa los métodos \__enter__() y \__exit__(). El método \__enter__() se ejecuta al entrar en el bloque 'with', y el método \__exit__() se ejecuta al salir del bloque with.

* Uso de la declaración 'with': El context manager se utiliza dentro de una declaración 'with', y el bloque de código que sigue a 'with' se ejecuta dentro del contexto proporcionado por el context manager.

* Control más detallado: Al implementar un context manager como una clase, tienes un control más detallado sobre las acciones que se realizan al entrar y salir del contexto, lo que puede ser útil en casos donde necesitas realizar operaciones más complejas.

2. Uso del decorador contextlib.contextmanager:

* Sintaxis más concisa: Se utiliza un generador para definir un context manager, lo que hace que la implementación sea más concisa y legible.

* Menos boilerplate: No es necesario definir explícitamente los métodos \__enter__() y \__exit__(), lo que reduce la cantidad de código que necesitas escribir.

* Más adecuado para casos simples: Es más adecuado para casos donde el context manager es relativamente simple y no requiere operaciones complejas de inicialización o limpieza.

* Uso de yield: Dentro del generador, el valor generado por yield define el punto de entrada en el contexto, y cualquier código después de yield se ejecuta al salir del contexto.

>En resumen, la declaración de un context manager utilizando una clase proporciona un control más detallado y es más adecuada para casos más complejos, mientras que el uso del decorador contextlib.contextmanager es más adecuado para context managers simples y proporciona una sintaxis más concisa y menos boilerplate. La elección entre ambos depende de las necesidades específicas y de la complejidad del context manager que estés implementando.


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

# Bibliotecas y conectores Base de datos

Hay una variedad de bibliotecas y conectores disponibles en Python para interactuar con diferentes sistemas de bases de datos. Aquí hay algunos de los conectores más comunes para las bases de datos más populares:

1. SQLite3: Para interactuar con bases de datos SQLite, Python incluye una biblioteca estándar llamada sqlite3, que proporciona una API para trabajar con bases de datos SQLite de forma nativa sin necesidad de instalar bibliotecas adicionales.

2. MySQL: Para interactuar con bases de datos MySQL, puedes usar la biblioteca mysql-connector-python, que es un conector oficial proporcionado por MySQL para Python. También puedes usar bibliotecas como PyMySQL y mysqlclient, que ofrecen funcionalidades similares.

3. PostgreSQL: Para interactuar con bases de datos PostgreSQL, puedes usar el conector oficial psycopg2, que es una biblioteca popular y ampliamente utilizada para Python. También está pg8000, una alternativa más ligera y puramente en Python.

4. Oracle: Para interactuar con bases de datos Oracle, puedes usar cx_Oracle, que es el conector oficial proporcionado por Oracle para Python. Es altamente compatible y soporta características avanzadas de Oracle Database.

5. Microsoft SQL Server: Para interactuar con bases de datos SQL Server, puedes usar pyodbc, que es un módulo Python que proporciona una API para interactuar con bases de datos ODBC, incluyendo SQL Server. También hay bibliotecas específicas como pymssql, que están diseñadas específicamente para interactuar con SQL Server.

6. MongoDB: Para interactuar con bases de datos NoSQL como MongoDB, puedes usar bibliotecas como pymongo, que proporciona una API completa y robusta para trabajar con MongoDB desde Python.

7. Cassandra: Para interactuar con bases de datos NoSQL como Apache Cassandra, puedes usar cassandra-driver, que es un conector oficial proporcionado por DataStax para Python. Proporciona una API para interactuar con Cassandra de manera eficiente y segura.

Estos son solo algunos ejemplos de conectores disponibles en Python para diferentes sistemas de bases de datos. La elección del conector depende del sistema de bases de datos que estés utilizando y de tus preferencias personales en términos de funcionalidad, compatibilidad y rendimiento.

# SQL

Para ejecutar consultas SQL dentro de Python, puedes utilizar varias bibliotecas que facilitan la interacción con bases de datos relacionales. Algunas de las bibliotecas más populares para trabajar con bases de datos SQL en Python son:

**SQLite3**: Es una biblioteca estándar de Python que proporciona una API para trabajar con la base de datos SQLite, que es una base de datos ligera y autocontenida que no requiere un servidor separado. SQLite3 se utiliza comúnmente para aplicaciones que necesitan una base de datos local sin los requisitos de rendimiento de una base de datos completa del servidor.

Ejemplo de uso de SQLite3:

```python
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta SQL
cursor.execute('SELECT * FROM tabla')

# Obtener los resultados
resultados = cursor.fetchall()

# Cerrar la conexión
conn.close()

```

**SQLAlchemy**: Es una biblioteca ORM (Object-Relational Mapping) que proporciona una forma más orientada a objetos de interactuar con bases de datos SQL en Python. SQLAlchemy facilita la creación y ejecución de consultas SQL y proporciona un alto grado de portabilidad entre diferentes sistemas de bases de datos.

Ejemplo de uso de SQLAlchemy:

```python
from sqlalchemy import create_engine, MetaData, Table

# Crear un motor de base de datos
engine = create_engine('sqlite:///ejemplo.db')

# Conectar al motor
conn = engine.connect()

# Crear un objeto MetaData
metadata = MetaData()

# Cargar la tabla
tabla = Table('nombre_tabla', metadata, autoload=True, autoload_with=engine)

# Ejecutar una consulta SQL
consulta = tabla.select()
resultados = conn.execute(consulta).fetchall()

# Cerrar la conexión
conn.close()

```

**Psycopg2 (para PostgreSQL)**: Es una biblioteca de adaptador de base de datos para PostgreSQL que proporciona una API para trabajar con bases de datos PostgreSQL desde Python. Psycopg2 es muy popular y ampliamente utilizado en aplicaciones que utilizan PostgreSQL como base de datos.

Ejemplo de uso de Psycopg2:

```python
import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    dbname='nombre_db',
    user='usuario',
    password='contraseña',
    host='localhost'
)

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta SQL
cursor.execute('SELECT * FROM tabla')

# Obtener los resultados
resultados = cursor.fetchall()

# Cerrar la conexión
conn.close()

```

Estas son solo algunas de las opciones disponibles para ejecutar consultas SQL dentro de Python. La elección de la biblioteca depende de factores como el tipo de base de datos que estés utilizando, tus preferencias personales y los requisitos específicos de tu aplicación.


## SQLite3

SQLite3 es una biblioteca ligera de administración de bases de datos relacionales que implementa un motor de base de datos SQL de servidor completo. Aquí hay algunos puntos clave y características importantes sobre SQLite3:

1. Autocontenido y sin servidor: SQLite3 es una base de datos autocontenido, lo que significa que toda la base de datos se almacena en un solo archivo de disco. No requiere un servidor de base de datos separado como MySQL o PostgreSQL. Esto lo hace ideal para aplicaciones que necesitan una base de datos local sin las complicaciones de configurar y administrar un servidor de base de datos.

2. Transacciones ACID: SQLite3 es compatible con transacciones ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad), lo que garantiza la integridad y la consistencia de los datos incluso en casos de fallos del sistema o caídas repentinas.

3. Ampliamente utilizado y bien soportado: SQLite3 es una de las bases de datos más utilizadas en el mundo, y está ampliamente integrada en muchos lenguajes de programación y sistemas operativos. Tiene una gran base de usuarios y una comunidad activa que proporciona soporte y contribuciones constantes.

4. Soporte completo de SQL: SQLite3 admite una gran parte del estándar SQL y proporciona muchas de las características que esperarías de una base de datos relacional, como consultas SELECT, INSERT, UPDATE y DELETE, así como la creación de tablas, índices y vistas.

5. Portabilidad: Debido a su naturaleza autocontenido y su amplio soporte, SQLite3 es altamente portátil y puede ejecutarse en una variedad de plataformas y sistemas operativos, incluyendo Windows, macOS, Linux, iOS y Android.

6. Rendimiento razonable: SQLite3 está diseñado para ser rápido y eficiente, especialmente para cargas de trabajo ligeras a moderadas. Aunque puede no ser tan rápido como los motores de bases de datos de servidor completo en situaciones de alta concurrencia o cargas de trabajo intensivas, proporciona un rendimiento más que adecuado para muchas aplicaciones.

7. Herramientas de administración: SQLite3 viene con varias herramientas de línea de comandos y GUI que facilitan la administración y el mantenimiento de bases de datos SQLite, como sqlite3 (CLI) y SQLiteStudio (GUI).

>En resumen, SQLite3 es una excelente opción para aplicaciones que requieren una base de datos ligera, autocontenido y fácil de usar. Es adecuado para una variedad de casos de uso, incluyendo aplicaciones móviles, aplicaciones de escritorio, aplicaciones web y proyectos de desarrollo rápido de prototipos.

### Cuando implementar

SQLite3 es una excelente opción en varias situaciones. Aquí hay algunos casos comunes en los que es apropiado utilizar SQLite3:

1. Aplicaciones móviles: SQLite3 es ampliamente utilizado en aplicaciones móviles, especialmente en dispositivos iOS y Android, donde proporciona una base de datos local eficiente para almacenar datos de la aplicación, como configuraciones, cachés, registros de usuario, etc. Su naturaleza autocontenida y su bajo consumo de recursos hacen que sea una opción ideal para aplicaciones móviles.

2. Desarrollo de prototipos y aplicaciones de un solo usuario: Cuando estás desarrollando una aplicación de escritorio o web que necesita una base de datos local para almacenar datos temporales o de usuario, SQLite3 es una excelente opción. Es rápido de configurar, no requiere un servidor de base de datos separado y proporciona todas las características necesarias para desarrollar y probar rápidamente tu aplicación.

3. Aplicaciones web pequeñas y medianas: Para aplicaciones web con cargas de trabajo ligeras a moderadas, SQLite3 puede ser una opción viable como base de datos principal. Es especialmente útil cuando necesitas una base de datos local para almacenar datos de configuración, sesiones de usuario, registros de actividad, etc., y no quieres lidiar con la complejidad y el costo de configurar un servidor de base de datos completo.

4. Herramientas de línea de comandos y utilidades: SQLite3 es a menudo utilizado en herramientas de línea de comandos y utilidades que requieren almacenamiento de datos local, como scripts de automatización, herramientas de análisis de datos, procesamiento por lotes, etc. Su naturaleza autocontenida y su facilidad de uso lo hacen ideal para este tipo de casos de uso.

>En resumen, SQLite3 es una excelente opción cuando necesitas una base de datos ligera, autocontenida y fácil de usar para aplicaciones móviles, desarrollo de prototipos, aplicaciones de un solo usuario, aplicaciones web pequeñas y medianas, y herramientas de línea de comandos y utilidades. Sin embargo, es importante tener en cuenta sus limitaciones en términos de rendimiento y escalabilidad, y considerar otras opciones si necesitas soportar cargas de trabajo intensivas o una alta concurrencia.

### Ejemplo creacion base datos de contactos
Un ejemplo más completo de cómo usar SQLite3 en Python para crear una base de datos de contactos, crear una tabla, insertar datos, y consultar la información de la tabla:

```python
import sqlite3

# Función para crear la tabla de contactos si no existe
def crear_tabla_contactos(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contactos (
                      id INTEGER PRIMARY KEY,
                      nombre TEXT NOT NULL,
                      telefono TEXT NOT NULL)''')
    conn.commit()

# Función para insertar un nuevo contacto en la tabla
def insertar_contacto(conn, nombre, telefono):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contactos (nombre, telefono) VALUES (?, ?)', (nombre, telefono))
    conn.commit()

# Función para obtener todos los contactos de la tabla
def obtener_contactos(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos')
    return cursor.fetchall()

# Función para obtener un contacto por nombre
def obtener_contacto_por_nombre(conn, nombre):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos WHERE nombre=?', (nombre,))
    return cursor.fetchone()

# Función principal
def main():
    # Conectar a la base de datos (se creará si no existe)
    conn = sqlite3.connect('contactos.db')

    # Crear la tabla de contactos si no existe
    crear_tabla_contactos(conn)

    # Insertar algunos contactos
    insertar_contacto(conn, 'Juan', '123456789')
    insertar_contacto(conn, 'Maria', '987654321')

    # Obtener todos los contactos e imprimirlos
    print("Todos los contactos:")
    for contacto in obtener_contactos(conn):
        print(contacto)

    # Obtener un contacto por nombre e imprimirlo
    nombre_buscar = 'Juan'
    print(f"\nContacto con el nombre '{nombre_buscar}':")
    contacto = obtener_contacto_por_nombre(conn, nombre_buscar)
    if contacto:
        print(contacto)
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre_buscar}'")

    # Cerrar la conexión
    conn.close()

if __name__ == "__main__":
    main()

```

Este script crea una base de datos SQLite llamada contactos.db, crea una tabla llamada contactos si no existe, inserta algunos contactos en la tabla, y luego realiza consultas para obtener todos los contactos e imprimirlos, así como para obtener un contacto específico por nombre.

No es necesario incluir un método \__init__ en el caso del ejemplo proporcionado anteriormente para trabajar con SQLite3 en Python. El método \__init__ se utiliza comúnmente en clases para inicializar objetos cuando se crean, pero en el caso de funciones o scripts independientes como el ejemplo que proporcioné, no es obligatorio ni necesario.

En el ejemplo anterior, las funciones están diseñadas para trabajar con una conexión de base de datos conn que se pasa como argumento a cada función según sea necesario. No hay necesidad de crear una instancia de una clase, por lo que no es necesario definir un método \__init__ para inicializar objetos.

Sin embargo, si estás creando una aplicación más compleja y deseas encapsular la lógica relacionada con la base de datos en una clase, podrías optar por utilizar un método \__init__ para inicializar una conexión de base de datos en la instancia de la clase. En ese caso, el uso de un método \__init__ podría ser apropiado dependiendo de la estructura y diseño de tu aplicación.

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

