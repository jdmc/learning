# Operadores

""" Los operadores en Python son símbolos especiales que indican que se debe realizar una operación.

Los operandos son los valores sobre los que actúa un operador.

Hay muchos tipos diferentes de operadores en Python, incluyendo:

Operadores aritméticos: Se utilizan para realizar operaciones matemáticas, como sumar, restar, multiplicar y dividir.
Operadores de comparación: Se utilizan para comparar dos valores, como si son iguales, mayores o menores.
Operadores lógicos: Se utilizan para realizar operaciones lógicas, como and, or y not.
Operadores de asignación: Se utilizan para asignar un valor a una variable.
Operadores de pertenencia: Se utilizan para comprobar si un valor está presente en una secuencia.
Operadores de identidad: Se utilizan para comprobar si dos variables se refieren al mismo objeto. 

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

Python
print(10 % 3)  # Salida: 1
print(11 % 3)  # Salida: 2
print(12 % 3)  # Salida: 0

En este ejemplo, 
el resto de la división de 10 por 3 es 1,  >> 10 dividido por 3 es 3 con un resto de 1.
el resto de la división de 11 por 3 es 2,
y el resto de la división de 12 por 3 es 0.

2. Formateo de cadenas:

El operador % también se puede usar para formatear cadenas. 
Se utiliza para reemplazar las marcas de posición en una cadena con valores específicos.

Ejemplo:

Python
nombre = "Juan"
edad = 30

print("Hola, %s! Tienes %d años." % (nombre, edad))  

# Salida: "Hola, Juan! Tienes 30 años."


En este ejemplo, las marcas de posición %s y %d se reemplazan con el valor de la variable nombre y la variable edad, respectivamente.

El operador % es una herramienta útil para realizar operaciones matemáticas y formatear cadenas en Python.
El operador % también se puede usar para formatear fechas, horas y otros tipos de datos.

!!! Es importante tener en cuenta que el operador % para formateo de cadenas está obsoleto en Python 3. 
Se recomienda usar la función format() o f-strings para formatear cadenas en Python 3.

Es importante tener en cuenta que el operador % tiene un orden de precedencia más bajo que los operadores aritméticos.

En la expresión 2 + 3 % 4, la suma se realiza primero, por lo que el resultado es 5.


"""