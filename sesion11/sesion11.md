# Getters & Setters

En Python, los "getters" y "setters" son métodos utilizados para acceder y modificar los atributos de una clase de manera controlada. Son comunes en la programación orientada a objetos y se utilizan para garantizar el encapsulamiento de datos, es decir, para controlar cómo los datos de un objeto son accedidos y modificados desde fuera de la clase.

Un **"getter"** es un método que se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo. Por convención, los nombres de los getters suelen empezar con **"get_"** seguido del nombre del atributo.

Un **"setter"** es un método que se utiliza para establecer el valor de un atributo privado de una clase. Proporciona acceso de escritura a ese atributo. Por convención, los nombres de los setters suelen empezar con **"set_"** seguido del nombre del atributo.

Aquí tienes un ejemplo básico que muestra cómo se podrían implementar getters y setters en Python:

```python 
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa.")

# Uso de los getters y setters
persona1 = Persona("Juan", 30)
print(persona1.get_nombre())  # Imprime "Juan"
print(persona1.get_edad())    # Imprime 30

persona1.set_nombre("Carlos")
persona1.set_edad(35)

print(persona1.get_nombre())  # Imprime "Carlos"
print(persona1.get_edad())    # Imprime 35

```

En este ejemplo, los métodos **get_nombre()** y **get_edad()** son los getters que permiten obtener los valores de los atributos **_nombre** y **_edad** respectivamente, mientras que los métodos **set_nombre()** y **set_edad()** son los setters que permiten establecer los valores de esos atributos. El uso de getters y setters en Python puede proporcionar un mayor control sobre la forma en que se acceden y modifican los datos de una clase.

# @property

Al incluir el decorador **@property** en Python, puedes convertir métodos de una clase en atributos, lo que permite acceder a ellos como si fueran atributos directos sin necesidad de llamar explícitamente al método. Esto puede hacer que tu código sea más limpio y más fácil de entender.

Veamos cómo se puede usar @property para implementar getters y setters en Python:

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

# Uso de @property
persona1 = Persona("Juan", 30)
print(persona1.nombre)  # Imprime "Juan"
print(persona1.edad)    # Imprime 30

persona1.nombre = "Carlos"
persona1.edad = 35

print(persona1.nombre)  # Imprime "Carlos"
print(persona1.edad)    # Imprime 35

```