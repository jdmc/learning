# Comprehension list

Las comprensiones de listas son una herramienta poderosa en Python que te permite crear listas de forma concisa y eficiente. 
Son una alternativa a los bucles for tradicionales para crear listas.

Sintaxis:
```python
nueva_lista = [expresion for elemento in iterable if condicion]
```

Explicación:
[]: Indica que estamos creando una lista.
nueva_lista: Es la variable que almacenará la nueva lista.
expresion: Es la expresión que se evalúa para cada elemento del iterable.
iterable: Es la lista u otro tipo de secuencia sobre la que se itera.
condicion: Es una expresión booleana opcional que se utiliza para filtrar los elementos del iterable.

Ejemplo:
```python 
numeros = [1, 2, 3, 4, 5]

cuadrados = [numero**2 for numero in numeros]

print(cuadrados) # Imprime [1, 4, 9, 16, 25]
```

En este ejemplo, la comprensión de lista crea una nueva lista llamada pares que solo contiene los números pares de la lista numeros.
La comprensión de listas crea una nueva lista cuadrados que contiene los cuadrados de los elementos de la lista numeros. 
La expresión numero**2 se evalúa para cada elemento de numeros y el resultado se agrega a la nueva lista.


En resumen, las comprensiones de listas son una herramienta poderosa en Python que te permite crear listas de forma concisa, eficiente y legible.

```python
[expresión for elemento in iterable if condición]
```
### Explicación:

expresión: La expresión que se evalúa para cada elemento del iterable.
for elemento in iterable: La iteración sobre el iterable.
if condición: La condición que se evalúa para cada elemento del iterable. 
Solo se incluyen los elementos que cumplen la condición.

### Ventajas de las comprensiones de listas:

**Concisión**: Permiten crear listas de forma más concisa que con bucles for.    
**Eficiencia**: Son más eficientes que los bucles for en algunos casos.    
**Legibilidad**: Pueden mejorar la legibilidad del código, especialmente cuando se usan expresiones simples.    

### Desventajas de las comprensiones de listas:

**Dificultad de depuración:**    
Puede ser más difícil depurar el código que usa comprensiones de listas.    
**Falta de nombre:**     
La expresión dentro de la comprensión de lista no tiene nombre, lo que puede dificultar la comprensión del propósito del código.

### Cuándo usar comprensiones de listas:

* Cuando necesitas crear una lista a partir de otra lista.
* Cuando la lógica para crear la lista es simple.
* Cuando quieres mejorar la legibilidad del código. 

En resumen, las comprensiones de listas son una herramienta poderosa para crear nuevas listas a partir de listas existentes de forma concisa y eficiente.

```python

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

# Comprension Lista

 ### Inicializamos una lista vacía para almacenar los valores convertidos a cadenas de texto
valores_convertidos = []

# Iteramos sobre cada campo en la lista 'campos'
for campo in campos:
    # Accedemos al valor asociado con el campo en el diccionario 'usuario'
    valor = usuario[campo]
    # Convertimos ese valor a una cadena de texto y lo agregamos a la lista 'valores_convertidos'
    valor_convertido = str(valor)
    valores_convertidos.append(valor_convertido)

# Unimos los valores convertidos en una sola cadena, separados por '---'
fila = '---'.join(valores_convertidos)

```
### Explicación:

Inicializamos una lista vacía llamada valores_convertidos para almacenar los valores convertidos a cadenas de texto.
Iteramos sobre cada campo en la lista campos.
Para cada campo, accedemos al valor asociado con ese campo en el diccionario usuario.
Convertimos ese valor a una cadena de texto utilizando str() y lo almacenamos en una variable llamada valor_convertido.
Agregamos el valor convertido a la lista valores_convertidos.
Una vez que hemos iterado sobre todos los campos y convertido sus valores, 
usamos el método join() para unir todos los valores convertidos en una sola cadena, separados por '---'. 
Esto nos da la fila que queremos escribir en el archivo CSV.
Dividir el proceso en pasos más pequeños y claros puede hacer que sea más fácil de entender, 
especialmente si estás teniendo dificultades con la comprensión de lista en una sola línea.

```python

  fila = '---'.join([str(usuario[campo]) for campo in campos])

[...] for ... in ...]: 
es una comprensión de lista, una forma compacta y poderosa de crear listas en Python. 

El bucle for en Python se utiliza para iterar sobre una secuencia de elementos, como una lista, una tupla, un diccionario, etc. 
Básicamente, itera sobre cada elemento de la secuencia y ejecuta un bloque de código para cada elemento.
En Python, cuando utilizas un bucle for, suele ser una buena práctica utilizar una variable que describa de manera clara el tipo de elementos que se están iterando. 
Esto hace que el código sea más legible y comprensible.

nombres = ["Juan", "María", "Pedro"]

for nombre in nombres:


Simplificado, podríamos decir que el bucle for en Python hace lo siguiente:

Para cada elemento en la secuencia:
Toma un elemento de la secuencia.
Ejecuta un bloque de código para ese elemento.

El primer paso es entender la estructura básica de una comprensión de lista. 

Comienza con [...], 
que indica que estamos creando una lista. 

Luego viene for ... in ..., 
que indica que estamos iterando sobre algo (una secuencia, como una lista) 
y generando elementos en nuestra nueva lista para cada elemento en esa secuencia.

ahora:
    
str(usuario[campo]):
Esto es lo que se llama una "llamada a método" en Python. str() es una función que convierte su argumento en una cadena de texto. 
En este caso, estamos convirtiendo usuario[campo] (el valor asociado a la clave campo en el diccionario usuario) en una cadena de texto.
        
Juntando todo:

Ahora que entendemos cada parte, podemos ver que [str(usuario[campo]) for campo in campos] significa que:
estamos creando una lista donde cada elemento es el valor asociado a la clave campo en el diccionario usuario, 
convertido a una cadena de texto. 
Lo estamos haciendo para cada campo en la lista campos.

Aplicándolo al código:

Para escribir este tipo de código, primero necesitas entender qué quieres lograr. 

Aquí, queremos obtener una lista de los valores de ciertos campos del diccionario usuario como cadenas de texto.
Luego, necesitas saber cómo acceder a esos valores en un diccionario. 
En Python, usuario[campo] accede al valor asociado con la clave campo en el diccionario usuario.
Finalmente, puedes usar una comprensión de lista para iterar sobre los campos deseados (campo in campos) y obtener los valores asociados (usuario[campo]), convirtiéndolos a cadenas de texto (str(usuario[campo])).

Con estos pasos, puedes entender y escribir comprensiones de lista y otros tipos de código en Python. 
Es una habilidad muy útil que te permite escribir código más conciso y legible.

´´´