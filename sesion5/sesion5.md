# diccionario

Un diccionario en Python, también conocido como "dict", es un tipo de dato que se utiliza para almacenar una colección de datos en forma de pares clave-valor.

El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.

Un diccionario en Python funciona de la misma manera que un diccionario bilingüe. Por ejemplo, se tiene la palabra en español "gato" y se necesita su equivalente en francés. Lo que se haría es buscar en el diccionario para encontrar la palabra "gato". Eventualmente la encontrarás, y sabrás que la palabra equivalente en francés es "chat".

En el mundo de Python, la palabra que se esta buscando se denomina **clave(key)**. La palabra que se obtiene del diccionario es denominada **valor**.

Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:

* Cada clave debe de ser única. No es posible tener una clave duplicada.
* Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante), o incluso una cadena.
* Un diccionario **no** es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores.
* La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
* Un diccionario es una herramienta de un solo sentido. Si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés más no viceversa.

## Características:

**Claves** únicas: Cada clave en un diccionario debe ser única.
**Valores**: Los valores pueden ser de cualquier tipo de dato en Python, como cadenas, números, listas o incluso otros diccionarios.
**Acceso rápido**: Los diccionarios proporcionan un acceso rápido a los valores mediante sus claves.
**Mutabilidad**: Los diccionarios son mutables, lo que significa que se pueden agregar, eliminar o modificar sus elementos después de su creación.

### Creación de un diccionario:

Se puede crear un diccionario usando dos métodos:

Notación literal:

```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

Función dict:

mi_diccionario = dict(nombre="Juan", edad=30, ciudad="Madrid")

```

### Acceso a los valores:

Se puede acceder a un valor en un diccionario usando la clave entre corchetes:

```python 


nombre = mi_diccionario["nombre"] # Almacena "Juan" en la variable nombre

``` 

* Agregar elementos:

Se pueden agregar nuevos elementos a un diccionario usando la clave como índice y el valor que se desea agregar:

```python 
mi_diccionario["telefono"] = "123456789"

```

* Eliminar elementos:

Se pueden eliminar elementos de un diccionario usando la función del:

```python 
del mi_diccionario["ciudad"]

```

* Iterar sobre un diccionario:

Se puede iterar sobre un diccionario usando un bucle for:

```python 

for clave in mi_diccionario:
  print(clave, mi_diccionario[clave])

```

## Diccionarios y listas:

Los diccionarios son una alternativa más eficiente que las listas para almacenar datos que se pueden identificar por una clave única.

Ejemplos de uso:

* Almacenar información de usuarios en un sistema.
* Almacenar datos de configuración de una aplicación.
* Almacenar datos de una encuesta.

```python 

#diccionario -> estructura compuesta de pares clave:valor

diccio1 = dict(a=1,b=2,c=3)
diccio2 = {
    "a": 1,
    "b":2,
    "c":3,
}

#se accede al valor a través de la clave
#print(diccio1["f"] if "f" in diccio1 else "No accesible")

print(diccio2["a"])
#KeyError -> cuando no existe la clave por la que queremos preguntar


diccio1["d"] = 20 #alta

print(diccio1)

#edicion
diccio1["a"] = 10 #update
print(diccio1)

#procesar por lotes
new_data = {
    'h': 90,
    'm': 100
}

diccio1.update(new_data)
print(diccio1)

for clave, valor in diccio1.items():
    print(f"Clave:{clave} Valor:{valor}")


x, y, z = diccio2.items()
print(x, y, z)

valores = list(diccio2.values())
print(valores)
print(type(valores))

claves = list(diccio2.keys())
print(claves)
print(type(claves))
```

## El método keys()

El método keys() en Python se utiliza en diccionarios para obtener una vista de las claves (keys en inglés) que están presentes en el diccionario. Este método devuelve un objeto de tipo 'dict_keys', que es una vista dinámica de las claves del diccionario. Estas vistas son iterables, lo que significa que puedes recorrerlas con un bucle 'for', también puedes convertirlas a una lista o realizar otras operaciones de conjunto sobre ellas.

Aquí hay un ejemplo de cómo usar el método keys():

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener una vista de las claves
claves = mi_diccionario.keys()

# Imprimir las claves
print(claves)  # Salida: dict_keys(['a', 'b', 'c'])

# Iterar sobre las claves
for clave in claves:
    print(clave)  # Salida: a, b, c

```
Puedes usar keys() para obtener todas las claves del diccionario y luego acceder a los valores correspondientes a esas claves utilizando la sintaxis de indexación habitual del diccionario mi_diccionario[clave].

## El método items() 

Devuelve una vista de tuplas que contienen pares clave-valor del diccionario. Esta vista de elementos (items) permite iterar sobre los pares clave-valor en el diccionario.

Aquí tienes un ejemplo de cómo usar el método items():

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener una vista de los pares clave-valor
items = mi_diccionario.items()

# Imprimir los pares clave-valor
print(items)  # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Iterar sobre los pares clave-valor
for clave, valor in items:
    print(clave, valor)  # Salida: a 1, b 2, c 3

```
El método items() es muy útil cuando necesitas recorrer tanto las **claves** como los **valores** de un diccionario simultáneamente.

## El método values() 

El método values() en Python se utiliza en diccionarios para obtener una vista de los **valores** que están presentes en el diccionario. Este método devuelve un objeto de tipo dict_values, que es una vista dinámica de los valores del diccionario. Al igual que con keys(), estas vistas son iterables y pueden ser recorridas con un bucle 'for', también puedes convertirlas a una lista o realizar otras operaciones de conjunto sobre ellas.

Aquí tienes un ejemplo de cómo usar el método values():

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener una vista de los valores
valores = mi_diccionario.values()

# Imprimir los valores
print(valores)  # Salida: dict_values([1, 2, 3])

# Iterar sobre los valores
for valor in valores:
    print(valor)  # Salida: 1, 2, 3

```
El método values() es útil cuando **solo** necesitas obtener los valores del diccionario y no te importan las claves asociadas.

## El método update() 

El método update() en Python se utiliza para actualizar un diccionario con elementos de otro diccionario u otro objeto iterable (como otro diccionario, una lista de tuplas, o incluso otro diccionario).

La sintaxis básica es la siguiente:

```python
diccionario.update([otros])

```
Donde otros puede ser otro diccionario, o un objeto iterable que contiene pares clave-valor (como una lista de tuplas).

Aquí tienes algunos ejemplos de cómo usar el método update():

* Actualizando con otro diccionario:

```python
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
diccionario1.update(diccionario2)
print(diccionario1)  # Salida: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

```

* Actualizando con una lista de tuplas:

```python
diccionario = {'a': 1, 'b': 2}
pares = [('c', 3), ('d', 4)]
diccionario.update(pares)
print(diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

```
* Actualizando con argumentos de palabra clave:

```python
diccionario = {'a': 1, 'b': 2}
diccionario.update(c=3, d=4)
print(diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

```
El método 'update()' añade elementos del argumento pasado al diccionario original. Si la clave ya existe en el diccionario original, el valor se actualiza; de lo contrario, se añade una nueva entrada al diccionario. Este método es útil para combinar varios diccionarios o agregar nuevos elementos a un diccionario existente. 

## El método count() 

El método count() en Python se utiliza para contar **cuántas veces** aparece un elemento específico en una secuencia, como una lista o una tupla. Este método se llama en una secuencia y toma un único argumento que representa el elemento que deseas contar.

Aquí tienes un ejemplo de cómo usar el método count() con una lista:

```python
mi_lista = [1, 2, 3, 1, 4, 1, 5]

# Contar cuántas veces aparece el número 1 en la lista
conteo = mi_lista.count(1)

print(conteo)  # Salida: 3

```
En este ejemplo, mi_lista.count(1) devuelve el número de veces que el elemento 1 aparece en la lista mi_lista, que es 3.

El método count() es útil cuando necesitas saber cuántas veces un elemento específico está presente en una secuencia.


## El método clear() 

El método clear() en Python se utiliza en estructuras de datos mutables, como diccionarios y conjuntos, para eliminar todos los elementos de la estructura, dejándola vacía.

Por ejemplo, si tienes un diccionario con algunos elementos y deseas eliminar todos esos elementos para dejar el diccionario vacío, puedes usar el método clear().

Aquí tienes un ejemplo de cómo usar clear() con un diccionario:

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

print(mi_diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3}

# Limpiar el diccionario
mi_diccionario.clear()

print(mi_diccionario)  # Salida: {}

```
Después de llamar a clear(), el diccionario se vacía y ya no contiene ningún elemento.

Es importante tener en cuenta que clear() modifica la estructura de datos original directamente y no devuelve ningún valor. Por lo tanto, no puedes asignar el resultado de clear() a una variable, ya que simplemente se vaciará el diccionario y la variable se quedará como None.


## del

Además del método clear(), que elimina todos los elementos de un diccionario dejándolo vacío, también tenemos la instrucción del en Python, que se utiliza para eliminar elementos específicos de un diccionario o variables en general.

La sintaxis básica de del para eliminar un elemento de un diccionario es:

```python
del mi_diccionario['clave']

```
Esto eliminará la clave especificada junto con su valor asociado del diccionario.

Por ejemplo:

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
del mi_diccionario['b']
print(mi_diccionario)  # Salida: {'a': 1, 'c': 3}

```
En este ejemplo, se elimina la clave 'b' junto con su valor asociado del diccionario.

También puedes usar del para eliminar completamente el diccionario, similar a clear(), pero 'del' también permite eliminar variables en general, no solo elementos de diccionarios. 

Por ejemplo:

```python
del mi_diccionario

```
Esto eliminará completamente el diccionario mi_diccionario de la memoria. Después de usar del, cualquier intento de acceder a mi_diccionario generará un error NameError indicando que la variable ya no existe.

```python
del mi_diccionario

```

## El método copy() 

Por otro lado, el método 'copy()' se utiliza para crear una copia superficial de un diccionario en Python. Esto significa que se crea un nuevo diccionario con los mismos pares clave-valor que el diccionario original, pero si los valores son objetos mutables, ambos diccionarios apuntarán a los mismos objetos. 

Aquí tienes un ejemplo:

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
copia_diccionario = mi_diccionario.copy()

print(copia_diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3}

```
En este caso, copia_diccionario es una copia superficial de mi_diccionario, ambos contienen los mismos elementos, pero si se modifican los valores mutables en uno, el otro no se verá afectado.

## pop() vs el método popitem ()

en Python, además de "pop()", existe el método "popitem()" que también se utiliza para eliminar elementos de un diccionario. 
Sin embargo, hay diferencias importantes entre pop() y popitem().

Aquí hay una comparación entre pop() y popitem():

### pop():

Elimina un elemento del diccionario basado en la clave **especificada**.
Toma la clave como argumento.
Devuelve el valor asociado a esa clave.
Específicamente elimina el elemento con la clave dada.

### popitem():

**Elimina y devuelve** un par "clave-valor" arbitrario (último insertado) del diccionario.
No toma argumentos.
No se puede predecir qué elemento será eliminado, ya que el método selecciona arbitrariamente un par clave-valor para eliminar.

Es útil cuando se quiere eliminar elementos en un orden no especificado, 
por ejemplo, para procesar elementos en un diccionario en un orden aleatorio o pseudoaleatorio.

Aquí tienes un ejemplo que muestra cómo funcionan pop() y popitem():

```python
#  Definir un diccionario

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Utilizar pop() para eliminar el elemento con la clave 'b'

valor_b = mi_diccionario.pop('b')
print("Valor de 'b' eliminado:", valor_b)
print("Diccionario actualizado:", mi_diccionario)

# Utilizar popitem() para eliminar un par clave-valor arbitrario

par_clave_valor = mi_diccionario.popitem()
print("Par clave-valor eliminado:", par_clave_valor)
print("Diccionario actualizado:", mi_diccionario)
```
Es importante tener en cuenta que popitem() se utiliza generalmente cuando se desea **eliminar** elementos de un diccionario sin preocuparse por el orden en que fueron insertados, 

mientras que pop() se utiliza cuando se desea eliminar un elemento **específico** basado en su clave.

```python

#eliminar items
item_eliminado = diccio2.pop("a")
print(diccio2, item_eliminado)

item_eliminado = diccio2.popitem()
print(diccio2)

diccio2.clear()
print(diccio2)

del diccio2
#print(diccio2)

#obtencion o lectura
valor_item = diccio1.get("a")
print(valor_item)

valor_item = diccio1.get("v", -999)
print(valor_item)


mi_diccionario = {
    'a': 100,
    'b': 200,
    'c': 300
}

papelera = dict() #vacia
par_eliminado = mi_diccionario.popitem() # tupla
papelera.update(dict([par_eliminado]))
print(papelera)



papelera.update(dict([diccio1.popitem()]))
nuevo_diccionario = dict([("a",6), ("c", 4)]) #diccio1.items() // ("a",([1,2,3])) -> dupla
papelera.update(nuevo_diccionario)

print(papelera)

```
# Exceptions

Las excepciones son un mecanismo para **controlar los errores** en Python.

Cuando se produce un error en un programa, se lanza una excepción. 
La excepción contiene información sobre el error, como el tipo de error y la ubicación donde se produjo.

## El programa puede manejar la excepción de diferentes maneras:

**Capturar la excepción**: Se puede usar un bloque try-except para capturar la excepción y realizar una acción específica.
**Propagar la excepción**: Se puede permitir que la excepción se propague a una función que la llame.
**Ignorar la excepción**: En algunos casos, se puede ignorar la excepción.

## Ventajas de usar excepciones:

**Mejora la robustez del programa:**    
El programa puede continuar ejecutándose incluso si se produce un error.

**Facilita la depuración:**    
 Las excepciones proporcionan información útil sobre los errores.

**Mejora la legibilidad del código:**    
 El código es más fácil de leer y entender.

## Tipos de excepciones:

**Excepciones estándar:**     
Son excepciones que forman parte de la instalación estándar de Python.    

**Excepciones personalizadas:**    
 Son excepciones que se crean por el usuario.


## Algunas excepciones útiles 

### ZeroDivisionError

ZeroDivisionError es una excepción específica en Python que se produce cuando intentas **dividir** un número por cero. En Python (y en la mayoría de los lenguajes de programación), la división por cero no está definida y, por lo tanto, produce un error. Esta excepción se produce cuando el denominador en una operación de división es cero.

Aquí tienes un ejemplo de cómo se produce ZeroDivisionError:

```python
resultado = 10 / 0

```
Al ejecutar este código, Python generará un **ZeroDivisionError** porque estás intentando dividir 10 por cero, lo cual es una operación indefinida en matemáticas.

Cuando se produce una excepción ZeroDivisionError, Python detiene la ejecución del programa y muestra un mensaje de error en la consola indicando que ocurrió una división por cero. Es importante manejar adecuadamente esta excepción en tu código para evitar que el programa se bloquee inesperadamente. Puedes hacer esto usando bloques try y except para capturar y manejar la excepción, o mostrando un mensaje de error personalizado al usuario.

### ValueError

**ValueError** es una excepción en Python que se genera cuando una función recibe un argumento con un tipo correcto, pero un valor incorrecto. Esto puede ocurrir cuando se llama a una función con un argumento que está fuera del rango esperado o que no puede ser interpretado de la forma en que se espera.

Aquí tienes algunos ejemplos comunes de situaciones que pueden generar ValueError:

Convertir una cadena en un número, pero la cadena no representa un número válido:

```python

```

```python

```

### TypeError

```python

```

### AttributeError

### SyntaxError

```python
diccionario  = dict(a=1, b=2)

try:
    #resultado = 14 / 0
    #print(resultado)
    data = diccionario["c"]

except (ZeroDivisionError, TypeError):
    print("El error es de tipo numerico")
except KeyError as kex:
    print(f"Clave inexistente:{kex}")
except Exception as ex:
    print(f"Ha habido un error: {ex}")


def convertir_a_entero(data:str) -> int:
    resultado = None
    try:
        resultado = int(data)
    except ValueError:
        pass
    
    return resultado

resultado_entero = convertir_a_entero("Hola")

diccionario = {
    "111H": "Juan",
    "222H": "Paloma"
}

try:
    #del diccionario
    diccionario["111H"] = "Miguel"
    print(diccionario)
except NameError:
    print("Diccionario no existente")
except Exception:
    print("Error general")
else:
    print("Se ha completado satisfactoriamente la operacion")
finally:
    print("Operacion terminada")

```













