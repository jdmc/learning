[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Listas

Las listas en Python son un tipo de dato que se utiliza para almacenar una colección ordenada y mutable de elementos.

Las listas se definen entre corchetes y los elementos se separan por comas.

```python

mi_lista = ["Hola", 1, True]

```

En este ejemplo, se crea una lista con tres elementos: una cadena, un número entero y un valor booleano.

Las listas son muy versátiles y se pueden usar para almacenar cualquier tipo de dato, incluso otras listas.

Las listas son mutables, lo que significa que se pueden modificar los elementos de una lista después de que se ha creado.

Se puede **agregar**, **eliminar** o **modificar** elementos de una lista.

Las listas son una herramienta poderosa para organizar y almacenar datos en Python.

Aquí hay algunos ejemplos de cómo se pueden usar las listas:

* Almacenar una lista de nombres.
* Almacenar una lista de números.
* Almacenar una lista de tareas.

Las listas son una herramienta fundamental para el desarrollo de aplicaciones en Python.

# Append

append() es un método que se utiliza para agregar un elemento al final de una lista en Python.

El método append() toma un solo argumento, que es el elemento que se desea agregar a la lista.

Ejemplo:

```python
mi_lista = ["Hola", 1, True]

mi_lista.append("nuevo elemento")

print(mi_lista)

```
 En este ejemplo, se agrega el elemento "nuevo elemento" al final de la lista mi_lista. 

La lista final será ["Hola", 1, True, "nuevo elemento"].

El método append() es una forma sencilla de agregar elementos a una lista.

Es importante tener en cuenta que el método append() no devuelve ningún valor.

Aquí hay algunos ejemplos adicionales de cómo se puede usar el método append():

* Agregar un número al final de una lista de números.
* Agregar una cadena al final de una lista de cadenas.
* Agregar una lista al final de una lista de listas.

El método append() es una herramienta útil para trabajar con listas en Python.

# Funciones 

En Python, una función es un bloque de código reutilizable que se utiliza para realizar una tarea específica. Las funciones permiten dividir el código en partes más pequeñas y manejables, lo que facilita la organización, comprensión y reutilización del código.

Una función en Python generalmente tiene la siguiente estructura:

```python
def nombre_de_la_funcion(parametros):
    """Documentación de la función (docstring)"""
    # Cuerpo de la función
    # Realiza alguna tarea con los parámetros
    return resultado

```
* **def** es la palabra clave y reservada que se utiliza para definir una función.
* **nombre_de_la_funcion** es el nombre de la función, que se utiliza para llamar a la función más tarde.
* **parametros** son los valores que la función espera recibir cuando se llama. Pueden ser opcionales.
* La cadena de texto entre triple comillas **"""** es la documentación de la función, también conocida como docstring. Proporciona una descripción de lo que hace la función.
* El cuerpo de la función contiene las instrucciones que se ejecutarán cuando se llame a la función.
* **return** es la palabra clave utilizada para devolver un valor de la función. Puede devolver un solo valor o una tupla de valores.

Aquí hay un ejemplo simple de una función que suma dos números:

```python
def suma(a, b):
    """Esta función suma dos números"""
    resultado = a + b
    return resultado

# Llamamos a la función y mostramos el resultado
print(suma(3, 5))  # Imprime 8

```
En este ejemplo, la función **suma** toma dos parámetros a y b, suma estos dos valores y devuelve el resultado. Luego, llamamos a la función con los argumentos 3 y 5, lo que devuelve 8, que se imprime.


## Funcionamiento de las funciones

El funcionamiento de las funciones en Python es bastante sencillo y sigue algunos pasos básicos. Aquí está una descripción general del funcionamiento de las funciones en Python:

1. Definición de la función:     
  Primero, defines la función utilizando la palabra clave **def**, seguida del nombre de la función y los parámetros entre paréntesis. Puedes incluir un bloque de código en el cuerpo de la función que realiza una tarea específica.

```python
def mi_funcion(parametro1, parametro2):
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado

```

2. Llamada a la función:     
  Para ejecutar el código dentro de la función y obtener un resultado, necesitas llamar a la función. Puedes llamar a una función pasando valores conocidos como argumentos.

```python
resultado = mi_funcion(5, 3)

```
En este ejemplo, estamos llamando a la función mi_funcion y pasando los valores 5 y 3 como argumentos. El resultado devuelto por la función se asigna a la variable resultado. 

3. Ejecución del código en la función:     
  Cuando llamas a la función, Python ejecuta el código dentro del cuerpo de la función utilizando los valores proporcionados como argumentos. Dentro de la función, puedes realizar cualquier tarea deseada utilizando los parámetros proporcionados y otras variables.

4. Retorno de valores:     
  Si la función incluye una declaración de retorno (return), el valor especificado en la declaración de retorno se devuelve a la ubicación de la llamada a la función. Esto permite que la función proporcione resultados útiles que pueden ser utilizados en otros lugares del programa.

5. Finalización de la función: 
  Una vez que la función ha completado su tarea y ha devuelto un valor (si es necesario), la ejecución del programa continúa desde el punto donde se realizó la llamada a la función.

> En resumen, las funciones en Python son bloques de código reutilizables que aceptan entradas, realizan operaciones basadas en esas entradas y pueden devolver un resultado. Esto permite que el código sea más modular, más fácil de entender y más fácil de mantener.

## Funciones parametrizadas

Las funciones parametrizadas, también conocidas como funciones con parámetros, son funciones que aceptan uno o más valores (parámetros) que se pasan cuando la función es llamada. Estos parámetros proporcionan datos a la función que pueden ser utilizados dentro del cuerpo de la función para realizar operaciones específicas.

En Python, puedes definir funciones que acepten cualquier número de parámetros. Estos parámetros se colocan entre paréntesis en la definición de la función y se utilizan como variables dentro del cuerpo de la función. Cuando llamas a la función, proporcionas valores para estos parámetros, que se utilizan como datos de entrada para la función.

Por ejemplo, considera esta función simple en Python:

```python
def saludar(nombre):
    print("¡Hola,", nombre, "!")

```
En esta función, nombre es un parámetro que se utiliza para recibir un valor cuando la función saludar() es llamada. Puedes llamar a esta función con diferentes nombres para saludar a diferentes personas:

```python
saludar("Juan")  # Imprime "¡Hola, Juan !"
saludar("María")  # Imprime "¡Hola, María !"

```
Aquí, cada vez que llamamos a la función saludar(), pasamos un nombre diferente como argumento, y ese nombre se utiliza dentro de la función como el valor del parámetro nombre.

```python
def suma(a, b):
    """Esta función suma dos números."""
    resultado = a + b
    return resultado

```

En esta función suma(a, b), hay dos parámetros: a y b. Cuando llamas a esta función, necesitas proporcionar dos valores como argumentos. 

Por ejemplo:

```python
resultado = suma(5, 3)
print(resultado)  # Imprime 8

```
En este caso, 5 se pasa como el primer argumento (a) y 3 se pasa como el segundo argumento (b). Dentro de la función, estos valores se suman y el resultado, 8, se devuelve y se asigna a la variable resultado.

Puedes llamar a la función suma() con diferentes pares de valores como argumentos, y la función sumará los valores correspondientes en cada llamada. 

Por ejemplo:

```python
resultado = suma(10, 20)
print(resultado)  # Imprime 30

resultado = suma(-3, 8)
print(resultado)  # Imprime 5

```
En cada caso, la función suma() toma los dos valores pasados como argumentos, los suma y devuelve el resultado correspondiente. 
Esto muestra cómo puedes definir y utilizar una función con varios parámetros en Python.

>En resumen, las funciones parametrizadas son funciones que aceptan parámetros o argumentos cuando son llamadas, permitiendo que se realicen operaciones específicas en función de los valores proporcionados. Esto hace que las funciones sean más flexibles y reutilizables, ya que pueden trabajar con diferentes conjuntos de datos sin necesidad de modificar el código de la función en sí.

### Paso de parámetros posicionales
El paso de parámetros posicionales es un método común de pasar argumentos a una función en Python. En este enfoque, los valores pasados como argumentos se asignan a los parámetros de la función basándose en su posición en la lista de argumentos.

Cuando llamas a una función y proporcionas argumentos, estos argumentos se asignan a los parámetros de la función en el **mismo orden** en el que se pasan. Por lo tanto, el primer argumento se asigna al primer parámetro, el segundo argumento al segundo parámetro, y así sucesivamente.

Aquí tienes un ejemplo de paso de parámetros posicionales:

```python
def saludar(nombre, apellido):
    print("¡Hola,", nombre, apellido, "!")

```
Cuando llamas a esta función, debes proporcionar dos valores: uno para nombre y otro para apellido, en ese orden. 

Por ejemplo:

```python
saludar("Juan", "Pérez")  # Imprime "¡Hola, Juan Pérez !"

```
En este ejemplo, "Juan" se pasa como el primer argumento, por lo que se asigna al parámetro nombre, y "Pérez" se pasa como el segundo argumento, por lo que se asigna al parámetro apellido.

El paso de parámetros posicionales es el método más común de pasar argumentos a una función en Python y es bastante intuitivo. Sin embargo, debes asegurarte de pasar los argumentos en el orden correcto para evitar errores en la ejecución de tu código.

### Paso de argumentos con palabra clave

El paso de argumentos con palabra clave es otra forma de pasar argumentos a una función en Python. En este enfoque, en lugar de depender del orden de los argumentos para asignar valores a los parámetros de la función, **especificas explícitamente** qué parámetro debe recibir qué valor utilizando el nombre del parámetro.

Para utilizar el paso de argumentos con palabra clave, al llamar a una función, proporcionas los argumentos junto con el nombre del parámetro al que deseas asignar ese valor. Esto ofrece una mayor claridad y flexibilidad en comparación con el paso de argumentos por posición, ya que puedes especificar los valores de los parámetros en cualquier orden.

Aquí tienes un ejemplo de paso de argumentos con palabra clave:

```python
def saludar(nombre, apellido):
    print("¡Hola,", nombre, apellido, "!")

```

Cuando llamas a esta función, puedes pasar los argumentos utilizando la sintaxis nombre=valor:

```python
saludar(apellido="Pérez", nombre="Juan")  # Imprime "¡Hola, Juan Pérez !"

```
En este ejemplo, estamos llamando a la función saludar() y pasando los argumentos utilizando la palabra clave nombre y apellido. Esto asegura que los valores se asignen correctamente a los parámetros nombre y apellido de la función, independientemente del orden en que se pasen los argumentos.

El paso de argumentos con palabra clave proporciona una mayor claridad en el código y evita confusiones al especificar los valores de los parámetros. También permite omitir argumentos opcionales y proporcionar solo los valores que son relevantes para la llamada de la función.


## Argumento

En Python, un argumento se refiere a **un valor que se pasa a una función o método cuando se llama**. Los argumentos proporcionan los datos que la función necesita para **realizar su tarea**. Dependiendo de cómo se defina la función, puede aceptar diferentes tipos de argumentos:

## Argumentos posicionales: 
Son los argumentos que se pasan a una función en el mismo orden en que están definidos en la firma de la función. Por ejemplo:

```python
def saludar(nombre, saludo):
    print(f"{saludo}, {nombre}!")

# Llamada a la función con argumentos posicionales
saludar("Juan", "Hola")

```
En este caso, "Juan" se pasa como el primer argumento (nombre) y "Hola" como el segundo argumento (saludo).

## Argumentos de palabra clave: 

Son los argumentos que se pasan a una función utilizando su nombre, lo que permite especificar los valores para parámetros específicos independientemente de su posición. Por ejemplo:

```python

saludar(saludo="Hola", nombre="María")

```
En este caso, los nombres de los parámetros (nombre y saludo) se utilizan para asociar los valores pasados a la función.

## Argumentos por defecto:

Son argumentos que tienen un valor predeterminado establecido en la firma de la función. Si no se proporciona un valor para estos argumentos al llamar a la función, se utilizará el valor predeterminado. Por ejemplo:

```python
def contar_hasta(numero, inicio=1):
    for i in range(inicio, numero + 1):
        print(i)

# Llamada a la función con un solo argumento
contar_hasta(5)

```
En este caso, el argumento inicio tiene un valor predeterminado de 1, por lo que si no se proporciona un segundo argumento al llamar a contar_hasta(), la cuenta comenzará desde 1.

Los argumentos en Python son extremadamente versátiles y pueden combinarse de varias maneras para proporcionar flexibilidad en la definición y llamada de funciones.

# Iteracion, Iterar, Iterable, Iteradores

Iterar es el proceso de recorrer elementos en una secuencia uno por uno. Un objeto iterable es aquel que se puede recorrer o iterar, es decir, que se puede utilizar en un bucle para acceder a sus elementos secuencialmente. Los iteradores son objetos que facilitan la iteración sobre un iterable, manteniendo un estado interno que recuerda el elemento actual en la secuencia y permite avanzar al siguiente elemento.

Un objeto iterable en Python es cualquier objeto que implemente el método \__iter__(), que devuelve un iterador. Por otro lado, un iterador en Python es cualquier objeto que implemente el método \__next__(), que devuelve el siguiente elemento de la secuencia o lanza una excepción StopIteration cuando se alcanza el final de la secuencia.

Aquí tienes un ejemplo para entender mejor estos conceptos:

```python
# Creamos una lista, que es un objeto iterable
mi_lista = [1, 2, 3, 4, 5]

# Creamos un iterador a partir de la lista
mi_iterador = iter(mi_lista)

# Iteramos sobre los elementos utilizando el iterador
while True:
    try:
        # Obtenemos el siguiente elemento del iterador
        elemento = next(mi_iterador)
        print(elemento)
    except StopIteration:
        # Cuando se alcanza el final de la lista, se lanza StopIteration
        break

```

En este ejemplo, mi_lista es un objeto iterable, y mi_iterador es un iterador creado a partir de la lista. Luego, utilizamos un bucle while junto con el método next() para iterar sobre los elementos de la lista utilizando el iterador. Cada llamada a next() devuelve el siguiente elemento de la lista, y cuando se alcanza el final de la lista, se lanza la excepción StopIteration, lo que nos permite salir del bucle.

Aquí está la secuencia de eventos:

1. Tenemos un objeto iterable, que en este caso es una lista (mi_lista).
2. Creamos un iterador a partir de este objeto iterable usando la función iter() (mi_iterador = iter(mi_lista)).
3. Utilizamos un bucle while para iterar sobre los elementos del iterable.
4. En cada iteración del bucle, llamamos a next() para obtener el siguiente elemento del iterador (elemento = next(mi_iterador)).
5. Cuando alcanzamos el final del iterable y no hay más elementos para iterar, next() lanza una excepción StopIteration.
6. Capturamos esta excepción usando un bloque try-except, lo que nos permite salir del bucle while y finalizar la iteración.

Entonces, efectivamente, el bucle while es responsable de mantener la iteración mientras haya elementos en el iterable. Y repetimos la iteración accediendo al siguiente elemento en cada iteración del bucle hasta que alcanzamos el final del iterable.