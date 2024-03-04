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

* inicio: Índice donde comienza el slicing (**inclusive**).
* final: Índice donde termina el slicing (**exclusivo**).
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

## len

La función len() en Python se utiliza para obtener la longitud o el tamaño de un objeto iterable, como una lista, una cadena, una tupla, un diccionario, etc. Devuelve el número de elementos en el objeto iterable.

Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).
La función toma el nombre de la lista como un argumento y devuelve el número de elementos almacenados actualmente dentro de la lista (en otras palabras, la longitud de la lista).

```python
# Longitud de una lista
mi_lista = [1, 2, 3, 4, 5]
print(len(mi_lista))  # Salida: 5

# Longitud de una cadena
mi_cadena = "Hola, mundo!"
print(len(mi_cadena))  # Salida: 12 (incluyendo los espacios y la coma)

# Longitud de una tupla
mi_tupla = (10, 20, 30, 40, 50)
print(len(mi_tupla))  # Salida: 5

# Longitud de un diccionario (número de pares clave-valor)
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
print(len(mi_diccionario))  # Salida: 3

```

## Eliminando elementos de una lista

Cualquier elemento de la lista puede ser eliminado en cualquier momento, esto se hace con una instrucción llamada del (eliminar). Nota: es una instrucción, no una función.

Tienes que apuntar al elemento que quieres eliminar, desaparecerá de la lista y la longitud de la lista se reducirá en uno.

1. Eliminación por índice:     
  Puedes eliminar un elemento de una lista utilizando su índice con la instrucción del o el método pop().

```python
# Eliminar elemento por índice utilizando del
mi_lista = [1, 2, 3, 4, 5]
del mi_lista[2]  # Elimina el elemento en el índice 2 (el tercer elemento)
print(mi_lista)  # Salida: [1, 2, 4, 5]

# Eliminar elemento por índice utilizando pop()
elemento_eliminado = mi_lista.pop(0)  # Elimina el primer elemento y lo devuelve
print(elemento_eliminado)  # Salida: 1
print(mi_lista)  # Salida: [2, 4, 5]

```

2. Eliminación por valor:    
  Puedes eliminar un elemento de una lista por su valor utilizando el método remove()

```python
# Eliminar elemento por valor utilizando remove()
mi_lista = ['a', 'b', 'c', 'd', 'e']
mi_lista.remove('c')  # Elimina el elemento 'c'
print(mi_lista)  # Salida: ['a', 'b', 'd', 'e']

```

3. Eliminación por criterio:    
  Si deseas eliminar elementos que cumplan ciertas condiciones, puedes utilizar una comprensión de lista o un bucle con la instrucción del.

```python
# Eliminar elementos mayores que 5 utilizando una comprensión de lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_lista = [x for x in mi_lista if x <= 5]
print(mi_lista)  # Salida: [1, 2, 3, 4, 5]

# Eliminar elementos que cumplan ciertas condiciones utilizando un bucle
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(mi_lista):
    if mi_lista[i] > 5:
        del mi_lista[i]
    else:
        i += 1
print(mi_lista)  # Salida: [1, 2, 3, 4, 5]

```

# Funciones frente a métodos

En Python, tanto las funciones como los métodos son bloques de código reutilizables que realizan una tarea específica. Sin embargo, hay diferencias fundamentales entre ellos:

1. Funciones:

* Son bloques de código independientes que toman cero o más argumentos como entrada y pueden devolver un resultado como salida.
* Se definen utilizando la palabra clave def seguida del nombre de la función y, opcionalmente, los parámetros entre paréntesis.
* Pueden ser invocadas desde cualquier parte del código donde estén visibles.
* No están asociadas con ningún objeto o clase en particular.

Ejemplo de definición y llamada de una función:

```python
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Salida: 7

```

2. Métodos:

* Son funciones definidas dentro de una clase y están asociadas con objetos de esa clase.
* Operan en los datos específicos de un objeto y pueden modificar el estado interno del objeto.
* Se definen dentro de la definición de una clase utilizando la palabra clave def.
* Son invocados en objetos específicos utilizando la notación de punto (objeto.metodo()).

Ejemplo de definición y llamada de un método:

```python
class Calculadora:
    def suma(self, a, b):
        return a + b

mi_calculadora = Calculadora()  # Crear un objeto de la clase Calculadora
resultado = mi_calculadora.suma(3, 4)
print(resultado)  # Salida: 7

```

En resumen, las funciones son bloques de código independientes que realizan una tarea general, mientras que los métodos son funciones asociadas con objetos específicos y pueden operar en los datos internos de esos objetos.

# Agregando elementos a una lista: append() e insert()

Agregando elementos a una lista en Python es una tarea común y hay dos métodos principales que puedes usar para hacerlo: 
**append()** e **insert()**.

## append()

* El método append() se utiliza para agregar un elemento al final de una lista.
* No necesitas especificar la posición donde deseas agregar el elemento; se añade automáticamente al final.
* Es útil cuando solo necesitas agregar elementos al final de la lista sin preocuparte por su posición exacta.

Ejemplo de uso de append():

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Salida: [1, 2, 3, 4]

```

## insert()

* El método insert() te permite agregar un elemento en una posición específica de la lista.
* Debes especificar la posición (índice) donde deseas insertar el elemento, así como el propio elemento.
* Después de la inserción, los elementos existentes se desplazan hacia la derecha para hacer espacio para el nuevo elemento.

Ejemplo de uso de insert():

```python
lista = [1, 2, 3]
lista.insert(1, 'a')
print(lista)  # Salida: [1, 'a', 2, 3]

```