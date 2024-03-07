[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
# Tuplas

Las tuplas en Python son un tipo de dato inmutable que se utiliza para almacenar una colección ordenada de elementos. 
Son similares a las listas, pero **no** se pueden modificar una vez creadas.

Cómo crear una tupla:

Las tuplas se crean entre paréntesis, separados por comas.
Las tuplas utilizan paréntesis, mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando los valores por comas.

```python

# Tupla con un solo elemento
mi_tupla = ("Hola",)

# Tupla con varios elementos
mi_tupla = ("Hola", "mundo", 123)

```

## Tipos de mutabilidad

### Datos Inmutables:

* Los datos inmutables son aquellos cuyo valor no puede cambiar después de que han sido creados.
* Una vez que un objeto inmutable se ha creado, no se puede modificar su contenido.
* Cualquier operación que parezca modificar un dato inmutable en realidad crea un nuevo objeto con el valor modificado.


#### Tipos de datos inmutables:

Los objetos de estos tipos no se pueden cambiar después de su creación. Cualquier operación que parezca modificar el objeto en realidad crea un nuevo objeto.
Ejemplos de tipos de datos inmutables en Python incluyen:

* Números enteros (int)
* Números flotantes (float)
* Cadenas (str)
* Tuplas (tuple)
* Frozensets (frozenset)

### Datos Mutables:

* Los datos mutables son aquellos cuyo valor puede cambiar después de que han sido creados.
* Estos objetos pueden ser modificados directamente después de su creación.
* Las modificaciones en un objeto mutable afectan directamente al objeto original, sin necesidad de crear un nuevo objeto.


#### Tipos de datos mutables:

Los objetos de estos tipos pueden ser modificados después de su creación. Esto significa que su estado interno puede ser alterado sin necesidad de crear un nuevo objeto.
Ejemplos de tipos de datos mutables en Python incluyen:

* Listas (list)
* Diccionarios (dict)
* Conjuntos (set)

Es importante tener en cuenta la mutabilidad de los objetos cuando se trabaja con ellos en Python, ya que puede afectar el comportamiento del programa, especialmente cuando se pasan objetos como argumentos a funciones o cuando se realizan operaciones de asignación. Los objetos mutables pueden ser modificados por múltiples partes del código, lo que puede llevar a efectos secundarios no deseados si no se manejan correctamente. Por otro lado, los objetos inmutables son más seguros en este sentido, ya que su estado no puede ser alterado una vez que han sido creados.



Es importante entender la diferencia entre datos inmutables y mutables, ya que afecta la forma en que se manejan y modifican los objetos en un programa. El uso adecuado de datos inmutables y mutables puede mejorar la eficiencia y la claridad del código, y también puede ayudar a evitar errores comunes relacionados con el estado de los objetos.

## Acceso a los elementos de una tupla:

Se puede acceder a los elementos de una tupla utilizando su índice.

```python

mi_tupla = ("Hola", "mundo", 123)

# Acceder al primer elemento
primer_elemento = mi_tupla[0]

# Acceder al segundo elemento
segundo_elemento = mi_tupla[1]

# Acceder al tercer elemento
tercer_elemento = mi_tupla[2]

```

## Operaciones con tuplas:

Las tuplas se pueden **concatenar**, **sumar** y **multiplicar**.

## Cuándo usar tuplas:

Las tuplas se pueden usar en lugar de listas cuando se necesita almacenar una colección de datos que no necesita ser modificada.

## Ventajas de usar tuplas:

**Inmutabilidad**:    
Las tuplas no se pueden modificar una vez creadas, lo que las hace más seguras y confiables.    

**Eficiencia**:    
Las tuplas son más eficientes que las listas en términos de memoria y velocidad.

## Desventajas de usar tuplas:

**Inmutabilidad**:     
Las tuplas no se pueden modificar una vez creadas, lo que puede ser un inconveniente en algunos casos.

En resumen, las tuplas son un tipo de dato inmutable que se utiliza para almacenar una colección ordenada de elementos. 
Son una buena opción cuando se necesita almacenar una colección de datos que no necesita ser modificada.

```python
i_tupla1 = ("Hola", "mundo")
mi_tupla2 = ("!", 123)

# Concatenación
mi_tupla_concatenada = mi_tupla1 + mi_tupla2

# Suma
mi_tupla_suma = mi_tupla1 + mi_tupla2

# Multiplicación
mi_tupla_multiplicada = mi_tupla1 * 3


#tupla: coleccion da datos INMUTABLE

tupla1 = (1,2,3)

tupla2 = tupla1[:]
print(tupla2)

#print(id(tupla1))
#print(id(tupla2))


tupla3 = tupla2[0:2]
print(id(tupla3))
print(id(tupla2))

for item in tupla2:
    print(item)

tupla5 = 1,2,3,4,5

#print(type(tupla5))



def procesar_data() -> tuple:
    return 1,2,3

n = 1,
print(type(n))

lista_tuplas = [(1,2),(4,6),('Juan', 9), (True, False)]

```

# set()

El término "set" en Python se refiere a un tipo de datos incorporado que representa una colección desordenada y sin elementos duplicados. En términos matemáticos, un conjunto es una colección de elementos únicos y no ordenados. En Python, los sets se definen utilizando llaves {} o la función set().

Aquí hay un ejemplo básico de cómo crear un set en Python:

```python
#Crear un set utilizando llaves
mi_set = {1, 2, 3, 4, 5}

#Crear un set utilizando la función set()
mi_otro_set = set([4, 5, 6, 7, 8])

print(mi_set)       # Output: {1, 2, 3, 4, 5}
print(mi_otro_set)  # Output: {4, 5, 6, 7, 8}

```

Algunas características importantes de los sets en Python incluyen:

**Elementos únicos**:    
Los sets no contienen elementos duplicados. Si intentas agregar un elemento que ya está presente en el set, simplemente se ignorará.

```python
mi_set = {1, 2, 3, 4, 5}
mi_set.add(6)
mi_set.add(2)  # Este elemento ya existe, por lo que se ignora
print(mi_set)  # Output: {1, 2, 3, 4, 5, 6}

```

**Desordenados**:     
Los sets no mantienen ningún orden específico de los elementos. Cuando imprimes un set, los elementos pueden aparecer en un orden diferente al que fueron agregados.

```python
mi_set = {3, 1, 4, 2, 5}
print(mi_set)  # Output: {1, 2, 3, 4, 5} (orden arbitrario)

```

**Operaciones de conjuntos**:    
Los sets admiten operaciones comunes de conjuntos como unión, intersección, diferencia y diferencia simétrica.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # Output: {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # Output: {3, 4}
print(set1.difference(set2))   # Output: {1, 2}
print(set2.difference(set1))   # Output: {5, 6}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}


```

Los sets son útiles cuando necesitas almacenar una colección de elementos únicos y no te importa el orden en que se almacenan. Se utilizan comúnmente para eliminar duplicados de una lista, verificar la pertenencia de elementos y realizar operaciones de conjuntos.

# Funcion tuple()