# herencia

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

class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

perro1 = Perro("Firulais")
print(perro1.sonido())  # Output: Guau!

gato1 = Gato("Michi")
print(gato1.sonido())   # Output: Miau!

```

En este ejemplo, la clase Perro y la clase Gato heredan de la clase Animal. Ambas clases hijas tienen un método sonido() que sobrescribe el método sonido() de la clase padre Animal, permitiéndoles definir su propio comportamiento.

# coleccion especiales

# pickle