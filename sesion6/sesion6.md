[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
# ¿Qué es lambda en Python?
Programación funcional
En Python, lambda se refiere a una función anónima. 
Estas funciones se definen en una sola línea y no tienen nombre. 
Se utilizan para realizar tareas simples de forma concisa y eficiente.

### Cuándo usar funciones lambda:

* Cuando necesitas una función simple para una tarea específica.
* Cuando necesitas pasar una función como argumento a otra función.
* Cuando quieres mejorar la legibilidad del código.

### Ventajas de usar funciones lambda:

**Concisión**: Permiten definir funciones pequeñas en una sola línea.    
**Eficiencia**: Son más eficientes que las funciones normales, ya que no tienen nombre ni código adicional.    
**Legibilidad**: Pueden mejorar la legibilidad del código, especialmente cuando se usan dentro de otras funciones o expresiones.    

### Desventajas de usar funciones lambda:

**Dificultad de depuración**: Puede ser más difícil depurar las funciones lambda que las funciones normales.    
**Falta de nombre**: No tener nombre puede dificultar la comprensión del propósito de la función.    

Ejemplo:

```python
def sumar (x: int , y: int) -> int:
    return x + y

#lambda = funciones anonimas

sumar_lambda = lambda x, y : x + y

r1 = sumar_lambda (10,3)
r2 = sumar (10,3)

print(r1 == r2)

def mayor_siete(alumno: tuple) -> bool: #hacer una funcion
    nota = alumno[1]
    return nota > 7.0

def sumar_medio_punto (alumno: tuple) -> tuple:
    alumno_modificado = (alumno[0], alumno [1] + 0.5)
    return alumno_modificado

alumnos = [('maite', 6.0), ('alicia', 8.2), ('luis', 7.5), ('juan', 7.0)]
```
# MAP
map dentro de una función lambda en Python
map es una función integrada en Python que se utiliza para aplicar una función a cada elemento de un iterable (una lista, una cadena, etc.) y devolver un nuevo iterable con los resultados. 
La función map toma dos argumentos:

El iterable al que se desea aplicar la función.
La función que se desea aplicar a cada elemento del iterable.
En el contexto de una función lambda, la función map se puede usar para aplicar una expresión simple a cada elemento de un iterable.
La expresión se define dentro de la función lambda y se evalúa para cada elemento del iterable.

## Ventajas de usar map dentro de una función lambda:

**Concisión**: Permite aplicar una función a cada elemento de un iterable en una sola línea.    
**Eficiencia**: Es más eficiente que usar un bucle for para aplicar una función a cada elemento.    
**Legibilidad**: Puede mejorar la legibilidad del código, especialmente cuando se usan expresiones simples.    

## Desventajas de usar map dentro de una función lambda:
**Dificultad de depuración**: Puede ser más difícil depurar el código que usa map dentro de una función lambda.    
**Falta de nombre**: La expresión dentro de la función lambda no tiene nombre, lo que puede dificultar la comprensión del propósito del código.    

## Cuándo usar map dentro de una función lambda:
* Cuando necesitas aplicar una función simple a cada elemento de un iterable.
* Cuando quieres mejorar la legibilidad del código.

Ejemplos de uso de map dentro de una función lambda:

```python
#alumnos_nota_corregida = list(map(lambda alumno: (alumno[0],alumno[1]+0.5) , alumnos))
alumnos_nota_corregida = list(map(sumar_medio_punto, alumnos))
print(type(alumnos_nota_corregida))
print(f"Map: {alumnos_nota_corregida}")
```
# FILTER
filter dentro de una función lambda en Python
filter es una función integrada en Python que se utiliza para filtrar elementos de un iterable (una lista, una cadena, etc.) en función de una condición. 

La función filter toma dos argumentos:

El iterable que se desea filtrar.
Una función que se utiliza para determinar si un elemento debe ser incluido o no en el resultado.
En el contexto de una función lambda, la función filter se puede usar para filtrar elementos de un iterable en función de una expresión simple. 
La expresión se define dentro de la función lambda y se evalúa para cada elemento del iterable. Si la expresión devuelve True, el elemento se incluye en el resultado. Si la expresión devuelve False, el elemento se excluye del resultado.

 ### Ventajas de usar filter dentro de una función lambda:

**Concisión**: Permite filtrar elementos de un iterable en una sola línea.    
**Eficiencia**: Es más eficiente que usar un bucle for para filtrar elementos.    
**Legibilidad**: Puede mejorar la legibilidad del código, especialmente cuando se usan expresiones simples.    


### Desventajas de usar filter dentro de una función lambda:
**Dificultad de depuración**: Puede ser más difícil depurar el código que usa filter dentro de una función lambda.    
**Falta de nombre**: La expresión dentro de la función lambda no tiene nombre, lo que puede dificultar la comprensión del propósito del código.    

### Cuándo usar filter dentro de una función lambda:
* Cuando necesitas filtrar elementos de un iterable en función de una expresión simple.
* Cuando quieres mejorar la legibilidad del código.

```python
#alumnos_mas_siete = list(filter(lambda alumno: alumno [1] > 7.0, alumnos)) # que tienes que hacer(lambda), donde lo pillas (alumnos)
alumnos_mas_siete = list(filter(lambda alumno: mayor_siete(alumno), alumnos)) # haciendo uso de una funcion >
"def mayor siete"
print(type(alumnos_mas_siete))
print(f"Filter: {alumnos_mas_siete}")

```

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 