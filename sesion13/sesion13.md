# Herencia

La herencia en Python es un concepto de la programación orientada a objetos que permite a una clase (llamada clase hija o subclase) heredar atributos y métodos de otra clase (llamada clase padre o superclase). Esto significa que la clase hija puede utilizar y extender funcionalidades de la clase padre, lo que promueve la reutilización del código y facilita la organización y estructuración del programa.

Cuando una clase hereda de otra, la clase hija adquiere todos los métodos y atributos de la clase padre y puede agregar nuevos métodos o modificar los existentes según sea necesario. Esto permite crear jerarquías de clases donde las clases más específicas heredan comportamientos y características de clases más generales.

La herencia en Python se logra especificando el nombre de la clase padre entre paréntesis en la definición de la clase hija.    
Por ejemplo:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        pass

class Perro(Animal):  # Especificando que Perro hereda de Animal
    def sonido(self):
        return "Guau!"

class Gato(Animal):   # Especificando que Gato hereda de Animal
    def sonido(self):
        return "Miau!"

perro1 = Perro("Firulais")
print(perro1.sonido())  # Output: Guau!

gato1 = Gato("Michi")
print(gato1.sonido())   # Output: Miau!


```

Este es el método de Python para establecer la herencia entre clases. La clase hija (Perro y Gato) hereda todos los métodos y atributos de la clase padre (Animal), permitiendo así que se utilicen y sobrescriban según sea necesario.

Ambas clases hijas tienen un método sonido() que sobrescribe el método sonido() de la clase padre Animal, permitiéndoles definir su propio comportamiento.

# Tipos de herencia

Dentro del concepto de herencia en programación orientada a objetos, hay varios tipos de relaciones y técnicas que se utilizan para modelar la estructura y el comportamiento de las clases. Algunos de los tipos comunes de herencia incluyen:

1. Herencia Simple:    
  Este es el tipo más básico de herencia, donde una clase hija hereda de una sola clase padre.

2. Herencia Múltiple:     
  En algunos lenguajes de programación, como Python, es posible que una clase hija herede de múltiples clases padres. Esto permite a la clase hija heredar atributos y métodos de todas las clases padres.

3. Herencia de Jerarquía:     
  Este tipo de herencia se refiere a la relación de herencia en la que una clase padre tiene múltiples clases hijas que heredan de ella. Cada clase hija puede tener sus propias subclases.

4. Herencia Simple vs. Herencia Múltiple:     
  Mientras que la herencia simple implica que una clase hija hereda de una sola clase padre, la herencia múltiple implica que una clase hija puede heredar de múltiples clases padres.

5. Herencia de Interfaz:     
  Aunque Python no tiene una implementación explícita de interfaces como en otros lenguajes, la herencia de interfaz se refiere al concepto de definir un conjunto de métodos que las clases hijas deben implementar. Esto promueve la consistencia y la coherencia en la interfaz de las clases.

6. Herencia Abstracta:     
  Se refiere a la creación de clases que no pueden ser instanciadas directamente y que están diseñadas específicamente para ser subclases. Estas clases a menudo contienen métodos abstractos, que deben ser implementados por las subclases.

Cada tipo de herencia tiene sus propias ventajas y desventajas, y es importante comprender cuándo y cómo aplicar cada uno según los requisitos del diseño del software.


## herencia simple

## herencia compleja

# coleccion especiales

# pickle