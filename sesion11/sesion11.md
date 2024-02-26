
# Class

En Python, class es una palabra clave que se utiliza para definir una nueva clase. Una clase es una plantilla para crear objetos que agrupan datos (atributos) y operaciones (métodos) que pueden realizar esos objetos.

Cuando defines una clase en Python, estás creando un nuevo tipo de objeto. Los objetos son instancias de una clase particular. Por ejemplo, podrías tener una clase llamada Persona que define atributos como nombre y edad, y métodos como saludar o caminar.

Aquí hay un ejemplo básico de cómo se define una clase en Python:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar de la instancia persona1
persona1.saludar()  # Imprime: Hola, soy Juan y tengo 30 años.

```
En este ejemplo, **class Persona:** define una nueva clase llamada **Persona**. Dentro de la clase, **\__init__** es un método especial llamado constructor que se llama automáticamente cuando se crea una nueva instancia de la clase. Los métodos de la clase toman **self** como su primer parámetro, que hace referencia a la instancia actual de la clase.

La palabra clave **self** se utiliza para acceder a los atributos y métodos de la instancia dentro de la clase. Por ejemplo, **self.nombre** se refiere al atributo nombre de la instancia actual de la clase **Persona**.

En resumen, **class** en Python se utiliza para definir una nueva clase, que actúa como una plantilla para crear objetos con atributos y métodos asociados.

# "__"  (Proteger datos)

En Python, puedes "proteger" los datos de una clase utilizando la convención de nombres con doble guion bajo "(\__)". Esto se conoce como "name mangling" o "enmascaramiento de nombres". Cuando un atributo o un método de una clase comienza con doble guion bajo (\__), Python lo renombra internamente agregando el nombre de la clase al principio, lo que hace que sea más difícil acceder a él desde fuera de la clase.

Veamos un ejemplo:

```python
class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def __metodo_privado(self):
        return 'Este es un método privado'

# Uso de la clase
objeto = MiClase()

# Intentamos acceder al atributo privado
print(objeto.__atributo_privado)  # Esto generará un AttributeError

# Intentamos llamar al método privado
print(objeto.__metodo_privado())  # Esto generará un AttributeError

```

En este ejemplo, tanto el atributo __atributo_privado como el método __metodo_privado están protegidos por la convención de doble guion bajo. Intentar acceder a ellos desde fuera de la clase resultará en un error AttributeError.

Sin embargo, aunque el acceso directo a estos miembros desde fuera de la clase está protegido, aún es posible acceder a ellos desde dentro de la clase:

```python
class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def __metodo_privado(self):
        return 'Este es un método privado'

    def acceder_miembro_privado(self):
        print(self.__atributo_privado)
        print(self.__metodo_privado())

# Uso de la clase
objeto = MiClase()
objeto.acceder_miembro_privado()  # Esto imprimirá el valor del atributo y el resultado del método

```

Dentro de la clase, puedes acceder a los miembros "privados" normalmente, sin embargo, desde fuera de la clase, acceder a ellos directamente generará un error. Esto proporciona un nivel de encapsulamiento y protección de los datos, aunque no garantiza la seguridad total. Es importante recordar que en Python, la privacidad se basa en la convención y no en la imposición.

# Getters & Setters

En Python, los **"getters"** y **"setters"** son métodos utilizados para acceder y modificar los atributos de una clase de manera controlada. Son comunes en la programación orientada a objetos y se utilizan para garantizar el encapsulamiento de datos, es decir, para controlar cómo los datos de un objeto son accedidos y modificados desde fuera de la clase.

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

En este ejemplo, los métodos **nombre()** y **edad()** están decorados con **@property**, lo que permite acceder a ellos como atributos directos de la instancia persona1. Además, los métodos **nombre()** y **edad()** se definen como getters, y los métodos **nombre.setter** y **edad.setter** se definen como setters. Esto significa que puedes asignar nuevos valores a nombre y edad como si fueran atributos directos, y se ejecutarán los métodos correspondientes para validar los nuevos valores según lo definido en los setters.

El uso de **@property** en Python permite una sintaxis más clara y concisa para implementar getters y setters, lo que puede hacer que tu código sea más legible y mantenible.