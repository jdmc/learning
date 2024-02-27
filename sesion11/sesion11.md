
# Modelar
Modelar con Programación Orientada a Objetos (POO) en Python se refiere al proceso de diseñar y crear clases y objetos que representen entidades y comportamientos del mundo real de manera modular y reutilizable.     
La POO es un paradigma de programación que se basa en el concepto de **"objetos", que son instancias de "clases", y permite organizar el código de una manera más estructurada y eficiente.

En Python, la POO se implementa utilizando clases y objetos. Aquí hay una descripción general de los conceptos básicos:

1. **Clase**: Una clase es una plantilla o un plano para crear objetos. Define las propiedades y comportamientos comunes que tendrán los objetos creados a partir de ella. Por ejemplo, podrías tener una clase llamada Persona que define propiedades como nombre, edad, y comportamientos como saludar.

2. **Objeto**: Un objeto es una instancia particular de una clase. Es una entidad con un estado (atributos) y un comportamiento (métodos). Por ejemplo, si tienes una clase Persona, un objeto de esta clase podría ser juan, con un nombre "Juan" y una edad de 30 años.

3. **Atributos**: Los atributos son variables que pertenecen a un objeto. Representan el estado de un objeto y pueden ser variables de datos o referencias a otros objetos.

4. **Métodos**: Los métodos son funciones definidas dentro de una clase que representan el comportamiento de los objetos de esa clase. Los métodos pueden realizar acciones y manipular los atributos de un objeto.

5. **Encapsulamiento**: Es el concepto de ocultar los detalles de implementación de una clase y exponer solo una interfaz pública para interactuar con los objetos. En Python, esto se logra a menudo utilizando atributos y métodos privados (que comienzan con __) y propiedades.

6. **Herencia**: Es un mecanismo que permite que una clase herede atributos y métodos de otra clase. Esto promueve la reutilización del código y la organización jerárquica de las clases.

7. **Polimorfismo**: Es la capacidad de los objetos de diferentes clases de responder al mismo mensaje (método) de manera diferente. Esto permite escribir código que funciona con una variedad de tipos de objetos.

En resumen, modelar con POO en Python implica definir clases que representen entidades del mundo real, crear objetos a partir de esas clases y definir sus propiedades y comportamientos mediante atributos y métodos. Esto permite escribir código más modular, reutilizable y fácil de mantener.

# SOLID

Los principios SOLID son un conjunto de cinco principios de diseño de software que fueron propuestos por Robert C. Martin, también conocido como "Uncle Bob". Estos principios están destinados a guiar a los desarrolladores hacia la creación de código limpio, mantenible y flexible. Cada uno de estos principios se centra en un aspecto específico del diseño de software orientado a objetos y modular.

A continuación, te presento cada uno de los principios SOLID:

1. S - Principio de responsabilidad única (Single Responsibility Principle):
  Este principio establece que una clase debe tener una única razón para cambiar. Es decir, una clase debe tener una sola responsabilidad y debe encapsular todo lo relacionado con esa responsabilidad. Esto promueve la cohesión y la modularidad en el diseño del software, facilitando su mantenimiento y reutilización.

2. O - Principio de abierto/cerrado (Open/Closed Principle):
  Este principio establece que una clase debe estar abierta para su extensión pero cerrada para su modificación. Es decir, el comportamiento de una clase debe poder extenderse mediante la adición de nuevas funcionalidades, pero sin necesidad de modificar su código fuente original. Esto se logra mediante el uso de la herencia, la composición, la inversión de dependencias y los patrones de diseño.

3. L - Principio de sustitución de Liskov (Liskov Substitution Principle):
  Este principio establece que los objetos de una clase base deben poder ser reemplazados por objetos de sus subclases sin afectar la integridad del programa. En otras palabras, una instancia de una subclase debe poder ser utilizada en cualquier lugar donde se espera una instancia de la clase base sin cambiar el comportamiento del programa. Esto garantiza que la herencia se utilice de manera adecuada y que las clases derivadas no introduzcan comportamientos inesperados.

4. I - Principio de segregación de interfaces (Interface Segregation Principle):
  Este principio establece que una clase no debe depender de métodos que no utiliza. En lugar de tener interfaces grandes que contienen múltiples métodos, se deben dividir en interfaces más pequeñas y específicas. Esto evita que las clases dependan de funcionalidades innecesarias y reduce el acoplamiento entre componentes del sistema.

5. D - Principio de inversión de dependencias (Dependency Inversion Principle):
  Este principio establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino que ambos deben depender de abstracciones. Además, las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones. Esto promueve la flexibilidad y la extensibilidad del código al permitir la sustitución de componentes concretos por otros que implementen la misma abstracción.

Estos principios **SOLID** son fundamentales para el diseño de software de calidad y ayudan a los desarrolladores a crear sistemas que sean fáciles de entender, mantener y extender a lo largo del tiempo.

[SOLID Wikipedi](https://es.wikipedia.org/wiki/SOLID )


# Class
En Python, class es una palabra clave que se utiliza para definir una nueva clase. Una clase es una plantilla para crear objetos que agrupan **datos** (atributos) y **operaciones** (métodos) que pueden realizar esos objetos.

Cuando defines una clase en Python, estás creando un nuevo tipo de objeto. Los objetos son instancias de una clase particular. Por ejemplo, podrías tener una clase llamada Persona que define atributos/datos como nombre y edad, y métodos/operaciones como saludar o caminar.

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

# Método mágico
El término "método mágico" en Python se refiere a métodos especiales que tienen nombres que comienzan y terminan con doble guion bajo (__).    
También se les conoce como **"métodos dunder"** (del inglés "double underscore").

Estos métodos mágicos son invocados automáticamente por el intérprete de Python en circunstancias específicas.     
Por ejemplo, cuando se crea una nueva instancia de una clase, Python busca e invoca el método \__init__() si está definido en la clase. De manera similar, cuando se utiliza la función len() en un objeto, Python busca e invoca el método \__len__() si está definido.

Aquí tienes algunos ejemplos de métodos mágicos comunes y sus usos:

\__init__():     
Método de inicialización, llamado automáticamente cuando se crea una nueva instancia de la clase.    
\__str__():    
Método que devuelve una representación de cadena legible para humanos del objeto, se llama cuando se utiliza la función str() o print().    
\__repr__():    
Método que devuelve una representación de cadena que es útil para recrear el objeto, se llama cuando se utiliza la función repr().    
\__len__():     
Método que devuelve la longitud del objeto, se llama cuando se utiliza la función len().    
\__add__(), \__sub__(), \__mul__(), etc.:     
Métodos que definen el comportamiento de operadores como suma, resta, multiplicación, etc.    
\__getitem__(), \__setitem__(), \__delitem__():     
Métodos que permiten acceder a los elementos de un objeto como si fuera un contenedor, como una lista o un diccionario.    

Estos métodos mágicos permiten que las clases definidas por el usuario se comporten de manera similar a los tipos de datos incorporados en Python y proporcionan una forma de personalizar el comportamiento de los objetos en contextos específicos.


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

# self

self es una convención utilizada para referirse al objeto mismo dentro de los métodos de una clase. 
Cuando defines métodos en una clase, el primer parámetro de cada método debe ser self. 
Este parámetro representa la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de esa instancia.

mas info > [Session 10: POO / self ](https://github.com/jdmc/learning/blob/9c8d3ea34434f0c84fda04dba222a384bf9d2d90/sesion10/POO_sesion10.md#self) 

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

# Uso "property" / "setter" / "getter"

El uso de **property**, **setter** y **getter** en Python es útil cuando deseas tener más control sobre cómo se acceden y modifican los atributos de una clase.    

Aquí hay algunas situaciones comunes en las que puede ser beneficioso utilizar estos:

1. Validación de datos: Cuando necesitas realizar validaciones o comprobaciones antes de permitir que un atributo se establezca con un valor determinado. Por ejemplo, si tienes un atributo que no debe ser negativo, puedes usar un setter para garantizar que el valor asignado sea válido.

2. Encapsulación: Cuando deseas encapsular los detalles de implementación de tu clase y proporcionar una interfaz más limpia y fácil de usar para los usuarios de tu clase. Los métodos getter y setter pueden ocultar la estructura interna de tu clase y proporcionar un punto de acceso controlado a los atributos.

3. Compatibilidad con versiones anteriores: Si necesitas mantener la compatibilidad con versiones anteriores de tu código, puedes usar @property para agregar propiedades a tu clase sin cambiar la interfaz existente.

4. Refactorización del código: Siempre que necesites cambiar la implementación interna de una clase pero desees mantener la interfaz externa, puedes refactorizar el código utilizando propiedades y métodos setter y getter para evitar cambios disruptivos en el código cliente.

5. Logging y seguimiento: Puedes utilizar métodos setter y getter para agregar lógica de logging o seguimiento cada vez que se accede o modifica un atributo, lo que puede ser útil para depurar o rastrear el comportamiento de tu aplicación.

En resumen, deberías considerar el uso de **property**, **setter** y **getter** en Python cuando necesitas un mayor control sobre cómo se acceden y modifican los atributos de una clase, así como para mejorar la encapsulación y mantener la compatibilidad con versiones anteriores del código. Sin embargo, ten en cuenta que su uso excesivo puede complicar innecesariamente tu código, así que úsalos con moderación y solo cuando realmente los necesites.