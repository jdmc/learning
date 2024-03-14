
[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# expresion regular / regular expression

En Python, una expresión regular (o regular expression en inglés) es una secuencia de caracteres que define un patrón de búsqueda. Se utilizan principalmente para buscar y manipular cadenas de texto de manera flexible y eficiente. Las expresiones regulares son extremadamente útiles cuando se trabaja con cadenas de texto complejas y se necesitan realizar operaciones como **búsqueda**, **extracción**, **reemplazo** o **validación** de patrones.

Python proporciona un módulo llamado **re** que permite trabajar con expresiones regulares. Este módulo ofrece funciones y métodos para compilar expresiones regulares, buscar coincidencias en cadenas de texto, y realizar operaciones de manipulación de texto basadas en patrones.

Aquí hay un ejemplo básico de cómo usar expresiones regulares en Python para buscar un patrón específico en una cadena de texto:

```python
import re

# Función principal: re.search()
# Patrón: Buscar la palabra "apple" en cualquier parte de la cadena.
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'I have an apple and a banana.'

# Buscar coincidencias utilizando la expresión regular con re.search()
matches = re.search(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')


```
En este ejemplo, la expresión regular r'apple' se compila y luego se utiliza para buscar la palabra "apple" en la cadena de texto. La función re.search() devuelve un objeto Match si se encuentra una coincidencia, de lo contrario, devuelve None. Luego, podemos usar el método group() del objeto Match para obtener la cadena que coincide con el patrón.

## Funciones VS Patrones

Entiendo que puede haber cierta confusión entre los términos "funciones principales" y "tipos de expresiones" en el contexto de expresiones regulares en Python. 

1. **Funciones principales (principal functions)**:     
  En el contexto de expresiones regulares en Python, las "funciones principales" se refieren a las funciones proporcionadas por el módulo **re** que se utilizan para trabajar con expresiones regulares y cadenas de texto. Estas funciones principales incluyen **re.search()** y **re.match()**, que son las funciones principales para buscar patrones en cadenas de texto. Otros ejemplos de funciones principales incluyen **re.findall()**, **re.sub()**, **re.split()**, entre otras. Estas funciones son esenciales para realizar operaciones como búsqueda, extracción, reemplazo y división de cadenas de texto utilizando expresiones regulares.

2. **Tipos de expresiones (types of expressions)**:     
  En el contexto de expresiones regulares, los "tipos de expresiones" se refieren a los **patrones** específicos que se utilizan para buscar coincidencias en las cadenas de texto. Estos patrones están compuestos por una combinación de caracteres literales, metacaracteres, clases de caracteres, cuantificadores, agrupaciones y referencias, entre otros elementos. Los tipos de expresiones varían dependiendo de la complejidad del patrón que se está buscando y de los requisitos específicos del usuario. Por ejemplo, una expresión regular puede ser un patrón simple como **r'apple'**, que busca la palabra "apple" en una cadena de texto, o puede ser un patrón más complejo que incluya múltiples metacaracteres, clases de caracteres y cuantificadores para buscar un patrón más específico.

>En resumen, las "funciones principales" se refieren a las funciones proporcionadas por el módulo **re** para trabajar con expresiones regulares, mientras que los "tipos de expresiones" se refieren a los patrones específicos que se utilizan en las funciones principales para buscar coincidencias en las cadenas de texto. Ambos son conceptos fundamentales para comprender y utilizar efectivamente expresiones regulares en Python.

## Funciones principales

En Python, el módulo re proporciona dos funciones principales para buscar patrones en cadenas de texto: re.search() y re.match(). Ambas funciones utilizan expresiones regulares para buscar coincidencias en cadenas de texto, pero difieren ligeramente en su comportamiento. Aquí hay una explicación de cada una:

**re.search(pattern, string)**: Esta función busca en toda la cadena de texto string cualquier ocurrencia del patrón pattern. Si encuentra una coincidencia en cualquier parte de la cadena, devuelve un objeto Match, que contiene la información sobre la primera coincidencia encontrada. Si no se encuentra ninguna coincidencia, devuelve None.

```python
import re

# Función principal: re.search()
# Patrón: Buscar la palabra "apple" en cualquier parte de la cadena.
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'I have an apple and a banana.'

# Buscar coincidencias utilizando la expresión regular con re.search()
matches = re.search(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')


```

En este ejemplo, re.search() encuentra la palabra "apple" en la cadena de texto y devuelve un objeto **Match**.

**re.match(pattern, string)**: Esta función intenta hacer coincidir el patrón pattern solo al principio de la cadena de texto string. Si encuentra una coincidencia al principio de la cadena, devuelve un objeto **Match**. Si no hay coincidencia al **principio de la cadena**, devuelve **None**.

```python
import re

# Función principal: re.match()
# Patrón: Buscar la palabra "apple" solo al principio de la cadena.
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'apple pie is delicious.'

# Buscar coincidencias utilizando la expresión regular con re.match()
matches = re.match(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')

```
En este ejemplo, re.match() encuentra la palabra "apple" al principio de la cadena de texto y devuelve un objeto **Match**.

Ambas funciones son útiles para buscar patrones en cadenas de texto, pero la diferencia principal radica en **dónde comienzan a buscar**. re.search() busca en toda la cadena de texto, mientras que re.match() busca **SOLO al principio de la cadena**. Dependiendo de sus necesidades, puede optar por utilizar una u otra función.

## Métodos de Match

En el contexto de expresiones regulares en Python, cuando se encuentra una coincidencia utilizando las funciones **re.search()** o **re.match()**, el objeto **Match** devuelto contiene varios métodos y atributos útiles para trabajar con la coincidencia. Entre estos métodos y atributos se encuentran **group()**, **start()**, **end()**, y span().

#### start, end, span, group

Los métodos start(), end(), span() y group() son métodos de la clase Match en Python, **no son atributos**. Esto significa que se utilizan llamando a estos métodos en un objeto Match devuelto por las funciones re.search() o re.match().

Entonces, para acceder a estos valores, usamos estos métodos en el objeto Match devuelto por re.search() o re.match().

Aquí está la explicación de cada uno:

1. group(): Este método devuelve la cadena que coincide con el patrón. Si la expresión regular contiene grupos de captura (definidos por paréntesis), group() también puede aceptar un argumento entero para devolver una cadena correspondiente a un grupo específico dentro de la expresión regular. Si no se especifica ningún argumento, group(0) devuelve la cadena completa que coincide con el patrón.

2. start(): Este método devuelve la posición inicial de la coincidencia en la cadena de texto.

3. end(): Este método devuelve la posición final de la coincidencia en la cadena de texto.

4. span(): Este método devuelve una tupla que contiene la posición inicial y la posición final de la coincidencia en la cadena de texto.

Para entender mejor cómo se utilizan estos métodos, aquí tienes un ejemplo que los ilustra:

```python
import re

# Expresión regular y cadena de texto
pattern = r'apple'
text = 'I have an apple and a banana.'

# Buscar coincidencias utilizando re.search()
matches = re.search(pattern, text)

if matches:
    print('Coincidencia encontrada:', matches.group())  # Imprime la cadena que coincide con el patrón
    print('Posición inicial:', matches.start())          # Imprime la posición inicial de la coincidencia
    print('Posición final:', matches.end())              # Imprime la posición final de la coincidencia
    print('Posición inicial y final:', matches.span())   # Imprime la posición inicial y final de la coincidencia

```
La salida de este código proporcionará información sobre la coincidencia encontrada, así como las posiciones inicial y final de la coincidencia en la cadena de texto. Esto puede ser útil para realizar operaciones adicionales en el texto o para obtener información específica sobre la coincidencia encontrada.

 Gracias por señalar el error y lamento la confusión.

## Patrones de expresiones regulares

Las expresiones regulares pueden variar en complejidad y funcionalidad dependiendo de las necesidades específicas del usuario. 

Algunos de los tipos comunes de expresiones regulares incluyen:

1. Caracteres Literales:     
  Son caracteres simples que coinciden exactamente con ellos mismos en una cadena de texto. Por ejemplo, la expresión regular "hello" coincidirá exactamente con la cadena "hello".

2. Metacaracteres:     
  Son caracteres especiales que representan clases de caracteres o realizan funciones especiales. Algunos metacaracteres comunes incluyen:

* .: Coincide con cualquier carácter excepto el salto de línea.
* ^: Coincide con el comienzo de una cadena de texto.
* $: Coincide con el final de una cadena de texto.
* \\: Se utiliza para escapar metacaracteres o para introducir secuencias especiales como \d, \w, etc.

3. Clases de caracteres:     
  Permiten especificar conjuntos de caracteres que coinciden con un solo carácter en la cadena de texto. Algunos ejemplos incluyen:

* \[abc]: Coincide con cualquiera de los caracteres dentro de los corchetes (a, b o c).
* \[0-9]: Coincide con cualquier dígito del 0 al 9.
* \[^0-9]: Coincide con cualquier carácter que no sea un dígito del 0 al 9.

4. Cuantificadores:     
  Especifican cuántas veces debe aparecer un patrón para que se considere una coincidencia. Algunos ejemplos incluyen:

* *: Coincide con cero o más repeticiones del patrón anterior.
* +: Coincide con una o más repeticiones del patrón anterior.
* ?: Coincide con cero o una repetición del patrón anterior.
* {n}: Coincide exactamente con n repeticiones del patrón anterior.
* {m, n}: Coincide con al menos m y como máximo n repeticiones del patrón anterior.

5. Agrupaciones y referencias:     
  Permiten agrupar partes de una expresión regular para aplicar cuantificadores o realizar operaciones específicas. Además, las referencias hacia atrás (\1, \2, etc.) permiten hacer referencia a grupos previamente definidos dentro de la expresión regular.

Estos son solo algunos ejemplos de los tipos de expresiones regulares disponibles en Python y otros lenguajes de programación. La complejidad y la variedad de las expresiones regulares permiten realizar tareas sofisticadas de búsqueda y manipulación de texto.


[Regular Expressions 101](https://regex101.com/) 

[Regular Expressions r ](https://regexr.com/) 

# Threading

Threading, en el contexto de la programación, se refiere a una técnica que permite que un programa realice **múltiples tareas simultáneamente**. Es una forma de ejecución concurrente donde varias partes del programa, llamadas "hilos" (threads en inglés), ejecutan código de forma independiente.

Los hilos comparten recursos comunes, como la memoria, pero tienen su propia pila de ejecución. Esto permite que los hilos trabajen en diferentes partes del programa de forma independiente y, potencialmente, mejoren la eficiencia y la capacidad de respuesta del sistema.

La programación con hilos es especialmente útil en situaciones donde hay tareas que pueden realizarse de manera independiente y paralela, como operaciones de entrada/salida (E/S) o cálculos intensivos.

En Python, puedes trabajar con hilos utilizando el **módulo threading**, que proporciona una interfaz de alto nivel para crear y administrar hilos. Puedes crear hilos mediante la **subclase Thread**, que te permite definir una función o método que será ejecutado en paralelo.

Aquí tienes un ejemplo básico de cómo usar threading en Python:

```python
import threading

# Función que será ejecutada por el hilo
def print_numbers():
    for i in range(5):
        print(i)

# Crear un objeto Thread y asignarle la función
thread = threading.Thread(target=print_numbers)

# Iniciar la ejecución del hilo
thread.start()

# Esperar a que el hilo termine antes de continuar con el código principal
thread.join()

# Continuar con el código principal
print("Hilo finalizado. Continuando con el código principal.")

```

En este ejemplo, creamos un hilo que ejecuta la función print_numbers(). El hilo se **inicia** llamando al método **start()** y se espera a que **termine** su ejecución mediante el método **join()**. Mientras tanto, el código principal continúa ejecutándose en paralelo con el hilo.

# Sockets 

En Python, los sockets son una forma de establecer comunicación entre procesos a través de una red. Los sockets permiten enviar y recibir datos entre dos dispositivos (como dos ordenadores) a través de una red, ya sea localmente en una misma máquina o a través de Internet.

El módulo estándar socket de Python proporciona una interfaz de programación de aplicaciones (API) para trabajar con sockets. Con este módulo, puedes crear sockets tanto para clientes como para servidores.

Aquí tienes un ejemplo básico de cómo crear un servidor y un cliente usando sockets en Python:

**Servidor:**
```python
import socket

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar el socket a un puerto
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(1)

print('Esperando una conexión...')

# Aceptar la conexión entrante
connection, client_address = server_socket.accept()

try:
    print('Conexión establecida desde', client_address)
    
    # Recibir datos del cliente
    data = connection.recv(1024)
    print('Datos recibidos:', data.decode())
    
finally:
    # Cerrar la conexión
    connection.close()

```

**Cliente:**

```python
import socket

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Enviar datos al servidor
    message = 'Hola, servidor!'
    client_socket.sendall(message.encode())
    
finally:
    # Cerrar la conexión
    client_socket.close()

```

En este ejemplo, el servidor espera una conexión entrante en el puerto 12345. Una vez que se establece la conexión, el servidor recibe datos del cliente y los imprime. Mientras tanto, el cliente se conecta al servidor en el mismo puerto y envía un mensaje al servidor.

Estos son solo ejemplos básicos. Los sockets en Python pueden ser utilizados para crear aplicaciones de red más complejas, como servidores web, sistemas de mensajería, transferencia de archivos, etc.

## Explorando las Posibilidades de los Sockets en Python

Los sockets en Python proporcionan una forma de comunicación entre procesos, tanto en la misma máquina como en diferentes máquinas en una red. Los sockets permiten enviar y recibir datos entre aplicaciones, lo que brinda una amplia gama de posibilidades. Aquí hay algunas de las cosas que puedes hacer con sockets en Python:

1. Comunicación Cliente-Servidor:     
  Puedes crear aplicaciones cliente-servidor donde un cliente se conecta a un servidor a través de un socket para enviar o recibir datos. Esto es útil para implementar servicios de red como servidores web, servidores de correo electrónico, servidores de chat, etc.

```python	

```

2. Transferencia de Archivos:     
  Puedes usar sockets para transferir archivos entre diferentes dispositivos en una red. Por ejemplo, puedes crear una aplicación que permita a los usuarios cargar y descargar archivos desde un servidor remoto.

```python	
 # Servidor para transferencia de archivos
import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket a la dirección y puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes
server_socket.listen(1)

print('Servidor escuchando en {}:{}'.format(HOST, PORT))

# Aceptar la conexión
conn, addr = server_socket.accept()
print('Conexión establecida con', addr)

# Recibir archivo del cliente
with open('archivo_recibido.txt', 'wb') as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

# Cerrar conexión
conn.close()
 
```

****************

```python
# Cliente para transferencia de archivos
import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 12345

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
client_socket.connect((HOST, PORT))

# Enviar archivo al servidor
with open('archivo_enviado.txt', 'rb') as file:
    for data in file:
        client_socket.sendall(data)

# Cerrar conexión
client_socket.close()

```

3. Comunicación entre Procesos Locales:     
  Los sockets también pueden utilizarse para la comunicación entre procesos locales en la misma máquina. Esto puede ser útil para crear aplicaciones que se ejecuten en diferentes hilos o procesos y necesiten intercambiar datos entre ellos.

```python	
  # Servidor
import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket a la dirección y puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes
server_socket.listen(1)

print('Servidor escuchando en {}:{}'.format(HOST, PORT))

# Aceptar la conexión
conn, addr = server_socket.accept()
print('Conexión establecida con', addr)

# Enviar mensaje de bienvenida al cliente
conn.sendall(b'Bienvenido al servidor!')

# Cerrar conexión
conn.close()

```

4. Streaming de Datos en Tiempo Real:     
  Los sockets pueden utilizarse para transmitir datos en tiempo real, como audio o video, a través de una red. Esto es útil para aplicaciones de streaming de medios o juegos en línea que requieren una comunicación rápida y eficiente.

```python	
  
```

5. Monitoreo y Control Remoto:     
  Puedes crear aplicaciones que permitan monitorear y controlar dispositivos remotos a través de una red utilizando sockets. Por ejemplo, podrías crear una aplicación para controlar un robot o un sistema de automatización del hogar desde una ubicación remota.

```python	
  
```

6. Comunicación entre Aplicaciones Distribuidas:     
  Los sockets son fundamentales para la comunicación entre diferentes aplicaciones distribuidas en una arquitectura de microservicios o sistemas distribuidos más complejos. Esto permite que las aplicaciones intercambien datos y coordinen su funcionamiento.

```python	
  
```

Estas son solo algunas de las posibilidades que puedes explorar utilizando sockets en Python. La versatilidad de los sockets hace que sean una herramienta poderosa para la programación de redes y la comunicación entre procesos.

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 