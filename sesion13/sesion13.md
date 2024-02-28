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
    
    1.1 Herencia Simple multinivel:    
    Dentro del concepto de herencia simple, podemos encontrar la herencia multinivel. La herencia multinivel se refiere a una situación en la que una clase hija hereda de otra clase hija, creando así una cadena o jerarquía de herencia.

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


## Herencia simple

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):  # Perro hereda de Animal
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):   # Gato hereda de Animal
    def hacer_sonido(self):
        return "Miau!"

# Crear instancias de las clases hijas
firulais = Perro("Firulais")
michi = Gato("Michi")

# Llamar al método de la clase padre desde las instancias de las clases hijas
print(firulais.nombre + " hace " + firulais.hacer_sonido())  # Output: Firulais hace Guau!
print(michi.nombre + " hace " + michi.hacer_sonido())        # Output: Michi hace Miau!

```

En este ejemplo:

La clase Animal es la clase padre que tiene un método hacer_sonido() que no está implementado. Esta clase es una representación genérica de un animal.
Las clases Perro y Gato son clases hijas que heredan de la clase Animal. Cada una implementa su propio método hacer_sonido(), especificando el sonido característico del perro y el gato respectivamente.
Se crean instancias de las clases hijas Perro y Gato, y se llama al método hacer_sonido() de cada una de ellas. Como se esperaba, cada instancia devuelve el sonido característico de su respectiva clase.
Este es un ejemplo básico de herencia simple donde una clase hija (Perro y Gato) hereda de una clase padre (Animal).

### Herencia Simple Multinivel

En este tipo de herencia, una clase puede heredar de otra clase que a su vez hereda de otra clase, y así sucesivamente, creando múltiples niveles en la jerarquía de herencia. Esto significa que una clase puede heredar características tanto de su clase padre inmediata como de todas las clases en la cadena de herencia ascendente.

Aquí tienes un ejemplo simple de herencia multinivel en Python:

```python
class Animal:
    def comer(self):
        print("El animal está comiendo.")

class Mamifero(Animal):
    def dormir(self):
        print("El mamífero está durmiendo.")

class Perro(Mamifero):
    def ladrar(self):
        print("El perro está ladrando.")

class Bulldog(Perro):
    def roncar(self):
        print("El bulldog está roncando.")

bulldog1 = Bulldog()
bulldog1.comer()  # Output: El animal está comiendo.
bulldog1.dormir()  # Output: El mamífero está durmiendo.
bulldog1.ladrar()  # Output: El perro está ladrando.
bulldog1.roncar()  # Output: El bulldog está roncando.

```
En este ejemplo, la clase Mamifero hereda de la clase Animal, la clase Perro hereda de la clase Mamifero, y la clase Bulldog hereda de la clase Perro. Esto forma una cadena de herencia multinivel, donde Bulldog hereda tanto de Perro como de Mamifero y Animal, lo que significa que puede acceder a los métodos de todas estas clases en la jerarquía de herencia.
## herencia compleja

# coleccion especiales

# pickle