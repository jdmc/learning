""" POO / OOP "Object-Oriented Programming" 

POO significa "Programación Orientada a Objetos". 

Es un paradigma de programación que se basa en el concepto de "objetos", 
los cuales son entidades que combinan datos (llamados atributos) y funciones (llamadas métodos) que operan sobre esos datos.

En la programación orientada a objetos, los objetos son instancias de clases,
que son como plantillas o moldes que definen la estructura y el comportamiento de los objetos. 
Las clases pueden contener atributos que representan el estado de los objetos y métodos que definen su comportamiento.

Los principales conceptos de la programación orientada a objetos son:

Clases y Objetos: (Classes and Objects)
Una clase es una plantilla que define la estructura y el comportamiento de los objetos, 
mientras que un objeto es una instancia específica de esa clase.

Una clase define las propiedades (atributos) y el comportamiento (métodos) que tendrán los objetos creados a partir de ella. 

Atributos: (Attributes)
Representan los datos asociados con un objeto y describen su estado.
Los atributos representan los datos asociados con un objeto,

Métodos: (Methods)
Son funciones "def" asociadas con los objetos que definen su comportamiento y operan sobre sus datos.
Mientras que los métodos son funciones que operan sobre esos datos.

**********************************
Encapsulamiento: (Encapsulation)
Es el concepto de ocultar los detalles internos de un objeto y proporcionar una interfaz clara y consistente para interactuar con él.

Herencia: (Inheritance)
Permite que una clase herede atributos y métodos de otra clase, 
lo que facilita la reutilización de código y la organización jerárquica de las clases.

Polimorfismo: (Polymorphism)
Es la capacidad de diferentes objetos de responder a un mismo mensaje de manera diferente, 
lo que permite escribir código más genérico y flexible.
***********************************

#Instanciar

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


# __init__

__init__ es un método especial en Python que se llama automáticamente cuando se crea una nueva instancia de una clase. 
Este método se utiliza para inicializar los atributos de la clase y realizar cualquier otra configuración necesaria al momento de la creación del objeto.

El nombre __init__ es una convención en Python para el constructor de la clase. 
El constructor es un método especial que se ejecuta automáticamente cuando se crea un nuevo objeto de esa clase. 
El doble guion bajo antes y después del nombre (__init__) indica que es un método especial y predefinido por el lenguaje.

Aquí tienes un ejemplo de cómo se utiliza __init__ en una clase:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una nueva instancia de Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar
persona1.saludar()

En este ejemplo, cuando se crea una nueva instancia de Persona (persona1), se llama automáticamente al método __init__ con los argumentos proporcionados ("Juan" y 30). 
Dentro de __init__, se inicializan los atributos nombre y edad de la instancia con los valores proporcionados.

# self

self es una convención utilizada para referirse al objeto mismo dentro de los métodos de una clase. 
Cuando defines métodos en una clase, el primer parámetro de cada método debe ser self. 
Este parámetro representa la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de esa instancia.

Por ejemplo, considera la siguiente clase Persona:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
En este ejemplo, 
self se utiliza dentro del método saludar() para acceder a los atributos nombre y edad de la instancia actual de Persona. 
Cuando se llama al método saludar(), se llama así: persona.saludar(), y self en el contexto de esa llamada se refiere a la instancia específica de Persona en la que se llamó al método.

En resumen, self en Python es una referencia a la instancia actual de una clase y se utiliza dentro de los métodos de la clase para acceder a los atributos y métodos de esa instancia. 
Es una convención de nomenclatura y no un palabra clave del lenguaje, por lo que podrías llamarlo de otra manera, aunque self es altamente recomendado por convención.

# *

El asterisco * se utiliza en diferentes contextos para realizar diferentes operaciones.

Aquí tienes algunas de las formas más comunes en las que se usa:

1.Desempaquetado de argumentos (unpacking): 
Se utiliza para desempaquetar iterables, como listas o tuplas, en argumentos individuales de una función.

def suma(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
resultado = suma(*numeros)  # Equivalente a suma(1, 2, 3)
print(resultado)  # Output: 6


2.Empaquetado de argumentos (packing): 
Se utiliza para empaquetar argumentos de una función en una tupla.

def mostrar_numeros(*args):
    for numero in args:
        print(numero)

mostrar_numeros(1, 2, 3)  # Output: 1\n2\n3

3.Definición de argumentos variables: 
Se utiliza en la definición de funciones para indicar que una función puede aceptar un número variable de argumentos.

def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = suma(1, 2, 3, 4)  # Puede aceptar cualquier cantidad de números
print(resultado)  # Output: 10

4.Desempaquetado de secuencias: Se utiliza para desempaquetar secuencias (listas, tuplas, etc.) en variables individuales.

numeros = [1, 2, 3]
a, b, c = numeros
print(a, b, c)  # Output: 1 2 3

En resumen, el asterisco * en Python se utiliza en varios contextos para realizar operaciones como:
desempaquetar argumentos, 
empaquetar argumentos, 
definir argumentos variables o 
desempaquetar secuencias.

"""
from escuela import Escuela
from curso import Curso
from asignatura import Asignatura
from alumno import Alumno

if __name__ == "__main__":
    pass
    #crear una escuela
    pue = Escuela("PUE", "Fernando") #instanciar el objeto pue a partir de la clase Escuela
    print(pue.nombre)
    print(pue.director)
    
    # >> Escuela >>> crear los cursos de esa escuela y asociarlos a la misma
    python_essentials_1 = Curso("PCAP1")
    python_essentials_2 = Curso("PCAP2")
    pue.anyadir_curso(python_essentials_1)
    pue.anyadir_curso(python_essentials_2)

    
    #  >> Escuela >>> asignaturas
    mates = Asignatura("Matematicas", 6.8)
    ingles = Asignatura("Ingles", 6.0)
    programacion = Asignatura("Programacion", 7.0)
    


    #  >> Escuela >>> crear los alumnos de los cursos de la escuela
    juan = Alumno('Juan Palomo',23,123)
    maria = Alumno('Maria Pelaez', 22, 1234)
    luis = Alumno('Luis Aute',21,12345)
    alicia = Alumno('Alicia Perez', 21, 123456)
    jaime = Alumno('Jaime Urrutia',24,1234567)

    python_essentials_1.matricular(juan, maria, luis)
    python_essentials_2.matricular(alicia, jaime)

    python_essentials_1.matricular_asignaturas(mates, ingles)
    python_essentials_2.matricular_asignaturas(programacion)
    
     #>> Escuela >>> 
     
    #matricularais en python_essentials_2 dos alumnos mas
    #al listar,  que apareciera el nombre del curso

    #listar alumnos actuales
    pue.listar_alumnos()
    

    #asociar los alumnos a las asignaturas