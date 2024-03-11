[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Abstracción 

La abstracción (abstraction) en Python (y en programación en general) se refiere al proceso de ocultar los detalles internos y complejidades de un objeto o sistema, y solo mostrar las características esenciales y relevantes para el usuario. En otras palabras, la abstracción permite al usuario interactuar con un objeto o sistema sin necesidad de entender cómo funciona internamente.

En el contexto de la programación orientada a objetos (POO), la abstracción se logra mediante la definición de clases y la creación de objetos. Las clases actúan como plantillas que definen las propiedades y comportamientos de los objetos, mientras que los objetos son instancias concretas de esas clases.

Un ejemplo de abstracción en Python sería el uso de una clase para representar un automóvil. El usuario puede interactuar con el automóvil (por ejemplo, encenderlo, acelerar, frenar) sin necesidad de conocer los detalles internos del funcionamiento del motor, la transmisión, el sistema de frenos, etc. La clase de automóvil abstracta proporciona una interfaz clara y simplificada para interactuar con el automóvil sin tener que preocuparse por las complejidades internas.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"The car is accelerating. Current speed: {self.speed} km/h")

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
            print(f"The car is braking. Current speed: {self.speed} km/h")
        else:
            print("The car is already stopped.")

# Crear un objeto Car
my_car = Car("Toyota", "Corolla", 2020)

# Interactuar con el objeto sin necesidad de conocer los detalles internos
my_car.accelerate()  # Acelerar el automóvil
my_car.accelerate()  # Acelerar de nuevo
my_car.brake()       # Frenar el automóvil

```

En este ejemplo, la clase Car representa un automóvil y define métodos para acelerar y frenar el automóvil. El usuario puede interactuar con el automóvil llamando a estos métodos sin necesidad de conocer cómo se implementan internamente.

El usuario solo necesita saber cómo usar los métodos proporcionados por la clase Car para realizar acciones como acelerar y frenar el automóvil. Los detalles internos, como cómo se realiza la aceleración o el frenado, están ocultos dentro de la implementación de la clase Car, lo que proporciona una abstracción efectiva.

>En resumen, la abstracción en Python permite simplificar la programación al ocultar detalles innecesarios y proporcionar una interfaz clara y fácil de usar para el usuario.

## abstractmethod

Abstractmethod es una característica específica de la programación orientada a objetos que contribuye a la abstracción en Python. Pertenece al módulo abc (Abstract Base Classes), que proporciona una forma de definir clases abstractas y métodos abstractos.

Un método abstracto es un método que se declara en una clase base pero no se implementa. En su lugar, las clases derivadas deben proporcionar una implementación concreta para el método abstracto. Esto promueve la abstracción al permitir que las clases base definan una interfaz común que las clases derivadas deben seguir.

Al utilizar abstractmethod, puedes definir una clase base que especifica ciertos métodos como abstractos, lo que obliga a las clases derivadas a implementarlos. Esto ayuda a garantizar que las clases derivadas cumplan con ciertas características o comportamientos esperados, lo que facilita la creación de jerarquías de clases más sólidas y coherentes.

>En resumen, abstractmethod es una herramienta poderosa que fomenta la abstracción al definir una interfaz común para las clases y promover la reutilización del código a través de la herencia.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Clase abstracta que representa una forma geométrica"""

    @abstractmethod
    def area(self):
        """Método abstracto para calcular el área de la forma"""
        pass

    @abstractmethod
    def perimeter(self):
        """Método abstracto para calcular el perímetro de la forma"""
        pass

class Rectangle(Shape):
    """Clase concreta que representa un rectángulo"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Clase concreta que representa un círculo"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creamos instancias de las clases
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Imprimimos el área y perímetro de las formas
print("Rectángulo:")
print("Área:", rectangle.area())
print("Perímetro:", rectangle.perimeter())

print("\nCírculo:")
print("Área:", circle.area())
print("Perímetro:", circle.perimeter())


``` 
En este ejemplo, Shape es una clase abstracta que define dos métodos abstractos: area() y perimeter(). Estos métodos deben ser implementados por cualquier clase que herede de Shape. Rectangle y Circle son clases concretas que heredan de Shape y proporcionan implementaciones concretas para los métodos abstractos. Esto asegura que todas las formas que se creen heredando de Shape tendrán métodos area() y perimeter() definidos.

### Cuando implementar

La abstracción se usa en programación cuando queremos ocultar los detalles internos de cómo funciona una parte del sistema y solo exponer una interfaz simplificada que permita interactuar con ella. Esto se hace para simplificar el desarrollo y el mantenimiento del código, así como para facilitar su reutilización.

Aquí hay algunas situaciones comunes en las que se usa la abstracción:

1. Modelado de objetos reales: En la programación orientada a objetos, la abstracción se utiliza para modelar objetos del mundo real. Por ejemplo, un objeto Car puede tener métodos como start(), accelerate(), brake(), etc., ocultando los detalles internos de cómo funciona el motor, la transmisión, etc.

2. Interacción con bibliotecas o frameworks: Cuando trabajamos con bibliotecas o frameworks, a menudo interactuamos con interfaces abstraídas que nos permiten utilizar la funcionalidad proporcionada sin necesidad de conocer los detalles de implementación internos.

3. División del código en módulos: La abstracción nos permite dividir nuestro código en módulos o componentes separados, donde cada componente proporciona una interfaz clara para interactuar con él, ocultando los detalles internos de su implementación.

4. Creación de interfaces de usuario: En el desarrollo de aplicaciones, se utilizan abstracciones para crear interfaces de usuario intuitivas que ocultan la complejidad subyacente de las operaciones realizadas.

En resumen, la abstracción se utiliza para simplificar la complejidad y mejorar la modularidad, la reutilización y la mantenibilidad del código al ocultar los detalles internos y exponer solo lo que es relevante para el usuario o desarrollador.