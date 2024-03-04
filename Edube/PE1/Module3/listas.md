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

También puedes usar la indexación para modificar elementos en una lista o para extraer porciones de la lista utilizando el "slicing". Por ejemplo: