# Operadores 

[Operadores 1](Edube\Module2\operadores_y_expresiones.md)  

## 2.Comparación: Se utilizan para comparar dos valores y devolver un resultado booleano (True o False).

\== (igual a)  
\!= (diferente de) >>  (no es igual a)  
\< (menor que)  
\> (mayor que)  
\<= (menor o igual que)  
\>= (mayor o igual que)  

# Instrucción condicional  

Una instrucción condicional, en programación, es una estructura que permite ejecutar diferentes fragmentos de código basándose en una condición.  
Básicamente, se evalúa una expresión booleana y, dependiendo de si esa expresión es verdadera o falsa, se ejecuta un bloque de código específico.

En Python, la instrucción condicional más común es la instrucción **if**, que tiene la siguiente estructura:

```python
if condicion:
    # Bloque de código a ejecutar si la condición es verdadera
```

También se puede usar la instrucción else para proporcionar un bloque de código alternativo que se ejecutará si la condición es falsa:

```python
if condicion:
    # Bloque de código a ejecutar si la condición es verdadera
else:
    # Bloque de código a ejecutar si la condición es falsa

###################

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
```

Además, se pueden encadenar múltiples condiciones utilizando la instrucción elif (abreviatura de "else if"):
elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera sentencia verdadera.

```python
if condicion1:
    # Bloque de código a ejecutar si la condicion1 es verdadera
elif condicion2:
    # Bloque de código a ejecutar si la condicion1 es falsa y la condicion2 es verdadera
else:
    # Bloque de código a ejecutar si todas las condiciones anteriores son falsas

###################

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

```

Estas instrucciones condicionales son fundamentales para escribir programas que tomen decisiones basadas en ciertas condiciones.

Se debe prestar atención adicional a este caso:

* No debes usar else sin un if precedente.
* else siempre es la última rama de la cascada, independientemente de si has usado elif o no.
* else es una parte opcional de la cascada, y puede omitirse.
* Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas.
* Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.


# Sangría

En Python, los espacios de sangría se definen mediante la cantidad de espacios en blanco al principio de una línea de código.     
Por convención, se recomienda usar **cuatro espacios** para cada nivel de sangría.

Una instrucción con sangría o un conjunto de instrucciones (se requiere absolutamente al menos una instrucción); la sangría se puede lograr de dos maneras:  

1. insertando un número particular de espacios (la recomendación es usar cuatro espacios de sangría), o 
2. usando el tabulador;   
   **nota:**  
    si hay mas de una instrucción en la parte con sangría, la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan tabuladores con espacios, es importante que todas las sangrías sean exactamente iguales Python 3 no permite mezclar espacios y tabuladores para la sangría.

Por ejemplo, en una instrucción condicional if, el bloque de código que se ejecuta si la condición es verdadera debe estar sangrado con cuatro espacios adicionales con respecto a la línea que contiene la instrucción if. Del mismo modo, cualquier bloque de código dentro de un bucle for o while, una función, una clase, etc., también debe estar sangrado de la misma manera.

Aquí tienes un ejemplo de cómo se utilizan los espacios de sangría en Python:

```python
if condicion:
    # Este bloque de código está sangrado con cuatro espacios
    instruccion1
    instruccion2
    # Fin del bloque de código del if

for elemento in lista:
    # Este bloque de código también está sangrado con cuatro espacios
    instruccion3
    instruccion4
    # Fin del bloque de código del for

def mi_funcion():
    # Este bloque de código también está sangrado con cuatro espacios
    instruccion5
    instruccion6
    # Fin del bloque de código de la función

```

Es importante mantener una consistencia en el uso de espacios de sangría en todo el código Python para que sea legible y fácil de entender.