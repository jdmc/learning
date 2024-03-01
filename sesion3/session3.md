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

# Argumento

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