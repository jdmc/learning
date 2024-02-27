# **Métodos: (Methods)** 

En Python existen diferentes tipos de métodos (funciones definidas dentro de una clase) que se utilizan para diferentes propósitos y pueden clasificarse de varias formas según su comportamiento y su relación con la clase y los objetos. Aquí te presento algunos tipos comunes de métodos en Python:

**Métodos de instancia**:    
Estos son los métodos más comunes en Python y son aquellos que se definen dentro de una clase y pueden acceder a los atributos de instancia de la clase utilizando self. Estos métodos actúan sobre instancias específicas de la clase y pueden modificar su estado. Se definen sin ningún decorador especial.

```python
class MiClase:
    def metodo_instancia(self):
        print("Este es un método de instancia.")

```

**Métodos estáticos**:    
Estos métodos no reciben una referencia a la instancia (self) ni a la clase (cls) como primer parámetro. Son independientes de cualquier instancia o clase específica y se definen utilizando el decorador @staticmethod. Se utilizan cuando la lógica de un método no depende del estado de la instancia o de la clase.

```python
class MiClase:
    @staticmethod
    def metodo_estatico():
        print("Este es un método estático.")

```
**Métodos de clase**:    
Estos métodos reciben una referencia a la clase (cls) como primer parámetro en lugar de una instancia. Se definen utilizando el decorador @classmethod. Se utilizan cuando la lógica de un método necesita acceder a la clase misma, pero no a instancias específicas de la clase.

```python
class MiClase:
    @classmethod
    def metodo_clase(cls):
        print("Este es un método de clase.")

```

**Métodos mágicos (dunder methods)**:    
Son métodos especiales que tienen nombres que comienzan y terminan con doble guion bajo (\__). Estos métodos son llamados automáticamente por el intérprete de Python en circunstancias específicas. Algunos ejemplos comunes incluyen \__init__() para inicialización, \__str__() para representación de cadena y \__len__() para longitud, entre otros.

```python
class MiClase:
    def __init__(self):
        pass

    def __str__(self):
        return "Este es un objeto de MiClase."

```

# Decorador General

En Python, los decoradores son funciones que se utilizan para modificar o extender el comportamiento de otras funciones o métodos. Los decoradores son una característica poderosa y flexible del lenguaje que se utilizan en muchas áreas, como la programación funcional, la programación orientada a objetos y el desarrollo web. 



**Decoradores Generales**:    
Estos son los decoradores que se pueden aplicar a funciones, métodos o cualquier otro tipo de callable (objetos que pueden ser llamados). Pueden modificar o extender el comportamiento de la función o método al que se aplican. Un ejemplo común de decorador general es **@decorator**, que toma una función y devuelve otra función.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función.")
        result = func(*args, **kwargs)
        print("Después de llamar a la función.")
        return result
    return wrapper

@decorator
def my_function():
    print("Esta es mi función.")

my_function()

```

## Algunos Decoradores generales

Aquí tienes algunos tipos comunes de decoradores en Python:

**Decoradores de funciones**:    
Estos son los decoradores más comunes y se utilizan para modificar el comportamiento de las funciones. Un decorador de función toma una función como argumento y devuelve otra función. Se utilizan colocando @nombre_del_decorador encima de la definición de la función.

```python
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función.")
        resultado = funcion(*args, **kwargs)
        print("Después de llamar a la función.")
        return resultado
    return wrapper

@decorador
def mi_funcion():
    print("Esta es mi función.")

mi_funcion()

```

**Decoradores de métodos**:    
Son similares a los decoradores de funciones, pero se utilizan específicamente para decorar métodos dentro de una clase. Funcionan de la misma manera que los decoradores de funciones, pero tienen en cuenta que el primer parámetro de la función es **self**.

```python
def decorador_metodo(funcion):
    def wrapper(self, *args, **kwargs):
        print("Antes de llamar al método.")
        resultado = funcion(self, *args, **kwargs)
        print("Después de llamar al método.")
        return resultado
    return wrapper

class MiClase:
    @decorador_metodo
    def mi_metodo(self):
        print("Este es mi método.")

objeto = MiClase()
objeto.mi_metodo()

```

# Decorador Especial

**Decoradores Especiales**:    
Estos son decoradores específicos proporcionados por Python que tienen un propósito y comportamiento predefinidos. Son utilizados en contextos específicos, como en la definición de propiedades **(@property)**, métodos de clase **(@classmethod)**, métodos estáticos **(@staticmethod)**, y en la creación de decoradores de clase **(@decorator_class)**.

```python
class MyClass:
    @staticmethod
    def static_method():
        print("Este es un método estático.")

    @classmethod
    def class_method(cls):
        print("Este es un método de clase.")

    @property
    def property_method(self):
        return "Este es un método de propiedad."

# Ejemplo de uso
obj = MyClass()
obj.static_method()
obj.class_method()
print(obj.property_method)

```

En este ejemplo, **@staticmethod**, **@classmethod**, y **@property** son ejemplos de decoradores especiales proporcionados por Python. Cada uno tiene un propósito específico y un comportamiento predefinido que es inherente a su función en el lenguaje.