# POO / OOP "Object-Oriented Programming" 

POO significa "Programación Orientada a Objetos". 

Es un paradigma de programación que se basa en el concepto de "objetos", 
los cuales son entidades que combinan datos (llamados atributos) y funciones (llamadas métodos) que operan sobre esos datos.

En la programación orientada a objetos, los objetos son instancias de clases,
que son como plantillas o moldes que definen la estructura y el comportamiento de los objetos. 
Las clases pueden contener atributos que representan el estado de los objetos y métodos que definen su comportamiento.

Los principales conceptos de la programación orientada a objetos son:

**Clases y Objetos: (Classes and Objects)**  
Una clase es una plantilla que define la estructura y el comportamiento de los objetos, 
mientras que un objeto es una instancia específica de esa clase.

Una clase define las propiedades (atributos) y el comportamiento (métodos) que tendrán los objetos creados a partir de ella. 

[Más detalles Clases](../sesion11/sesion11.md#class)     

**Atributos: (Attributes)**  
Representan los datos asociados con un objeto y describen su estado.
Los atributos representan los datos asociados con un objeto,

**Métodos: (Methods)**  
Son funciones "def" asociadas con los objetos que definen su comportamiento y operan sobre sus datos.
Mientras que los métodos son funciones que operan sobre esos datos.

 [Más detalles Métodos](../sesion12/sesion12.md)

# 3 Principios Fundamentales POO

En la programación orientada a objetos (POO), hay tres principios fundamentales que constituyen la base del paradigma:

## Encapsulamiento: (Encapsulation)  
Es el concepto de ocultar los detalles internos de un objeto y proporcionar una interfaz clara y consistente para interactuar con él.

Es un principio que se refiere a la agrupación de datos y métodos que operan en esos datos en una única unidad llamada clase. El encapsulamiento oculta los detalles internos de cómo funciona una clase y solo expone una interfaz pública para interactuar con ella. Esto ayuda a prevenir el acceso no autorizado a los datos internos de un objeto y promueve la modularidad y el mantenimiento del código.

[Más detalles Encapsulamiento](sesion11/sesion11.mdencapsulamiento-__--atributo-privado-proteger-datos-1er-principio-poo) 

## Herencia: (Inheritance)  
Permite que una clase herede atributos y métodos de otra clase, 
lo que facilita la reutilización de código y la organización jerárquica de las clases.

Es un principio que permite que una clase (llamada subclase o clase hija) herede atributos y métodos de otra clase (llamada superclase o clase padre). La herencia permite la reutilización de código al permitir que las clases hijas aprovechen la funcionalidad existente de las clases padres. Esto promueve la jerarquía de clases y la relación "es-un" entre las clases, donde una subclase es un tipo especializado de su superclase.

[Más detalles Herencia](sesion13/sesion13.md) 

## Polimorfismo: (Polymorphism)  
Es la capacidad de diferentes objetos de responder a un mismo mensaje de manera diferente, 
lo que permite escribir código más genérico y flexible.

Es un principio que se refiere a la capacidad de un objeto de comportarse de diferentes maneras según el contexto en el que se utilice. Esto se logra mediante la sobrecarga de métodos (métodos con el mismo nombre pero diferentes parámetros) y la sustitución de métodos (una subclase proporciona una implementación específica de un método heredado de su superclase). El polimorfismo permite que los objetos sean tratados de manera uniforme a través de interfaces comunes, independientemente de sus tipos específicos, lo que simplifica el diseño del software y lo hace más flexible y extensible.

[Más detalles Polimorismo](sesion13/sesion13.md) 

Estos tres principios son fundamentales en la POO y se utilizan para crear modelos de datos y sistemas de software modular, eficiente y fácil de mantener.

# Instanciar

Instanciar en el contexto de la programación orientada a objetos significa crear un objeto específico (instancia) de una clase. 
Cuando instancias una clase, estás creando un objeto que tiene su propia copia de los atributos definidos en esa clase, 
así como acceso a los métodos que la clase proporciona.

Por ejemplo, supongamos que tienes una clase llamada Persona que define atributos como nombre, edad, y métodos como caminar, correr, etc. 
Cuando instancias la clase Persona, estás creando un objeto específico que representa a una persona en particular, 
con su propio nombre, edad, y capacidad para caminar, correr, etc.

La instancia es única y diferente de cualquier otra instancia de la misma clase. 
Puedes crear múltiples instancias de una clase, cada una con sus propios datos y comportamiento, 
pero todas compartiendo la misma estructura y definición de la clase original.

En resumen, instanciar una clase significa crear un objeto específico basado en esa clase, con sus propios atributos y métodos. 


# \__init__

\__init__ es un método especial en Python que se llama automáticamente cuando se crea una nueva instancia de una clase. 
Este método se utiliza para inicializar los atributos de la clase y realizar cualquier otra configuración necesaria al momento de la creación del objeto.

El nombre \__init__ es una convención en Python para el constructor de la clase. 
El constructor es un método especial que se ejecuta automáticamente cuando se crea un nuevo objeto de esa clase. 
El doble guion bajo antes y después del nombre (\__init__) indica que es un método especial y predefinido por el lenguaje.

Aquí tienes un ejemplo de cómo se utiliza \__init__ en una clase:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

### Crear una nueva instancia de Persona
persona1 = Persona("Juan", 30)

### Llamar al método saludar
persona1.saludar()

```

En este ejemplo, cuando se crea una nueva instancia de Persona (persona1), se llama automáticamente al método \__init__ con los argumentos proporcionados ("Juan" y 30). 
Dentro de \__init__, se inicializan los atributos nombre y edad de la instancia con los valores proporcionados.

[Más detalles Método Mágico](sesion11/sesion11.md#método-mágico) 

# self

self es una convención utilizada para referirse al objeto mismo dentro de los métodos de una clase. 
Cuando defines métodos en una clase, el primer parámetro de cada método debe ser self. 
Este parámetro representa la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de esa instancia.

Por ejemplo, considera la siguiente clase Persona:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
```
        
En este ejemplo, 

**self** se utiliza dentro del método saludar() para acceder a los atributos nombre y edad de la instancia actual de Persona. 
Cuando se llama al método saludar(), se llama así: persona.saludar(), y self en el contexto de esa llamada se refiere a la instancia específica de Persona en la que se llamó al método.

En resumen, **self** en Python es una referencia a la instancia actual de una clase y se utiliza dentro de los métodos de la clase para acceder a los atributos y métodos de esa instancia. 
Es una convención de nomenclatura y no un palabra clave del lenguaje, por lo que podrías llamarlo de otra manera, aunque self es altamente recomendado por convención.

# \*

El asterisco "*"" se utiliza en diferentes contextos para realizar diferentes operaciones.

Aquí tienes algunas de las formas más comunes en las que se usa:

1. Desempaquetado de argumentos (unpacking): 

Se utiliza para desempaquetar iterables, como listas o tuplas, en argumentos individuales de una función.
```python
def suma(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
resultado = suma(*numeros)  # Equivalente a suma(1, 2, 3)
print(resultado)  # Output: 6

```

2. Empaquetado de argumentos (packing): 
   Se utiliza para empaquetar argumentos de una función en una tupla.
```python
def mostrar_numeros(*args):
    for numero in args:
        print(numero)

mostrar_numeros(1, 2, 3)  # Output: 1\n2\n3
```
3. Definición de argumentos variables: 
   Se utiliza en la definición de funciones para indicar que una función puede aceptar un número variable de argumentos.
```python
def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = suma(1, 2, 3, 4)  # Puede aceptar cualquier cantidad de números
print(resultado)  # Output: 10
```

4. Desempaquetado de secuencias: 
   Se utiliza para desempaquetar secuencias (listas, tuplas, etc.) en variables individuales.
```python
numeros = [1, 2, 3]
a, b, c = numeros
print(a, b, c)  # Output: 1 2 3
```

En resumen, el asterisco "*"" en Python se utiliza en varios contextos para realizar operaciones como:
* desempaquetar argumentos, 
* empaquetar argumentos, 
* definir argumentos variables o 
* desempaquetar secuencias.

