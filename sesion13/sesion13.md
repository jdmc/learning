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

En resumen, la herencia simple es un concepto fundamental en la programación orientada a objetos que promueve la reutilización de código, la organización estructurada del programa y la creación de relaciones "es-un" entre las clases. Es una herramienta poderosa para el diseño de software modular y extensible.


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

En resumen, la herencia múltiple es una característica poderosa pero compleja de la programación orientada a objetos que puede ser útil en ciertos casos, pero que también requiere un manejo cuidadoso para evitar complicaciones y ambigüedades en el diseño del programa.

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

En resumen, las excepciones en herencias en Python permiten a las clases hijas manejar excepciones heredadas de sus clases padres, además de manejar excepciones específicas de la subclase cuando sea necesario. Esto proporciona flexibilidad en el manejo de errores y permite una mayor personalización del comportamiento de manejo de excepciones en las subclases.

# Polimorfismo


# coleccion especiales

# pickle