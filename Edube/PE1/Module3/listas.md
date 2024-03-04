# ¿Por qué necesitamos listas?
Puede suceder que tengas que leer, almacenar, procesar y, finalmente, imprimir docenas, quizás cientos, tal vez incluso miles de números. ¿Entonces qué? ¿Necesitas crear una variable separada para cada valor? 

Digamos lo mismo utilizando una terminología adecuada: numeros es una lista que consta de cinco valores, todos ellos números. También podemos decir que esta sentencia crea una lista de longitud igual a cinco (ya que contiene cinco elementos).

Los elementos dentro de una lista pueden tener diferentes tipos. Algunos de ellos pueden ser enteros, otros son flotantes y otros pueden ser listas.

Python ha adoptado una convención que indica que los elementos de una lista están siempre numerados desde cero. Esto significa que el elemento almacenado al principio de la lista tendrá el número cero. Como hay cinco elementos en nuestra lista, al último de ellos se le asigna el número cuatro. No olvides esto.

# Indexando Listas

Indexar listas se refiere al proceso de acceder a elementos dentro de una lista utilizando su posición o índice. En Python, la indexación de listas comienza en 0, lo que significa que el primer elemento de una lista tiene un índice de 0, el segundo elemento tiene un índice de 1, y así sucesivamente.

```python
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
```


El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice, mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.

También se admite la indexación negativa, lo que te permite acceder a elementos desde el final de la lista. Por ejemplo, -1 se refiere al último elemento, -2 se refiere al penúltimo elemento, y así sucesivamente.

```python
mi_lista = ['manzana', 'banana', 'naranja', 'uva', 'kiwi']

print(mi_lista[-1])  # Salida: 'kiwi'
print(mi_lista[-2])  # Salida: 'uva'

```

También puedes usar la indexación para modificar elementos en una lista o para extraer porciones de la lista utilizando el "slicing". 

Por ejemplo:

```python
mi_lista = ['manzana', 'banana', 'naranja', 'uva', 'kiwi']
# Modificar elementos usando la indexación
mi_lista[1] = 'pera'
print(mi_lista)  # Salida: ['manzana', 'pera', 'naranja', 'uva', 'kiwi']

# Slicing de listas
print(mi_lista[1:4])  # Salida: ['pera', 'naranja', 'uva']
print(mi_lista[:3])   # Salida: ['manzana', 'pera', 'naranja']
print(mi_lista[2:])   # Salida: ['naranja', 'uva', 'kiwi']

```

### Slicing

El "slicing" en Python se refiere a la técnica de extraer partes o porciones de una lista, cadena u otro tipo de secuencia utilizando la notación de corchetes []. Permite seleccionar un subconjunto de elementos basado en su posición o índice dentro de la secuencia.

La sintaxis básica del slicing es [inicio:final:paso], donde:

* inicio: Índice donde comienza el slicing (inclusive).
* final: Índice donde termina el slicing (exclusivo).
* paso: Paso o incremento entre elementos seleccionados (opcional).
Si no se especifica inicio, por defecto se toma el primer elemento de la secuencia. Si no se especifica final, se toma hasta el final de la secuencia. Si no se especifica paso, se toma un paso de 1.

Aquí tienes algunos ejemplos de slicing en listas:

```python
mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Slicing básico
print(mi_lista[2:5])    # Salida: ['c', 'd', 'e']

# Si no se especifica 'final', toma hasta el final de la lista
print(mi_lista[5:])     # Salida: ['f', 'g', 'h', 'i', 'j']

# Si no se especifica 'inicio', toma desde el principio de la lista
print(mi_lista[:3])     # Salida: ['a', 'b', 'c']

# Slicing con paso
print(mi_lista[1:8:2])  # Salida: ['b', 'd', 'f', 'h']

```
