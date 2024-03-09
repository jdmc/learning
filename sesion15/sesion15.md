[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Generadores 

Los generadores en Python son una forma poderosa y eficiente de trabajar con secuencias de datos de manera perezosa, es decir, generan valores sobre la marcha en lugar de almacenarlos todos en la memoria al mismo tiempo. Los generadores permiten iterar sobre grandes conjuntos de datos de manera eficiente sin la necesidad de almacenar todos los valores en la memoria al mismo tiempo, lo que puede ser útil para conjuntos de datos potencialmente infinitos o para optimizar el uso de la memoria en general.

En Python, los generadores se crean utilizando funciones generadoras o expresiones generadoras. 

Aquí hay dos formas comunes de crear generadores:

## Funciones generadoras: 

  Son funciones que utilizan la palabra clave **yield** en lugar de return. Cuando una función generadora se llama, devuelve un objeto generador que puede iterarse para producir los valores generados por la función.

```python
def generador():
    yield 1
    yield 2
    yield 3

gen = generador()
for valor in gen:
    print(valor)  # Salida: 1, 2, 3
```

##  Expresiones generadoras: 

  Son expresiones que generan secuencias de valores sobre la marcha utilizando la sintaxis similar a la comprensión de listas, pero con paréntesis en lugar de corchetes. Se utilizan para crear generadores de manera más concisa.

```python
gen = (x for x in range(1, 4))
for valor in gen:
    print(valor)  # Salida: 1, 2, 3

```

En ambos casos, los generadores producen valores sobre la marcha a medida que se solicitan, lo que puede ser más eficiente en términos de uso de memoria y puede permitir trabajar con conjuntos de datos grandes o infinitos. Los generadores son una característica poderosa de Python que facilita el manejo de flujos de datos de manera eficiente y elegante.


### stop iteration

Cuando iteras sobre un generador y este ha agotado todos sus elementos, se produce una excepción llamada StopIteration. Esta excepción es internamente manejada por Python y se utiliza para señalar que no hay más elementos para iterar en el generador.

Aquí tienes un ejemplo práctico que muestra cómo se produce la excepción StopIteration al iterar sobre un generador:

```python
def generador():
    yield 1
    yield 2
    yield 3

gen = generador()

# Iterar sobre el generador
try:
    while True:
        valor = next(gen)
        print(valor)
except StopIteration:
    print("Se alcanzó el final del generador.")

```
En este ejemplo:

* Definimos una función generadora llamada generador() que produce tres valores.
* Creamos un objeto generador llamado gen llamando a la función generador().
* Iteramos sobre el generador utilizando un bucle while y la función next(), que obtiene el siguiente valor del generador en cada iteración.
* Cuando el generador se agota y no hay más elementos para iterar, se produce la excepción StopIteration.
* Capturamos la excepción utilizando un bloque try y except, e imprimimos un mensaje indicando que se alcanzó el final del generador.

Este ejemplo ilustra cómo Python maneja internamente la excepción StopIteration cuando iteras sobre un generador y no hay más elementos disponibles.

# Iteradores PART 2

para una comprensión más avanzada de los iteradores en Python, podemos profundizar en algunos conceptos adicionales. Los iteradores en Python son objetos que representan una secuencia de datos y permiten el acceso a elementos de esta secuencia de manera secuencial. Aquí hay algunos aspectos más avanzados sobre los iteradores:

## Protocolo del iterador en Python:
El protocolo del iterador en Python se basa en dos métodos especiales:

* \__iter__(): Este método devuelve el propio objeto iterador. Puede ser útil si deseas que un objeto sea tanto un iterable como un iterador.

* \__next__(): Este método devuelve el próximo elemento de la secuencia. Cuando no hay más elementos en la secuencia, debe lanzar la excepción StopIteration.

## Implementación de un iterador personalizado:
Puedes crear tu propio iterador personalizado implementando una clase que tenga los métodos __iter__() y __next__(). Esto es útil cuando necesitas iterar sobre una secuencia de datos de una manera específica que no se puede lograr con las estructuras de datos integradas.

## Generadores:
Los generadores son una forma conveniente de crear iteradores en Python. Puedes crear un generador utilizando la sintaxis de comprensión de listas o con la palabra clave yield. Los generadores permiten la iteración perezosa, lo que significa que los elementos se generan bajo demanda, lo que ahorra memoria y mejora el rendimiento en comparación con la generación de todos los elementos de antemano.

## Funciones de iteración avanzadas:
Python ofrece funciones de iteración avanzadas que pueden trabajar con iteradores, como map(), filter(), zip(), enumerate() y itertools. Estas funciones proporcionan formas poderosas y expresivas de manipular y trabajar con secuencias de datos.

## Iteración infinita:
Python permite la creación de iteradores que pueden generar una secuencia infinita de elementos. Estos iteradores pueden ser útiles en situaciones donde necesitas procesar una secuencia de datos potencialmente infinita o cuando necesitas modelar conceptos matemáticos como números primos o secuencias de Fibonacci.

## Context Managers y el protocolo \__enter__ y \__exit__:
Los context managers en Python, implementados mediante los métodos especiales \__enter__() y \__exit__(), pueden ser utilizados para administrar recursos y establecer y liberar el estado de un iterador de manera controlada. Esto es útil para la gestión de archivos, conexiones de red u otras operaciones que requieren limpieza y administración de recursos.

## Iteración asíncrona:
Con la introducción de asyncio en Python, también puedes encontrar iteradores asincrónicos que te permiten iterar sobre secuencias de datos de manera asíncrona, lo que es útil en aplicaciones que involucran E/S intensiva o tareas de red.

Estos son solo algunos de los aspectos más avanzados relacionados con los iteradores en Python. Comprender estos conceptos puede ayudarte a aprovechar al máximo las capacidades de iteración en el lenguaje y a escribir código más eficiente y expresivo.


# Decoradores PART 2

Los decoradores en Python son una herramienta poderosa y flexible que te permite modificar o extender el comportamiento de funciones o métodos sin cambiar su código. Aquí te explico cómo puedes usar decoradores de manera más avanzada, junto con ejemplos:

## 1. Decoradores de funciones anidados:
Puedes definir un decorador como una función anidada dentro de otra función. Esto te permite aceptar argumentos adicionales o realizar tareas de inicialización antes de aplicar el decorador a una función específica.

```python
def decorador_con_argumentos(arg1, arg2):
    def decorador(func):
        def wrapper(*args, **kwargs):
            # Hacer algo antes de llamar a la función
            print("Argumentos del decorador:", arg1, arg2)
            resultado = func(*args, **kwargs)
            # Hacer algo después de llamar a la función
            return resultado
        return wrapper
    return decorador

@decorador_con_argumentos("Hola", "Mundo")
def mi_funcion():
    print("¡Hola, Mundo!")

mi_funcion()

```
### función anidada

Una función anidada en Python es simplemente una función definida dentro de otra función. Esto significa que la función interna está definida y existe dentro del ámbito de la función externa. La función anidada puede acceder a las variables locales de la función externa, así como a cualquier variable global disponible en el ámbito global.

Aquí tienes un ejemplo de una función anidada:

```python
def funcion_externa():
    def funcion_interna():
        print("Esta es una función anidada.")
    
    funcion_interna()  # Llamada a la función anidada dentro de la función externa

# Llamada a la función externa
funcion_externa()


```
En este ejemplo, funcion_interna es una función anidada dentro de funcion_externa. Cuando llamamos a funcion_externa(), también se ejecuta el código dentro de funcion_interna(), ya que está definido dentro de funcion_externa() y tiene acceso a su ámbito.

Las funciones anidadas son útiles para encapsular lógica relacionada y pueden ayudar a mantener el código más organizado y modular. Además, son comunes en el contexto de los decoradores y los HOF (funciones de orden superior), donde se utilizan para definir comportamientos adicionales o envolver otras funciones.

## 2. Decoradores de clase:

Además de decorar funciones, puedes decorar métodos de clases. Esto te permite modificar el comportamiento de métodos específicos en una clase.

```python
def decorador_de_metodo(func):
    def wrapper(self, *args, **kwargs):
        # Hacer algo antes de llamar al método
        print("Antes de llamar al método:", func.__name__)
        resultado = func(self, *args, **kwargs)
        # Hacer algo después de llamar al método
        print("Después de llamar al método:", func.__name__)
        return resultado
    return wrapper

class MiClase:
    @decorador_de_metodo
    def mi_metodo(self):
        print("En el método")

objeto = MiClase()
objeto.mi_metodo()

```

##  3. Decoradores de clase con argumentos:

Puedes definir decoradores de clase que acepten argumentos adicionales, lo que te brinda aún más flexibilidad al aplicar el decorador a diferentes métodos.

```python
class DecoradorDeClaseConArgumentos:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("Argumentos del decorador de clase:", self.arg1, self.arg2)
            resultado = func(*args, **kwargs)
            return resultado
        return wrapper

@DecoradorDeClaseConArgumentos("Hola", "Mundo")
def mi_funcion():
    print("¡Hola, Mundo!")

mi_funcion()

```

Estos son solo algunos ejemplos de cómo puedes usar decoradores de manera más avanzada en Python. Los decoradores te permiten implementar patrones comunes de diseño, como la decoración, la inyección de dependencias, la gestión de recursos y la validación de argumentos, de una manera elegante y reutilizable.

## High Order Function (HOF)

Los HOF (High Order Functions o Funciones de Orden Superior) son aquellas funciones que pueden aceptar otras funciones como argumentos y/o devolver funciones como resultado. En Python, los HOF son una parte fundamental de la programación funcional y se pueden combinar de manera poderosa con decoradores para crear abstracciones más complejas y reutilizables. 

Aquí tienes un ejemplo de cómo podrías utilizar un HOF junto con un decorador:

Supongamos que tienes un HOF llamado crear_decorador que toma una función de transformación como argumento y devuelve un decorador que aplica esa función a los resultados de otra función:

```python
def crear_decorador(funcion_de_transformacion):
    def decorador(funcion_a_decorar):
        def wrapper(*args, **kwargs):
            resultado = funcion_a_decorar(*args, **kwargs)
            return funcion_de_transformacion(resultado)
        return wrapper
    return decorador

# Definimos una función de transformación
def duplicar(numero):
    return numero * 2

# Creamos un decorador que aplica la función de transformación
@crear_decorador(duplicar)
def sumar(a, b):
    return a + b

# Probamos nuestra función decorada
resultado = sumar(3, 4)
print(resultado)  # Salida: 14 (7 * 2)

```
En este ejemplo, crear_decorador es nuestro HOF, ya que toma una función funcion_de_transformacion como argumento y devuelve un decorador. Este decorador aplica la función de transformación (duplicar) al resultado de la función a decorar (sumar). Así, la función sumar decorada devuelve el resultado de la suma multiplicado por 2.

Este es solo un ejemplo básico de cómo los HOF pueden combinarse con decoradores para crear abstracciones más complejas y reutilizables en Python. Con HOF y decoradores, puedes construir estructuras de código altamente modulares y expresivas que sean fácilmente adaptables a diferentes situaciones y requisitos.

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md)  



