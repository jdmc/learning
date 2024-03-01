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

Operador	Descripción	Ejemplo
\+	           Suma	             2 + 3 = 5    
\-	           Resta	         5 - 2 = 3    
\*	           Multiplicación	 2 * 3 = 6    
\/	           División	         6 / 2 = 3    
\==	           Igualdad	         2 == 2   
\!=	           Desigualdad	     2 != 3    
\<	           Menor que	     2 < 3    
\<=	           Menor o igual que 2 <= 3    
\>	           Mayor que	     3 > 2    
\>=	           Mayor o igual que 3 >= 2    
\and	           Y lógico	         True and True = True    
\or	           O lógico	         False or True = True    
\not	           No lógico	     not True = False    
\=	           Asignación	     x = 5     
\in	           Pertenencia	     2 in [1, 2, 3]     
\is	           Identidad	     x is y     


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

En Python, todo es un objeto. Un objeto es una instancia de una clase, y una clase es como un plano o una plantilla que define la estructura y el comportamiento de los objetos. Los objetos en Python pueden ser de diferentes tipos, como números, cadenas, listas, diccionarios, funciones, módulos, clases y más.

Aquí hay algunos puntos clave sobre los objetos en Python:

1. Instancias de clases:     
  Cuando creas un objeto en Python, estás creando una instancia de una clase. Por ejemplo, cuando haces mi_numero = 10, estás creando un objeto de tipo entero (int) que representa el número 10.

2. Atributos y métodos:     
  Los objetos pueden tener atributos y métodos. Los atributos son variables asociadas al objeto, mientras que los métodos son funciones asociadas al objeto. Puedes acceder a los atributos y métodos de un objeto utilizando la notación de punto (objeto.atributo o objeto.metodo()).

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


