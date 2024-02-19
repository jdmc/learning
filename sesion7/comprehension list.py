#Comprehension list

""" Las comprensiones de listas son una herramienta poderosa en Python que te permite crear listas de forma concisa y eficiente. 
Son una alternativa a los bucles for tradicionales para crear listas.

Sintaxis:

nueva_lista = [expresion for elemento in iterable if condicion]

Explicación:
[]: Indica que estamos creando una lista.
nueva_lista: Es la variable que almacenará la nueva lista.
expresion: Es la expresión que se evalúa para cada elemento del iterable.
iterable: Es la lista u otro tipo de secuencia sobre la que se itera.
condicion: Es una expresión booleana opcional que se utiliza para filtrar los elementos del iterable.

Ejemplo:

numeros = [1, 2, 3, 4, 5]

cuadrados = [numero**2 for numero in numeros]

print(cuadrados) # Imprime [1, 4, 9, 16, 25]

En este ejemplo, la comprensión de lista crea una nueva lista llamada pares que solo contiene los números pares de la lista numeros.
La comprensión de listas crea una nueva lista cuadrados que contiene los cuadrados de los elementos de la lista numeros. 
La expresión numero**2 se evalúa para cada elemento de numeros y el resultado se agrega a la nueva lista.


En resumen, las comprensiones de listas son una herramienta poderosa en Python que te permite crear listas de forma concisa, eficiente y legible.
 """
# [expresión for elemento in iterable if condición]

""" Explicación:

expresión: La expresión que se evalúa para cada elemento del iterable.
for elemento in iterable: La iteración sobre el iterable.
if condición: La condición que se evalúa para cada elemento del iterable. 
Solo se incluyen los elementos que cumplen la condición.

Ventajas de las comprensiones de listas:

Concisión: Permiten crear listas de forma más concisa que con bucles for.
Eficiencia: Son más eficientes que los bucles for en algunos casos.
Legibilidad: Pueden mejorar la legibilidad del código, especialmente cuando se usan expresiones simples.

Desventajas de las comprensiones de listas:

Dificultad de depuración: Puede ser más difícil depurar el código que usa comprensiones de listas.
Falta de nombre: La expresión dentro de la comprensión de lista no tiene nombre, lo que puede dificultar la comprensión del propósito del código.
Cuándo usar comprensiones de listas:

Cuando necesitas crear una lista a partir de otra lista.
Cuando la lógica para crear la lista es simple.
Cuando quieres mejorar la legibilidad del código. 

En resumen, las comprensiones de listas son una herramienta poderosa para crear nuevas listas a partir de listas existentes de forma concisa y eficiente.
"""

#listas
#comprehension list

lista = list()
lista2 = [1,2,3,4]

#numeros_20 = list(range(20))
numeros_20 = range(20)

numeros_20_actualizado = [numero * 2 for numero in numeros_20]
#print(numeros_20)
#print(numeros_20_actualizado)

elevar_cuadrado = lambda numero : numero ** 2

numeros_20_actualizado_v2 = [elevar_cuadrado(numero) for numero in numeros_20]
print(numeros_20_actualizado_v2)

es_impar = lambda n: n % 2 != 0

#procesar, de numeros_20, solo los impares
numeros_20_impares = [numero - 1 for numero in numeros_20 if numero % 2 != 0] # muestra pares por el "numero - 1"
#[numero - 1 for numero in numeros_20 if es_impar(numero)]

print(numeros_20_impares)

#ejercicio comprehension list

alumnos = [('Paco', 8), ('Carmen', 7.5), ('Julio',5)]
lista_aprobado_7 = [alumno for alumno in alumnos if alumno[1] >=7.0]
print(lista_aprobado_7)

