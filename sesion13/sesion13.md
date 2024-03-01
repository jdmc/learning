[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
# Herencia (2º principio POO)

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

La herencia simple es un concepto fundamental en la programación orientada a objetos que permite a una clase (llamada clase hija o subclase) heredar atributos y métodos de otra clase (llamada clase padre o superclase).

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

### Caracteristicas Herencia Simple

Algunas características y consideraciones sobre la herencia simple incluyen:

1. Reutilización de código:     
  La herencia simple facilita la reutilización de código al permitir que las clases hijas hereden comportamientos y características de sus clases padre.

2. Jerarquía de clases:    
  La herencia simple se utiliza para crear jerarquías de clases, donde las clases más específicas heredan de clases más generales. Esto promueve una estructura organizada y coherente en el diseño de un programa.

3. Extensibilidad:     
  Las clases hijas pueden extender la funcionalidad de las clases padre al agregar nuevos métodos o sobrescribir métodos existentes. Esto permite adaptar las clases a diferentes necesidades y escenarios específicos.

4. Polimorfismo:     
  La herencia simple facilita el polimorfismo, que es la capacidad de las clases hijas de proporcionar implementaciones diferentes para los mismos métodos heredados de las clases padre. Esto permite tratar objetos de diferentes clases de manera uniforme a través de interfaces comunes.

5. Encapsulación:     
  La herencia simple puede utilizarse junto con otros principios de la programación orientada a objetos, como la encapsulación, para mejorar la modularidad y la seguridad del código.

6. Relación "es-un":     
  La herencia simple se utiliza para modelar la relación "es-un", donde una clase hija se considera un tipo especializado de su clase padre. Por ejemplo, un perro (clase hija) es un tipo de animal (clase padre).

>En resumen, la herencia simple es un concepto fundamental en la programación orientada a objetos que promueve la reutilización de código, la organización estructurada del programa y la creación de relaciones "es-un" entre las clases. Es una herramienta poderosa para el diseño de software modular y extensible.


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


## Herencia Multiple

La herencia múltiple es un concepto de la programación orientada a objetos que permite que una clase hija herede atributos y métodos de más de una clase padre. Aunque puede ser poderosa, también puede resultar complicada y generar situaciones ambiguas si no se maneja correctamente.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Mascota:
    def __init__(self, dueno):
        self.dueno = dueno
    
    def mostrar_dueno(self):
        return f"Mi dueño es {self.dueno}"

class Perro(Animal, Mascota):  # Perro hereda de Animal y Mascota
    def __init__(self, nombre, dueno):
        Animal.__init__(self, nombre)
        Mascota.__init__(self, dueno)

    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal, Mascota):   # Gato hereda de Animal y Mascota
    def __init__(self, nombre, dueno):
        Animal.__init__(self, nombre)
        Mascota.__init__(self, dueno)

    def hacer_sonido(self):
        return "Miau!"

# Crear instancias de las clases hijas con herencia múltiple
firulais = Perro("Firulais", "Juan")
michi = Gato("Michi", "Maria")

# Llamar a métodos de las clases padre desde las instancias de las clases hijas
print(firulais.nombre + " hace " + firulais.hacer_sonido())  # Output: Firulais hace Guau!
print(michi.nombre + " hace " + michi.hacer_sonido())        # Output: Michi hace Miau!

# Llamar a métodos de las clases de mezcla (Mixin)
print(firulais.mostrar_dueno())  # Output: Mi dueño es Juan
print(michi.mostrar_dueno())     # Output: Mi dueño es Maria

```
En este ejemplo:

Las clases Animal y Mascota son clases padres que definen funcionalidades relacionadas con los animales y las mascotas, respectivamente.
Las clases Perro y Gato son clases hijas que heredan de las clases Animal y Mascota. Ambas clases hijas tienen su propio método hacer_sonido().
Se crean instancias de las clases hijas Perro y Gato, especificando tanto el nombre como el dueño.
Cada instancia de las clases hijas puede acceder tanto a los métodos de la clase Animal como de la clase Mascota, lo que demuestra la herencia múltiple.

### Caracteristicas Herencia Multiple

Aquí hay algunas características y consideraciones sobre la herencia múltiple:

1. Reutilización de código:     
  Al igual que con la herencia simple, la herencia múltiple permite la reutilización de código al heredar atributos y métodos de múltiples clases padres.

2. Jerarquía de clases:     
  La herencia múltiple puede utilizarse para construir jerarquías de clases más complejas, donde una clase puede heredar de múltiples clases padres para adquirir diferentes comportamientos y características.

3. Conflictos de nombres:     
  Cuando una clase hija hereda métodos o atributos con el mismo nombre de más de una clase padre, puede surgir un conflicto de nombres. En estos casos, es necesario que el programador resuelva explícitamente estos conflictos para evitar ambigüedades.

4. MRO (Method Resolution Order):     
  Python utiliza el algoritmo MRO para determinar el orden en el que se buscan los métodos en las clases padre cuando se llama a un método desde una instancia de la clase hija. Esto es importante para resolver conflictos de nombres en la herencia múltiple.

5. Diseño cuidadoso:     
   La herencia múltiple puede llevar a una complejidad innecesaria si se abusa de ella. Es importante diseñar cuidadosamente las jerarquías de clases y considerar si la herencia múltiple es la mejor opción o si se pueden utilizar otras técnicas de diseño, como la composición.

6. Interfaces y mixins:    
  En Python, la herencia múltiple puede usarse para implementar mixins, que son clases que proporcionan funcionalidades adicionales a otras clases sin formar parte de la jerarquía de herencia principal. Esto puede ser útil para agregar comportamientos específicos a diferentes clases de manera modular.

>En resumen, la herencia múltiple es una característica poderosa pero compleja de la programación orientada a objetos que puede ser útil en ciertos casos, pero que también requiere un manejo cuidadoso para evitar complicaciones y ambigüedades en el diseño del programa.

# Herencia compuesta

La herencia compuesta, a veces también llamada composición, es un concepto relacionado con la reutilización de código en la programación orientada a objetos, pero difiere de la herencia tradicional en que no involucra una relación de subclase y superclase. En cambio, implica incluir objetos de otras clases como parte de la definición de una nueva clase, en lugar de heredar directamente de esas clases.

En lugar de extender la funcionalidad de una clase al heredar de ella, la herencia compuesta se basa en la idea de que un objeto puede contener o estar compuesto por otros objetos. Estos objetos se incluyen como atributos dentro de la clase que los utiliza. Esta técnica fomenta la reutilización de código y permite construir clases más flexibles y modulares.

Un ejemplo común de herencia compuesta es el patrón de diseño "Decorator" (Decorador), donde un objeto decorador envuelve a otro objeto para agregarle funcionalidad sin alterar su interfaz. Otro ejemplo es cuando una clase necesita utilizar la funcionalidad de otra clase sin ser una subclase de ella, simplemente creando una instancia de esa clase y usándola como un componente dentro de la nueva clase.

Aquí hay un ejemplo simple para ilustrar la herencia compuesta:

```python
class Motor:
    def arrancar(self):
        print("El motor arranca")

    def detener(self):
        print("El motor se detiene")

class Automovil:
    def __init__(self):
        self.motor = Motor()  # Composición: un automóvil tiene un motor

    def conducir(self):
        self.motor.arrancar()
        print("El automóvil está en movimiento")

    def estacionar(self):
        self.motor.detener()
        print("El automóvil se ha estacionado")

auto = Automovil()
auto.conducir()
auto.estacionar()

```
En este ejemplo, la clase Automovil no hereda de la clase Motor, sino que contiene una instancia de la clase Motor como un atributo (self.motor). La funcionalidad del motor se accede a través de este atributo dentro de los métodos de la clase Automovil, lo que ilustra el concepto de herencia compuesta.

## Diferencia entre Herencia

La herencia compuesta se diferencia de la herencia simple y múltiple principalmente en cómo se estructuran las relaciones entre las clases y cómo se comparten y reutilizan los comportamientos y características de esas clases.

**Herencia Simple**:

* En la herencia simple, una clase hija hereda de una única clase padre.
* La clase hija adquiere todos los atributos y métodos de la clase padre.
* Se utiliza para modelar relaciones "es-un", donde la clase hija es un tipo especializado de la clase padre.

**Herencia Múltiple**:

* En la herencia múltiple, una clase hija puede heredar de múltiples clases padres.
* La clase hija adquiere atributos y métodos de todas las clases padres.
* Se utiliza para combinar funcionalidades de múltiples clases en una nueva clase.

**Herencia Compuesta**:

* En la herencia compuesta, una clase contiene instancias de otras clases como atributos, en lugar de heredar directamente de esas clases.
* Los comportamientos y características de las clases incluidas se acceden a través de estas instancias.
* Se utiliza para incluir funcionalidades de otras clases dentro de una nueva clase sin formar una relación de subclase-superclase directa.

### Ejemplos

**Herencia Simple**:    

En este ejemplo, tenemos una clase base Animal y una subclase Perro que hereda de la clase base.

```python
class Animal:
    def sonido(self):
        print("Sonido genérico de un animal")

class Perro(Animal):
    def sonido(self):
        print("Guau!")

perro = Perro()
perro.sonido()  # Output: Guau!

```
**Herencia Múltiple**:    

En este ejemplo, tenemos dos clases base Volador y Nadador, y una subclase Pato que hereda de ambas.

```python
class Volador:
    def volar(self):
        print("El pato está volando")

class Nadador:
    def nadar(self):
        print("El pato está nadando")

class Pato(Volador, Nadador):
    pass

pato = Pato()
pato.volar()  # Output: El pato está volando
pato.nadar()  # Output: El pato está nadando

```
**Herencia Compuesta**:    

En este ejemplo, tenemos una clase Motor y una clase Automovil que contiene una instancia de Motor.

```python
class Motor:
    def arrancar(self):
        print("El motor arranca")

    def detener(self):
        print("El motor se detiene")

class Automovil:
    def __init__(self):
        self.motor = Motor()  # Composición: un automóvil tiene un motor

    def conducir(self):
        self.motor.arrancar()
        print("El automóvil está en movimiento")

    def estacionar(self):
        self.motor.detener()
        print("El automóvil se ha estacionado")

auto = Automovil()
auto.conducir()  # Output: El motor arranca, El automóvil está en movimiento
auto.estacionar()  # Output: El motor se detiene, El automóvil se ha estacionado

```
En resumen:

La herencia simple implica que una clase hija hereda de una única clase padre.
La herencia múltiple implica que una clase hija puede heredar de múltiples clases padres.
La herencia compuesta implica que una clase contiene instancias de otras clases como atributos.


## Cuando?

En cuanto a cuándo y por qué se usa la herencia compuesta:

**Cuándo usarla**:     
Se utiliza la herencia compuesta cuando una relación "tiene-un" es más apropiada que una relación "es-un". Es decir, cuando un objeto necesita utilizar los comportamientos de otro objeto sin ser una subclase de él, sino más bien conteniendo una instancia de esa clase. Además, la herencia compuesta es útil cuando se desea agregar funcionalidad a una clase existente sin modificar su interfaz pública.

**Por qué usarla**:     
La herencia compuesta promueve la modularidad y el reuso de código al permitir que los objetos se compongan de otros objetos. Esto ayuda a mantener la flexibilidad y la cohesión en el diseño del software, ya que los objetos pueden ser intercambiados fácilmente o extendidos con diferentes comportamientos sin afectar la estructura de la clase contenedora. Además, la herencia compuesta puede evitar algunos de los problemas asociados con la herencia múltiple, como los conflictos de nombres o la complejidad excesiva en la resolución de métodos.


# super()

En Python, super() es una función incorporada que se utiliza dentro de las clases para acceder y llamar a métodos de la clase padre o superclase. Proporciona una forma conveniente de llamar a métodos de la superclase desde una subclase, lo que es útil cuando se está trabajando con herencia y se necesita invocar la implementación de un método específico de la superclase.

La función super() se usa comúnmente dentro de la definición de métodos en las subclases y generalmente se invoca con dos argumentos: la clase actual y una instancia de esa clase. Por ejemplo, dentro de un método de una subclase, super() se puede usar de la siguiente manera:

```python
class SubClase(ClasePadre):
    def metodo(self):
        super().metodo()
        # Aquí va el código adicional específico de la subclase

```
En este ejemplo, super().metodo() llama al método metodo() de la superclase ClasePadre. Esto permite que la subclase SubClase herede el comportamiento de la superclase y luego agregue su propia lógica adicional si es necesario.

Es importante destacar que super() se utiliza principalmente para evitar la necesidad de hacer referencia explícita a la superclase por su nombre. Esto hace que el código sea más flexible y menos propenso a errores cuando se realizan cambios en la jerarquía de herencia.

Además, es importante tener en cuenta que super() no solo se utiliza para llamar al método \__init__() de la superclase durante la inicialización de una subclase, sino que también se puede usar para llamar a cualquier otro método de la superclase en cualquier otro contexto dentro de la subclase.

## Acceder a los métodos

super() se puede usar en cualquier tipo de herencia, ya sea herencia simple o múltiple. La función super() proporciona una forma consistente y conveniente de acceder a los métodos de la superclase, independientemente de la estructura de herencia utilizada.

En el caso de la herencia simple, donde una clase hija hereda de una única clase padre, super() se utiliza para acceder a los métodos de la clase padre. Por ejemplo:

```python
class ClasePadre:
    def metodo(self):
        print("Método de la clase padre")

class SubClase(ClasePadre):
    def metodo(self):
        super().metodo()
        print("Método de la subclase")

sub = SubClase()
sub.metodo()

```

En el caso de la herencia múltiple, donde una clase hija hereda de múltiples clases padres, super() puede ser especialmente útil para manejar el método de resolución de orden (MRO, Method Resolution Order). Python utiliza el MRO para determinar el orden en el que se buscan los métodos cuando se invoca super(). Por ejemplo:

```python
class ClasePadreA:
    def metodo(self):
        print("Método de la clase padre A")

class ClasePadreB:
    def metodo(self):
        print("Método de la clase padre B")

class SubClase(ClasePadreA, ClasePadreB):
    def metodo(self):
        super().metodo()
        print("Método de la subclase")

sub = SubClase()
sub.metodo()

```
En este ejemplo, el método metodo() de la clase SubClase utiliza super() para llamar al método de la clase ClasePadreA según el MRO, que es el orden en el que se declaran las clases en la tupla de herencia de la subclase. Esto garantiza un comportamiento predecible y consistente en la resolución de métodos, independientemente de la complejidad de la herencia.

# Excepciones en Herencias

Las excepciones en herencias se refieren a cómo las clases hijas pueden manejar excepciones heredadas de sus clases padres o superclases. Cuando una clase hija hereda de una clase padre que tiene métodos que pueden lanzar excepciones, la clase hija puede elegir manejar esas excepciones de manera diferente o adicional.

Aquí hay un ejemplo para ilustrar cómo se manejan las excepciones en herencias:

Supongamos que tenemos una clase base Animal y una subclase Perro. La clase Animal tiene un método hablar() que lanza una excepción NotImplementedError para indicar que debe ser implementado por las subclases. La clase Perro implementa este método pero también puede manejar excepciones de manera específica para los perros.

```python
class Animal:
    def hablar(self):
        raise NotImplementedError("El método hablar() debe ser implementado por las subclases.")

class Perro(Animal):
    def hablar(self):
        try:
            print("Guau!")
        except Exception as e:
            print("Error al hablar:", e)

perro = Perro()
perro.hablar()  # Output: Guau!

```
En este ejemplo:

* La clase base 'Animal' define un método 'hablar()' que lanza una excepción NotImplementedError. Esta excepción indica que cualquier subclase que no implemente este método recibirá un error si intenta llamarlo.
* La subclase 'Perro' hereda de 'Animal' y sobrescribe el método 'hablar()'. En este caso, la subclase implementa el método para que imprima "Guau!" cuando se llama.
* La subclase 'Perro' también puede manejar excepciones adicionales en su método 'hablar()'. En este ejemplo, se muestra cómo la clase 'Perro' podría manejar cualquier excepción que se produzca al hablar.

>En resumen, las excepciones en herencias en Python permiten a las clases hijas manejar excepciones heredadas de sus clases padres, además de manejar excepciones específicas de la subclase cuando sea necesario. Esto proporciona flexibilidad en el manejo de errores y permite una mayor personalización del comportamiento de manejo de excepciones en las subclases.

# Polimorfismo (3º principio POO)

El polimorfismo es un concepto fundamental en la programación orientada a objetos (POO) que se refiere a la capacidad de un objeto de una clase para presentar diferentes comportamientos según el contexto en el que se utilice. Esto significa que un objeto puede ser tratado como si fuera de un tipo diferente al que realmente pertenece, siempre y cuando sea compatible con el comportamiento esperado.

El polimorfismo se basa en dos conceptos clave:

1. **Sobrecarga de métodos**:     
  Se refiere a la capacidad de una clase para tener múltiples métodos con el mismo nombre pero diferentes parámetros. Estos métodos realizan acciones similares pero específicas para los tipos de parámetros que reciben.

2. **Sustitución de métodos**:    
  Se refiere a la capacidad de una subclase para proporcionar una implementación específica de un método heredado de su superclase. La subclase puede sobrescribir el método de la superclase con una implementación más específica o especializada.

El polimorfismo permite escribir código más genérico y flexible, ya que los objetos pueden ser tratados de manera uniforme a través de interfaces comunes, independientemente de sus tipos específicos. Esto simplifica el diseño del software y facilita la extensión y mantenimiento del código.

Un ejemplo común de polimorfismo es cuando una función o método espera un objeto de una clase específica, pero se le pasa un objeto de una subclase de esa clase. El código funcionará correctamente siempre que la subclase proporcione una implementación adecuada de los métodos esperados por la función o método.

Por ejemplo, considera una clase Animal con un método hacer_sonido():

```python
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

```

Aquí, tanto Perro como Gato son subclases de Animal, y ambas sobrescriben el método hacer_sonido(). Cuando se llama a hacer_sonido() en un objeto Perro o Gato, el método apropiado de la subclase se ejecutará, demostrando el polimorfismo en acción:

```python
perro = Perro()
print(perro.hacer_sonido())  # Output: Guau!

gato = Gato()
print(gato.hacer_sonido())   # Output: Miau!

```

El mismo método hacer_sonido() se comporta de manera diferente según el tipo de objeto al que se llama, lo que ilustra el polimorfismo.

# enumerados (Enum)

Los enumerados, conocidos como Enum, son un tipo de dato en Python que permite definir conjuntos de nombres simbólicos asociados con valores constantes. En esencia, los enumerados son una forma de crear una lista de constantes nombradas que se pueden utilizar en lugar de números o cadenas.

Los enumerados son útiles cuando necesitas representar un conjunto fijo y predefinido de valores que tienen un significado específico. Por ejemplo, los días de la semana, los meses del año, las direcciones cardinales, etc.

En Python, puedes definir un enumerado utilizando la clase Enum del módulo enum. Aquí tienes un ejemplo básico de cómo definir y usar un enumerado:

```python

from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

print(DiaSemana.LUNES)  # Output: DiaSemana.LUNES
print(DiaSemana.LUNES.value)  # Output: 1
print(DiaSemana.LUNES.name)   # Output: LUNES


```
En este ejemplo, 'DiaSemana' es un enumerado que representa los días de la semana. Cada miembro del enumerado se define como una constante nombrada con un valor asociado. Puedes acceder a los miembros del enumerado utilizando su nombre, y también puedes obtener su valor o nombre utilizando los atributos 'value' y 'name', respectivamente.

Los enumerados proporcionan una forma más legible y segura de trabajar con conjuntos predefinidos de valores, en lugar de usar números o cadenas directamente. Además, los enumerados permiten la verificación de tipos y ayudan a evitar errores de escritura o de interpretación de los valores.


# Pickle

pickle es un módulo de Python que se utiliza para serializar y deserializar objetos de Python. La serialización es el proceso de convertir un objeto en una secuencia de bytes, y la deserialización es el proceso inverso de reconstruir un objeto a partir de esa secuencia de bytes.

En esencia, pickle permite guardar objetos Python en archivos o enviarlos a través de una red y luego recuperarlos más tarde en su forma original. Esto es útil cuando necesitas guardar el estado de un objeto entre sesiones de ejecución de un programa o cuando deseas transferir objetos entre diferentes procesos o máquinas.

El módulo pickle ofrece dos funciones principales:

1. pickle.dump(objeto, archivo): Serializa el objeto y lo guarda en el archivo proporcionado como argumento.

2. pickle.load(archivo): Lee los datos serializados del archivo y los deserializa, devolviendo el objeto original.

Aquí tienes un ejemplo básico de cómo utilizar pickle para serializar y deserializar un objeto:

```python
import pickle

# Objeto a serializar
datos = {'nombre': 'Juan', 'edad': 30}

# Serializar el objeto y guardarlo en un archivo
with open('datos.pkl', 'wb') as archivo:
    pickle.dump(datos, archivo)

# Deserializar el objeto desde el archivo
with open('datos.pkl', 'rb') as archivo:
    datos_recuperados = pickle.load(archivo)

print(datos_recuperados)  # Output: {'nombre': 'Juan', 'edad': 30}

```

### Cuando se usa?

Cuando utilizas pickle para guardar un objeto en un archivo o para enviarlo a través de una red, los datos se guardan en un formato binario que puede ser leído y modificado por cualquier persona que tenga acceso al archivo o a los datos transferidos.

El módulo pickle es útil en una variedad de situaciones en las que necesitas guardar el estado de un objeto de Python para su uso posterior. Aquí hay algunas situaciones comunes en las que pickle puede ser útil:

1. Persistencia de datos: Puedes utilizar pickle para guardar el estado de un objeto de Python en un archivo para que puedas cargarlo y recuperarlo en una sesión posterior. Esto es útil para guardar y cargar datos en aplicaciones de procesamiento de datos, aplicaciones de aprendizaje automático, juegos, etc.

2. Comunicación entre procesos o máquinas: Puedes utilizar pickle para serializar objetos y enviarlos a través de una red a otros procesos o máquinas. Esto es útil para la comunicación entre componentes distribuidos de una aplicación o para enviar datos entre procesos en paralelo.

3. Cache de objetos: Puedes utilizar pickle para guardar objetos en caché en un archivo para evitar el costo de volver a calcularlos cada vez que sean necesarios. Esto es útil para almacenar resultados de cálculos costosos o datos preprocesados en aplicaciones que requieren un rendimiento óptimo.

4. Serialización de datos complejos: Puedes utilizar pickle para serializar objetos Python complejos que no son compatibles con otros formatos de serialización más simples, como JSON. Esto incluye objetos que contienen referencias circulares, objetos personalizados con métodos definidos por el usuario, etc.

Sin embargo, es importante tener en cuenta que 'pickle' no es adecuado para todas las situaciones. Por ejemplo, los archivos 'pickl'e' pueden no ser portables entre diferentes versiones de Python o entre diferentes sistemas operativos. Además, los archivos 'pickle' pueden ser vulnerables a ataques de deserialización de código malicioso si se cargan desde fuentes no confiables. Por lo tanto, debes usar 'pickle' con precaución y considerar otras alternativas, como JSON o el formato 'protocol buffers', en casos donde la portabilidad y la seguridad son preocupaciones importantes.

# Modulo

En Python, un módulo es simplemente un archivo de Python que contiene definiciones de funciones, clases y variables, así como instrucciones ejecutables. Los módulos permiten organizar el código de manera modular y reutilizable. Puedes importar y utilizar funcionalidades definidas en un módulo en otros archivos de Python utilizando la palabra clave import.

Existen diferentes tipos de módulos en Python, que pueden clasificarse en tres categorías principales:

1. Módulos estándar de Python:     
  Estos son módulos que forman parte de la biblioteca estándar de Python y se distribuyen junto con el propio lenguaje. 
  Algunos ejemplos comunes son:
* math: Proporciona funciones matemáticas estándar.
* random: Ofrece funciones para generar números aleatorios.
* os: Permite interactuar con el sistema operativo, como manipular archivos y directorios.
* datetime: Proporciona clases para trabajar con fechas y horas.

2. Módulos de terceros:    
  Estos son módulos desarrollados por la comunidad de Python, pero no forman parte de la biblioteca estándar. Pueden ser instalados utilizando herramientas como pip, el gestor de paquetes de Python. 
  Algunos ejemplos populares incluyen:
* numpy: Biblioteca para computación numérica que ofrece arrays y funciones matemáticas avanzadas.
* pandas: Herramienta para manipulación y análisis de datos que proporciona estructuras de datos flexibles.
* requests: Biblioteca HTTP para realizar peticiones web de manera sencilla.
* matplotlib: Biblioteca para la creación de gráficos y visualizaciones.

3. Módulos personalizados:    
  Estos son módulos creados por el usuario para organizar y reutilizar su propio código. Puedes crear tus propios módulos simplemente creando archivos de Python con las definiciones de funciones, clases y variables que desees utilizar en otros lugares de tu proyecto.

Para utilizar un módulo en un archivo de Python, simplemente necesitas importarlo utilizando la palabra clave **import**, seguida del nombre del módulo. Por ejemplo:

```python
import math

print(math.sqrt(25))  # Utilizando la función sqrt() del módulo math para calcular la raíz cuadrada de 25

```

Es importante tener en cuenta que los módulos deben estar instalados o presentes en el mismo directorio que el archivo de Python que los importa para que puedan ser utilizados.

## math

El módulo math es un módulo incorporado en Python que proporciona funciones matemáticas estándar. Contiene varias funciones y constantes que son útiles para realizar operaciones matemáticas comunes. Algunas de las funcionalidades más importantes que ofrece el módulo math incluyen:

1. **Funciones trigonométricas**:      
  El módulo math proporciona funciones trigonométricas estándar como seno (sin()), coseno (cos()), tangente (tan()), arcoseno (asin()), arcocoseno (acos()), arcotangente (atan()), entre otras.

2. **Funciones exponenciales y logarítmicas**:    
  Incluye funciones para calcular potencias (pow()), logaritmos naturales (log()), logaritmos en base 10 (log10()), exponenciales (exp()), entre otras.

3. **Constantes matemáticas**:    
  El módulo math también define varias constantes matemáticas importantes, como pi (pi), e (e), tau (tau), entre otras.

4. **Funciones de redondeo y truncamiento**:    
  Incluye funciones para redondear (round()), truncar (trunc()), redondear hacia arriba (ceil()), redondear hacia abajo (floor()), entre otras.

5. **Funciones de factorización y otras operaciones matemáticas**:    
  El módulo math proporciona funciones para realizar operaciones matemáticas comunes como factorial (factorial()), valor absoluto (fabs()), máximo (max()), mínimo (min()), entre otras.

Aquí tienes un ejemplo básico de cómo se utiliza el módulo math en Python:

```python
import math

# Calcular el seno de 45 grados
print(math.sin(math.radians(45)))  # Salida: 0.7071067811865475

# Calcular el logaritmo natural de 10
print(math.log(10))  # Salida: 2.302585092994046

# Imprimir el valor de pi
print(math.pi)  # Salida: 3.141592653589793

```
El módulo math es una herramienta fundamental para realizar operaciones matemáticas en Python y es ampliamente utilizado en una variedad de aplicaciones científicas, de ingeniería y matemáticas.

## random

El módulo random es otro módulo integrado en Python que se utiliza para generar números aleatorios y realizar operaciones relacionadas con aleatoriedad. Proporciona una variedad de funciones para trabajar con números aleatorios, seleccionar elementos aleatorios de secuencias, y realizar otras operaciones relacionadas con la aleatoriedad.

Algunas de las funcionalidades más importantes del módulo random incluyen:

1. **Generación de números aleatorios**:    
  El módulo 'random' proporciona funciones para generar números aleatorios de diferentes tipos, incluyendo números enteros (randint()), números de punto flotante en el rango [0.0, 1.0) (random()), y números de punto flotante con una distribución gaussiana (gauss()).

2. **Selección aleatoria de elementos**:    
  Incluye funciones para seleccionar elementos aleatorios de secuencias, como listas, tuplas, y rangos. Algunas de estas funciones son choice(), sample(), y shuffle().

3. **Establecimiento de semillas**:    
  Permite establecer la semilla inicial para el generador de números aleatorios utilizando la función seed(). Esto es útil para reproducir resultados aleatorios en diferentes ejecuciones del programa.

4. **Generación de secuencias aleatorias**:    
  El módulo random también proporciona funciones para generar secuencias aleatorias, como randrange() para generar números aleatorios dentro de un rango específico con un paso determinado, y choices() para generar secuencias de elementos aleatorios con reemplazo.

Aquí tienes un ejemplo básico de cómo se utiliza el módulo random en Python:

```python
import random

# Generar un número aleatorio entre 1 y 100
print(random.randint(1, 100))  # Salida: un número aleatorio entre 1 y 100

# Seleccionar un elemento aleatorio de una lista
lista = ['a', 'b', 'c', 'd', 'e']
print(random.choice(lista))  # Salida: un elemento aleatorio de la lista

# Barajar una lista aleatoriamente
random.shuffle(lista)
print(lista)  # Salida: una permutación aleatoria de la lista original

```
El módulo random es una herramienta muy útil para generar aleatoriedad en tus programas y es ampliamente utilizado en una variedad de aplicaciones, como juegos, simulaciones, y pruebas. Sin embargo, es importante tener en cuenta que los números generados por las funciones en random son pseudo-aleatorios y dependen de una semilla inicial, por lo que pueden ser reproducibles si se fija la semilla inicial.

## time

En Python, time es un módulo estándar que proporciona funciones relacionadas con la medición del tiempo y la manipulación de fechas y horas. Algunas de las funcionalidades más comunes que ofrece este módulo incluyen:

Obtener la hora actual.
Medir el tiempo transcurrido durante la ejecución de un bloque de código.
Convertir entre representaciones de tiempo, como timestamps y objetos datetime.
Realizar operaciones aritméticas con fechas y horas, como sumar o restar días, horas, etc.
Suspender la ejecución de un programa durante un cierto período de tiempo.
Aquí tienes un ejemplo de cómo puedes usar el módulo time en Python:

```python
import time

# Obtener la hora actual
hora_actual = time.localtime()
print("Hora actual:", hora_actual)

# Medir el tiempo transcurrido
inicio = time.time()
# Simular alguna operación que tome tiempo
time.sleep(2)
fin = time.time()
tiempo_transcurrido = fin - inicio
print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")

```

Este código importa el módulo time, obtiene la hora actual utilizando time.localtime() y mide el tiempo transcurrido entre dos puntos utilizando time.time(). También se utiliza time.sleep(2) para suspender la ejecución del programa durante 2 segundos como ejemplo de pausa en la ejecución.

## timeit

'timeit' es un módulo en Python que se utiliza para medir el tiempo de ejecución de pequeños fragmentos de código. Es útil cuando necesitas comparar el rendimiento de diferentes implementaciones o algoritmos, o cuando deseas optimizar partes críticas de tu código.

El módulo timeit proporciona una interfaz simple para medir el tiempo de ejecución de un fragmento de código en varias repeticiones. Se encarga automáticamente de ejecutar el código múltiples veces para obtener una estimación más precisa del tiempo de ejecución y manejar factores como la carga de trabajo del sistema y otras fluctuaciones de tiempo.

Aquí hay un ejemplo básico de cómo usar timeit para medir el tiempo de ejecución de un fragmento de código:

```python
import timeit

# Definir el código que quieres medir
codigo = '''
suma = 0
for i in range(1000000):
    suma += i
'''

# Medir el tiempo de ejecución del código
tiempo = timeit.timeit(stmt=codigo, number=10)  # Ejecutar el código 10 veces
print("Tiempo de ejecución:", tiempo, "segundos")

```

En este ejemplo, la variable 'codigo' contiene el fragmento de código que queremos medir. Luego, utilizamos la función 'timeit.timeit()' para medir el tiempo de ejecución de este código. El parámetro 'stmt' recibe el código que queremos medir, y el parámetro 'number' especifica cuántas veces queremos que se ejecute el código para calcular el tiempo medio de ejecución. En este caso, se ejecuta el código 10 veces. El resultado es el tiempo medio de ejecución del código en segundos.

El módulo timeit es una herramienta útil para medir el rendimiento de pequeños fragmentos de código y optimizar tu código Python. Te ayuda a identificar qué partes de tu código son más lentas y dónde puedes concentrar tus esfuerzos de optimización.

## datetime

El módulo datetime en Python proporciona clases para manejar fechas y horas de una manera más conveniente. Esto incluye la capacidad de crear objetos de fecha, hora y fecha/hora, así como realizar operaciones como cálculos de diferencia entre fechas, formatos de fecha y hora, y más.

Aquí tienes algunos ejemplos de cómo puedes usar el módulo datetime:

#### Obtener la fecha y hora actual:

```python
import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()

print("Fecha y hora actual:", fecha_actual)

```

#### Crear un objeto de fecha específica:

```python
import datetime

# Crear un objeto de fecha específica
mi_fecha = datetime.date(2022, 12, 31)

print("Fecha específica:", mi_fecha)

```

#### Crear un objeto de fecha/hora específica:

```python
import datetime

# Crear un objeto de fecha/hora específica
mi_fecha_hora = datetime.datetime(2022, 12, 31, 23, 59, 59)

print("Fecha/hora específica:", mi_fecha_hora)

```

#### Formatear una fecha o hora:

```python
import datetime

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()

# Formatear la fecha
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")

print("Fecha formateada:", fecha_formateada)

```

#### Calcular la diferencia entre dos fechas:

```python
import datetime

# Crear dos fechas
fecha1 = datetime.date(2022, 1, 1)
fecha2 = datetime.date(2023, 1, 1)

# Calcular la diferencia entre las fechas
diferencia = fecha2 - fecha1

print("Diferencia de días entre las fechas:", diferencia.days)

```

#### Obtener el día de la semana:

```python
import datetime

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()

# Obtener el día de la semana (lunes = 0, martes = 1, ..., domingo = 6)
dia_semana = fecha_actual.weekday()

print("Día de la semana:", dia_semana)

```

#### Reemplazar:

```python
import datetime

# Crear un objeto de datetime
fecha_hora = datetime.datetime(2022, 12, 31, 23, 59, 59)

print("Fecha/hora original:", fecha_hora)

# Reemplazar el año con 2023
nueva_fecha_hora = fecha_hora.replace(year=2023)

print("Fecha/hora modificada (año reemplazado por 2023):", nueva_fecha_hora)

# Reemplazar el mes con 6
nueva_fecha_hora = fecha_hora.replace(month=6)

print("Fecha/hora modificada (mes reemplazado por junio):", nueva_fecha_hora)

# Reemplazar la hora con 12
nueva_fecha_hora = fecha_hora.replace(hour=12)

print("Fecha/hora modificada (hora reemplazada por 12):", nueva_fecha_hora)

```

#### Formatear un objeto de fecha/datetime

```python
import datetime

# Crear un objeto de datetime
fecha_hora = datetime.datetime(2022, 12, 31, 23, 59, 59)

# Formatear la fecha/hora como una cadena de texto
cadena_formateada = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

print("Fecha/hora formateada:", cadena_formateada)

```
En este ejemplo, %Y, %m, %d, %H, %M y %S son códigos de formato que se utilizan para representar diferentes partes de la fecha y la hora. Por ejemplo:

* %Y: Año con cuatro dígitos
* %m: Mes con dos dígitos (01-12)
* %d: Día del mes con dos dígitos (01-31)
* %H: Hora en formato de 24 horas (00-23)
* %M: Minuto con dos dígitos (00-59)
* %S: Segundo con dos dígitos (00-59)    

Puedes combinar estos códigos de formato con otros caracteres fijos para construir el formato de fecha/hora deseado. Por ejemplo, "%Y-%m-%d %H:%M:%S" produce una cadena de texto con el formato "YYYY-MM-DD HH:MM:SS".

El módulo datetime proporciona muchas más funcionalidades que estas, pero estos ejemplos deberían darte una buena idea de cómo empezar a trabajar con fechas y horas en Python utilizando este módulo.

### datetime / time

El módulo datetime de Python incluye la clase time, que se utiliza para representar una hora específica del día, sin incluir información sobre la fecha. Aquí tienes un ejemplo de cómo se utiliza la clase time con comentarios explicativos:

```python
import datetime

# Crear un objeto de hora específica (hora:minuto:segundo)
hora_actual = datetime.time(14, 30, 15)

# Imprimir la hora actual
print("Hora actual:", hora_actual)

# Acceder a los atributos de hora, minuto y segundo
print("Hora:", hora_actual.hour)      # Salida: 14
print("Minuto:", hora_actual.minute)  # Salida: 30
print("Segundo:", hora_actual.second) # Salida: 15

# Formatear la hora utilizando strftime()
hora_formateada = hora_actual.strftime("%H:%M:%S")

# Imprimir la hora formateada
print("Hora formateada:", hora_formateada)

```
En este ejemplo:

* Creamos un objeto de hora específica utilizando datetime.time(hora, minuto, segundo).
* Imprimimos la hora actual utilizando el método print().
* Accedemos a los atributos de hora (hour), minuto (minute) y segundo (second) del objeto de tiempo.
* Formateamos la hora utilizando el método strftime() para obtener una representación de cadena formateada de la hora en formato HH:MM:SS.
* Imprimimos la hora formateada.

### datetime / timedelta

'timedelta' es una clase dentro del módulo datetime de Python que se utiliza para representar una **duración de tiempo, es decir, un período de tiempo definido por una cantidad específica de días, horas, minutos, segundos y microsegundos.

Esta clase es útil para realizar operaciones aritméticas en fechas y horas. Por ejemplo, puedes sumar o restar un timedelta a una fecha o hora para calcular una nueva fecha o hora.

Aquí tienes un ejemplo de cómo se utiliza timedelta:

```python
import datetime

# Crear un objeto timedelta representando 10 días
delta = datetime.timedelta(days=10)

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()

# Sumar el timedelta a la fecha actual para obtener una nueva fecha
nueva_fecha = fecha_actual + delta

print("Fecha actual:", fecha_actual)
print("Nueva fecha después de 10 días:", nueva_fecha)

```
En este ejemplo, creamos un objeto timedelta llamado delta que representa un período de 10 días. Luego, obtenemos la fecha y hora actual utilizando datetime.now(). Sumamos el timedelta a la fecha actual para obtener una nueva fecha que es 10 días en el futuro. La operación de suma (+) con timedelta se encarga automáticamente de manejar correctamente los cambios de mes y año si son necesarios.

# Colecciones especiales (Módulo)

El módulo **collections** en Python proporciona colecciones especializadas y de alto rendimiento que van más allá de las estructuras de datos básicas ofrecidas por el lenguaje. Estas colecciones son útiles en una variedad de situaciones y pueden simplificar el código al proporcionar implementaciones optimizadas de estructuras de datos comunes. Algunas de las colecciones más comunes en este módulo son:

1. **Counter**:     
  Es una subclase de diccionario que se utiliza para contar la frecuencia de elementos en una secuencia. Es especialmente útil para conteos de elementos en listas, tuplas u otras colecciones iterables.    
* Uso: Contar la frecuencia de elementos en una secuencia, como caracteres en una cadena, elementos en una lista, etc.

Ejemplo:

```python
from collections import Counter

# Contar la frecuencia de caracteres en una cadena
cadena = "hola mundo"
conteo = Counter(cadena)
print(conteo)
# Salida: Counter({'o': 2, ' ': 1, 'h': 1, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1})

```

2. **deque**:     
  Es una doble lista enlazada optimizada para operaciones de inserción y eliminación eficientes tanto al principio como al final de la lista. Es útil cuando necesitas una cola o una pila eficiente.
* Uso: Implementar una cola o una pila donde necesitas inserciones y eliminaciones eficientes tanto al principio como al final de la colección.

Ejemplo con agregar:

```python
from collections import deque

# Crear una cola con deque
cola = deque()
cola.append(1)  # Agregar al final
cola.appendleft(2)  # Agregar al principio
print(cola)  # Salida: deque([2, 1])

``` 

Eliminar elementos de un deque utilizando el método pop() y popleft() para eliminar elementos del final y del principio de la cola respectivamente:

Ejemplo con eliminar:

```python
from collections import deque

# Crear una cola con deque
cola = deque([1, 2, 3, 4, 5])

# Eliminar un elemento del final de la cola
elemento_final = cola.pop()
print("Elemento eliminado del final:", elemento_final)  # Salida: 5
print("Cola después de eliminar del final:", cola)  # Salida: deque([1, 2, 3, 4])

# Eliminar un elemento del principio de la cola
elemento_principio = cola.popleft()
print("Elemento eliminado del principio:", elemento_principio)  # Salida: 1
print("Cola después de eliminar del principio:", cola)  # Salida: deque([2, 3, 4])

```

3. **namedtuple**:     
  Es una fábrica de tipos de tuplas con nombres de campo. Proporciona una forma de crear tuplas con campos nombrados, lo que hace que el código sea más legible y autodocumentado.
* Uso: Crear estructuras de datos simples pero autodocumentadas, especialmente cuando necesitas una tupla con campos nombrados.

Ejemplo:

```python
from collections import namedtuple

# Definir una tupla con campos nombrados
Persona = namedtuple("Persona", ["nombre", "edad"])
persona1 = Persona("Juan", 30)
print(persona1.nombre, persona1.edad)  # Salida: Juan 30

```

4. **defaultdict**:     
  Es una subclase de diccionario que proporciona un valor predeterminado para claves que no están presentes en el diccionario. Es útil para contar elementos o asignar valores predeterminados sin la necesidad de verificar la existencia de claves.
* Uso: Asignar valores predeterminados o contar elementos sin la necesidad de verificar la existencia de claves.

Ejemplo:

```python
from collections import defaultdict

# Crear un defaultdict con int como valor predeterminado
d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(d)  # Salida: defaultdict(<class 'int'>, {'a': 1, 'b': 2})

```

Estas son solo algunas de las colecciones especializadas disponibles en el módulo collections. Cada una tiene sus propias características y casos de uso específicos, lo que las hace valiosas para diferentes escenarios de programación.

## _make

En Python, **_make** no es una función o método estándar del lenguaje. Sin embargo, puede estar relacionado con el método **namedtuple._make()** que se utiliza para crear una nueva instancia de una tupla nombrada utilizando una secuencia iterable de valores.

Cuando defines una tupla nombrada utilizando 'namedtuple', puedes crear instancias de esa tupla utilizando el método '_make()'. Este método toma una secuencia iterable de valores y los asigna a los campos de la tupla en el mismo orden en que fueron definidos.

Aquí tienes un ejemplo para clarificarlo:

```python
from collections import namedtuple

# Definir una tupla nombrada llamada Punto con los campos x e y
Punto = namedtuple("Punto", ["x", "y"])

# Crear una instancia de Punto utilizando _make()
coordenadas = (3, 5)
punto = Punto._make(coordenadas)

print(punto)
# Output: Punto(x=3, y=5)

```
En este ejemplo, 'Punto._make(coordenadas)' crea una nueva instancia de 'Punto' utilizando los valores '(3, 5)' de la secuencia 'coordenadas', asignándolos a los campos 'x' e 'y' en el mismo orden en que fueron definidos en la tupla nombrada.