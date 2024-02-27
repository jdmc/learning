# Tuplas

Las tuplas en Python son un tipo de dato inmutable que se utiliza para almacenar una colección ordenada de elementos. 
Son similares a las listas, pero no se pueden modificar una vez creadas.

Cómo crear una tupla:

Las tuplas se crean entre paréntesis, separados por comas.

```python

# Tupla con un solo elemento
mi_tupla = ("Hola",)

# Tupla con varios elementos
mi_tupla = ("Hola", "mundo", 123)

```

** Acceso a los elementos de una tupla:

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

´´´python
# Crear un set utilizando llaves
mi_set = {1, 2, 3, 4, 5}

# Crear un set utilizando la función set()
mi_otro_set = set([4, 5, 6, 7, 8])

print(mi_set)       # Output: {1, 2, 3, 4, 5}
print(mi_otro_set)  # Output: {4, 5, 6, 7, 8}

´´´
Algunas características importantes de los sets en Python incluyen:

**Elementos únicos**:    
Los sets no contienen elementos duplicados. Si intentas agregar un elemento que ya está presente en el set, simplemente se ignorará.

```python
mi_set = {1, 2, 3, 4, 5}
mi_set.add(6)
mi_set.add(2)  # Este elemento ya existe, por lo que se ignora
print(mi_set)  # Output: {1, 2, 3, 4, 5, 6}

```