# Introspección

La introspección en Python se refiere a la capacidad de un programa para examinar y hacer consultas sobre tipos, atributos y métodos de objetos durante la ejecución. En otras palabras, la introspección permite a un programa examinarse a sí mismo y obtener información sobre su estructura y componentes en tiempo de ejecución.

Python ofrece varias herramientas y características que facilitan la introspección:

1. Funciones integradas:     
  Python proporciona varias funciones integradas que permiten inspeccionar objetos y sus atributos. Algunas de estas funciones incluyen dir(), vars(), type(), getattr(), hasattr(), entre otras.

2. Atributos especiales:     
  Los objetos en Python pueden tener atributos especiales que proporcionan información sobre sí mismos. Por ejemplo, el atributo \__class__ proporciona una referencia a la clase de un objeto, el atributo \__dict__ contiene un diccionario que representa los atributos del objeto, y así sucesivamente.

3. Módulos de reflexión:     
  Python tiene módulos específicos que facilitan la introspección. Por ejemplo, el módulo inspect proporciona funciones para obtener información sobre los objetos y sus estructuras.

4. Documentación integrada:     
  Muchas bibliotecas y marcos de trabajo en Python están diseñados con la introspección en mente y proporcionan una documentación exhaustiva y detallada que describe la estructura y el comportamiento de sus componentes.

La introspección es útil en una variedad de situaciones, como depuración de código, inspección de objetos en tiempo de ejecución, generación dinámica de código, pruebas unitarias, entre otros. Permite a los desarrolladores explorar y comprender el funcionamiento interno de sus programas, lo que a menudo conduce a un desarrollo más eficiente y a la resolución más rápida de problemas.

## funciones y atributos

Python ofrece varias funciones y atributos integrados que facilitan la introspección. Algunos ejemplos incluyen:

* La función type():    
  Permite obtener el tipo de un objeto.
* La función dir():     
  Retorna una lista de los atributos y métodos disponibles para un objeto.
* El atributo \__dict__:     
  Proporciona un diccionario que contiene los atributos y sus valores para un objeto.
* La función getattr():     
  Permite obtener el valor de un atributo de un objeto por su nombre.
* La función hasattr():     
  Permite verificar si un objeto tiene un atributo con un nombre específico.

La introspección es especialmente útil durante el desarrollo y la depuración de programas, ya que permite explorar la estructura y el comportamiento de objetos en tiempo de ejecución sin necesidad de conocer su definición estática en tiempo de diseño.

Por ejemplo, puedes usar la introspección para descubrir qué métodos y atributos tiene un objeto determinado, lo que puede ser útil al interactuar con bibliotecas externas o al trabajar con objetos dinámicos cuya estructura puede cambiar durante la ejecución del programa.

## funciones

Como ya hemos visto la introspección en Python se refiere a la capacidad de examinar y determinar las propiedades de un objeto en tiempo de ejecución. Python proporciona varias funciones y métodos que permiten realizar introspección de manera efectiva. 



Aquí tienes algunos ejemplos:

1. type(): La función type() devuelve el tipo de un objeto.

```python
x = 5
print(type(x))  # <class 'int'>

```

2. dir(): La función dir() devuelve una lista de atributos y métodos de un objeto.

```python
x = "Hola"
print(dir(x))  # ['__add__', '__class__', '__contains__', '__delattr__', ... ]

```
3. hasattr(): La función hasattr() verifica si un objeto tiene un atributo dado.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Juan")
print(hasattr(p, 'nombre'))  # True
print(hasattr(p, 'edad'))    # False

```

4. getattr(): La función getattr() devuelve el valor de un atributo de un objeto.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Juan")
print(getattr(p, 'nombre'))  # Juan

```

5. setattr(): La función setattr() establece el valor de un atributo de un objeto.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Juan")
setattr(p, 'edad', 30)
print(p.edad)  # 30

```

6. isinstance(): La función isinstance() verifica si un objeto es una instancia de una clase dada.

```python
class Persona:
    pass

p = Persona()
print(isinstance(p, Persona))  # True
print(isinstance(p, str))       # False

```

Estas son solo algunas de las formas en que Python permite la introspección de objetos y clases en tiempo de ejecución. La introspección es una característica poderosa que facilita la exploración y manipulación dinámica de objetos en Python.
