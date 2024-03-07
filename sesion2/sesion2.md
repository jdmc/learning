[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
# Operadores

Los operadores en Python son símbolos especiales que indican que se debe realizar una operación.

Los operandos son los valores sobre los que actúa un operador.

Hay muchos tipos diferentes de operadores en Python, incluyendo:

* Operadores aritméticos: Se utilizan para realizar operaciones matemáticas, como sumar, restar, multiplicar y dividir.
* Operadores de comparación: Se utilizan para comparar dos valores, como si son iguales, mayores o menores.
* Operadores lógicos: Se utilizan para realizar operaciones lógicas, como and, or y not.
* Operadores de asignación: Se utilizan para asignar un valor a una variable.
* Operadores de pertenencia: Se utilizan para comprobar si un valor está presente en una secuencia.
* Operadores de identidad: Se utilizan para comprobar si dos variables se refieren al mismo objeto.


| Operador |      Descripción      | Ejemplo              |
|----------|-----------------------|----------------------|
| +        | Suma                  | 2 + 3 = 5            |
| -        | Resta                 | 5 - 2 = 3            |
| *        | Multiplicación        | 2 * 3 = 6            |
| /        | División              | 6 / 2 = 3            |
| ==       | Igualdad              | 2 == 2               |
| !=       | Desigualdad           | 2 != 3               |
| <        | Menor que             | 2 < 3                |
| <=       | Menor o igual que     | 2 <= 3               |
| >        | Mayor que             | 3 > 2                |
| >=       | Mayor o igual que     | 3 >= 2               |
| and      | Y lógico              | True and True = True |
| or       | O lógico              | False or True = True |
| not      | No lógico             | not True = False     |
| =        | Asignación            | x = 5                |
| in       | Pertenencia           | 2 in [1, 2, 3]       |
| is       | Identidad             | x is y               |


*** El operador % en Python se utiliza para realizar dos operaciones diferentes:

1. Módulo:
  El módulo es el resto de la división entre dos números. 
  El operador % devuelve el resto de la división del primer operando por el segundo operando.

Ejemplo:

```Python
print(10 % 3)  # Salida: 1
print(11 % 3)  # Salida: 2
print(12 % 3)  # Salida: 0
```

En este ejemplo, 
el resto de la división de 10 por 3 es 1,  >> 10 dividido por 3 es 3 con un resto de 1.
el resto de la división de 11 por 3 es 2,
y el resto de la división de 12 por 3 es 0.

2. Formateo de cadenas:
  El operador % también se puede usar para formatear cadenas. 
  Se utiliza para reemplazar las marcas de posición en una cadena con valores específicos.

Ejemplo:

```Python
nombre = "Juan"
edad = 30

print("Hola, %s! Tienes %d años." % (nombre, edad))  

# Salida: "Hola, Juan! Tienes 30 años."
```

En este ejemplo, las marcas de posición %s y %d se reemplazan con el valor de la variable nombre y la variable edad, respectivamente.

El operador % es una herramienta útil para realizar operaciones matemáticas y formatear cadenas en Python.
El operador % también se puede usar para formatear fechas, horas y otros tipos de datos.

!!! Es importante tener en cuenta que el operador % para formateo de cadenas está obsoleto en Python 3. 
Se recomienda usar la función format() o f-strings para formatear cadenas en Python 3.

Es importante tener en cuenta que el operador % tiene un orden de precedencia más bajo que los operadores aritméticos.

En la expresión 2 + 3 % 4, la suma se realiza primero, por lo que el resultado es 5.


# Objeto

En Python, todo es un objeto. Un objeto es una **instancia de una clase**, y una clase es como un plano o una plantilla que define la estructura y el comportamiento de los objetos. Los objetos en Python pueden ser de diferentes tipos, como números, cadenas, listas, diccionarios, funciones, módulos, clases y más.

## Instancia de una clase
Para entender qué significa una "instancia de clases", es importante comprender primero los conceptos de instancia y clase por separado:

### Instancia:     
En programación orientada a objetos, una instancia es un objeto **específico** creado a partir de una clase. Cuando instancias una clase, estás creando una versión única y concreta de esa clase, con su propio conjunto de atributos y métodos.

### Clase: 
Una clase es una plantilla/manual que define cómo se deben crear las instancias. Define los atributos (variables) y métodos (funciones) que estarán disponibles en las instancias creadas a partir de ella.

Con estos conceptos en mente, una "instancia de clases" se refiere simplemente a un **objeto individual** creado a partir de una clase específica. Es el resultado de aplicar la plantilla definida por la clase para crear un objeto concreto con sus propios atributos y métodos.

Por ejemplo, si tienes una clase Perro que define características como raza, edad, y métodos como ladrar() y correr(), puedes crear múltiples instancias de esta clase, cada una representando un perro diferente con sus propias características específicas, como una raza diferente o una edad diferente. Cada instancia es como un clon adaptado y modificado desde la base que es la clase.

Entonces, en resumen, una instancia de clases es un objeto específico que se ha creado a partir de una clase particular. Es una instancia única y concreta de esa clase en particular, con su propio estado y comportamiento.

Ahora que comprendemos el concepto de instancia de clase, podemos profundizar en los **atributos** y **métodos** que están dentro de esas instancias.

### Atributos

Los atributos son variables asociadas a cada instancia de clase. Estos representan **características o propiedades** del objeto. Los atributos pueden ser variables de instancia (definidas dentro de los métodos de la clase y accesibles mediante self) o variables de clase (definidas fuera de los métodos y compartidas por todas las instancias de la clase).

### Métodos
Los métodos son **funciones** asociadas a cada instancia de clase que pueden realizar operaciones en el objeto o acceder y modificar sus atributos. Los métodos pueden ser métodos de instancia (que operan en una instancia específica y reciben self como primer parámetro) o métodos de clase (que operan en la clase misma y pueden acceder a los atributos de clase).

A continuación, un ejemplo simplificado que demuestra cómo se definen y usan atributos y métodos en una clase:

```python
class Perro:
    # Atributo de clase
    especie = "Canino"

    # Método inicializador
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad

    # Método de instancia
    def ladrar(self):
        return f"{self.nombre} está ladrando."

    # Método de instancia
    def correr(self):
        return f"{self.nombre} está corriendo."


# Crear instancias de la clase Perro
perro1 = Perro("Buddy", 3)
perro2 = Perro("Max", 5)

# Acceder a los atributos
print(perro1.nombre)  # Salida: Buddy
print(perro2.edad)    # Salida: 5

# Llamar a métodos de instancia
print(perro1.ladrar())  # Salida: Buddy está ladrando.
print(perro2.correr())  # Salida: Max está corriendo.

```


En el ejemplo proporcionado, Perro es la clase, no la instancia. La clase Perro define la plantilla o el plano para crear objetos de tipo perro. Cuando creamos objetos utilizando esta clase, como perro1 = Perro("Buddy", 3), Perro("Buddy", 3) es la instancia de la clase Perro, que en este caso llamamos perro1.

* La clase Perro es una plantilla que define cómo deben ser los objetos de tipo perro.
* Cuando creamos un objeto usando la clase Perro, por ejemplo, perro1 = Perro("Buddy", 3), estamos creando una instancia de la clase Perro llamada perro1.
* De manera similar, cuando creamos otro objeto como perro2 = Perro("Max", 5), estamos creando otra instancia de la clase Perro llamada perro2.

Para aclarar:

* Perro es la clase, que define la estructura y el comportamiento de los objetos de tipo perro.
* perro1 es una instancia de la clase Perro, creada a partir de la clase Perro usando el constructor \__init__.

En este ejemplo, nombre y edad son atributos de instancia, y ladrar() y correr() son métodos de instancia. especie es un atributo de clase, compartido por todas las instancias de la clase Perro.

Cada instancia tiene sus propios atributos y métodos, pero comparten la misma estructura definida por la clase.

Aquí hay algunos puntos clave sobre los objetos en Python:

1. Instancias de clases:     
  Cuando creas un objeto en Python, estás creando una instancia de una clase. Por ejemplo, cuando haces 'mi_numero = 10', estás creando un objeto de tipo entero (int) que representa el número 10.

2. Atributos y métodos:     
  Los objetos pueden tener atributos y métodos. 
  * Los atributos son variables asociadas al objeto, 
  * mientras que los métodos son funciones asociadas al objeto.    

  Puedes acceder a los atributos y métodos de un objeto utilizando la notación de punto (objeto.atributo o objeto.metodo()).

3. Herencia y polimorfismo:     
  En Python, las clases pueden heredar atributos y métodos de otras clases (herencia). Esto significa que los objetos pueden compartir comportamientos y características comunes. Además, el polimorfismo permite que los objetos de diferentes clases se comporten de manera similar cuando se utilizan de ciertas maneras.

4. Identidad, tipo y valor:     
  Cada objeto en Python tiene una identidad única, un tipo que define qué clase lo instancia y un valor que representa su contenido. Puedes obtener la identidad de un objeto utilizando la función id(), su tipo con la función type(), y su valor simplemente accediendo al objeto.

Por ejemplo, en el siguiente código:

```python

mi_numero = 10
print(type(mi_numero))  # Salida: <class 'int'>
print(mi_numero.bit_length())  # Salida: 4 (método de objeto entero)
```

mi_numero es un objeto de tipo entero (int) con un valor de 10. Puedes llamar al método bit_length() en este objeto para obtener el número de bits necesarios para representar el valor 10 en binario.

En resumen, en Python, los objetos son entidades fundamentales que representan datos y comportamientos. La orientación a objetos en Python proporciona un enfoque poderoso para organizar y estructurar código de manera modular y reutilizable.

# Convención programa principal 

La línea \if __name__ == "__main__": es una convención comúnmente utilizada en Python para determinar si un script se está ejecutando como el programa principal o si está siendo importado como un módulo en otro script.

Cuando un archivo Python se ejecuta, Python establece una serie de variables especiales. La variable \__name__ es una de ellas. Cuando un archivo Python se ejecuta como el programa principal, el valor de \__name__ es establecido como "\__main__". Sin embargo, si el archivo se importa como un módulo en otro script, el valor de \__name__ se establece como el nombre del módulo (es decir, el nombre del archivo sin la extensión .py).

Entonces, la línea \if \__name__ == "\__main__": se utiliza para ejecutar cierto código solo cuando el archivo se está ejecutando como el programa principal, y no cuando se está importando como un módulo.

Por ejemplo, supongamos que tenemos un archivo llamado mi_script.py con el siguiente contenido:

```python
def funcion_principal():
    print("Este es el programa principal")

if __name__ == "__main__":
    funcion_principal()

```
Cuando ejecutas mi_script.py, el mensaje "Este es el programa principal" se imprimirá en la consola. Sin embargo, si importas mi_script.py en otro script, la función funcion_principal() no se ejecutará automáticamente. Esto permite que el código dentro del bloque if __name__ == "__main__": se utilice como punto de entrada cuando el archivo se ejecuta como un script independiente, pero no cuando se importa como un módulo.

