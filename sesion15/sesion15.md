[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# generadores 

Los generadores en Python son una forma poderosa y eficiente de trabajar con secuencias de datos de manera perezosa, es decir, generan valores sobre la marcha en lugar de almacenarlos todos en la memoria al mismo tiempo. Los generadores permiten iterar sobre grandes conjuntos de datos de manera eficiente sin la necesidad de almacenar todos los valores en la memoria al mismo tiempo, lo que puede ser útil para conjuntos de datos potencialmente infinitos o para optimizar el uso de la memoria en general.

En Python, los generadores se crean utilizando funciones generadoras o expresiones generadoras. 

Aquí hay dos formas comunes de crear generadores:

## Funciones generadoras: 

  Son funciones que utilizan la palabra clave **yield** en lugar de return. Cuando una función generadora se llama, devuelve un objeto generador que puede iterarse para producir los valores generados por la función.

```python
def generador():
    yield 1
    yield 2
    yield 3

gen = generador()
for valor in gen:
    print(valor)  # Salida: 1, 2, 3
```
### stop iteration

Cuando iteras sobre un generador y este ha agotado todos sus elementos, se produce una excepción llamada StopIteration. Esta excepción es internamente manejada por Python y se utiliza para señalar que no hay más elementos para iterar en el generador.

Aquí tienes un ejemplo práctico que muestra cómo se produce la excepción StopIteration al iterar sobre un generador:

```python
def generador():
    yield 1
    yield 2
    yield 3

gen = generador()

# Iterar sobre el generador
try:
    while True:
        valor = next(gen)
        print(valor)
except StopIteration:
    print("Se alcanzó el final del generador.")

```
En este ejemplo:

* Definimos una función generadora llamada generador() que produce tres valores.
* Creamos un objeto generador llamado gen llamando a la función generador().
* Iteramos sobre el generador utilizando un bucle while y la función next(), que obtiene el siguiente valor del generador en cada iteración.
* Cuando el generador se agota y no hay más elementos para iterar, se produce la excepción StopIteration.
* Capturamos la excepción utilizando un bloque try y except, e imprimimos un mensaje indicando que se alcanzó el final del generador.

Este ejemplo ilustra cómo Python maneja internamente la excepción StopIteration cuando iteras sobre un generador y no hay más elementos disponibles.


##  Expresiones generadoras: 

  Son expresiones que generan secuencias de valores sobre la marcha utilizando la sintaxis similar a la comprensión de listas, pero con paréntesis en lugar de corchetes. Se utilizan para crear generadores de manera más concisa.

```python
gen = (x for x in range(1, 4))
for valor in gen:
    print(valor)  # Salida: 1, 2, 3

```

En ambos casos, los generadores producen valores sobre la marcha a medida que se solicitan, lo que puede ser más eficiente en términos de uso de memoria y puede permitir trabajar con conjuntos de datos grandes o infinitos. Los generadores son una característica poderosa de Python que facilita el manejo de flujos de datos de manera eficiente y elegante.



> figure

