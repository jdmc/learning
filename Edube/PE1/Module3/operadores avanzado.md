# Operadores 

[Operadores 1](Edube\PE1\Module2\operadores_y_expresiones.md)  

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
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()

################### Sentencias if-else anidadas

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

# Pseudocódigo e introducción a los bucles (ciclos)

## Pseudocódigo

El pseudocódigo es una forma de representar algoritmos utilizando un lenguaje informal y cercano al lenguaje humano, que describe la lógica de un programa sin utilizar una sintaxis de programación específica. El objetivo del pseudocódigo es expresar las operaciones y la lógica del algoritmo de una manera clara y comprensible, sin preocuparse por detalles específicos de implementación o sintaxis de un lenguaje de programación real.

El pseudocódigo suele ser utilizado como una etapa inicial en el proceso de diseño de programas, permitiendo a los programadores planificar y diseñar la estructura y el flujo de su código antes de comenzar a escribirlo en un lenguaje de programación real.

Aquí tienes un ejemplo simple de pseudocódigo que describe un algoritmo para sumar dos números:

```python

Inicio
    Leer el primer número (a)
    Leer el segundo número (b)
    Sumar a y b y almacenar el resultado en una variable (resultado)
    Mostrar el resultado
Fin

```
Como puedes ver, el pseudocódigo utiliza palabras clave como "Leer", "Sumar", "Mostrar", etc., para describir las acciones que debe realizar el algoritmo, pero no se preocupa por la sintaxis específica de un lenguaje de programación real. Esto lo hace más accesible y fácil de entender para cualquier persona familiarizada con los conceptos básicos de la programación.

# Bucles / Ciclos

Los bucles, también conocidos como ciclos, son estructuras de control que permiten repetir un bloque de código varias veces.   
En Python, hay dos tipos principales de bucles: el bucle "for" y el bucle "while".

### for
1. Bucle for: 
   Este bucle se utiliza para iterar sobre una secuencia de elementos, como una lista, una tupla, un diccionario, etc.   
   La sintaxis básica del bucle for es la siguiente:


```python
for elemento in secuencia:
    # Bloque de código a ejecutar en cada iteración

```
Donde elemento es una variable que toma el valor de cada elemento en la secuencia en cada iteración del bucle, y secuencia es la secuencia sobre la cual se está iterando.

### while 
2. Bucle while:  
   Este bucle se utiliza para repetir un bloque de código mientras una condición sea verdadera.   
   La sintaxis básica del bucle while es la siguiente:

```python
while condicion:
    # Bloque de código a ejecutar mientras la condición sea verdadera

```
Donde condicion es una expresión booleana que se evalúa en cada iteración del bucle. El bucle se ejecuta mientras esta condición sea verdadera.


Aquí tienes un ejemplo de cada tipo de bucle:

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

```
Bucle while:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

```

#### for

Ambos bucles imprimirán los números del 0 al 4.  
El bucle **for** itera sobre la lista de números, mientras que el bucle **while** incrementa un contador hasta que llega a 5.

En realidad, el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento.

### range()

La función range() en Python es una función que genera una secuencia inmutable de números en un rango especificado. Se utiliza comúnmente en bucles for para iterar sobre una secuencia de números.

La sintaxis general de range() es la siguiente:

```Python

range([start], stop[, step])

```
Donde:

start: Es el valor inicial del rango. Este argumento es opcional y por defecto es 0 si no se especifica.
stop: Es el valor final del rango. Este argumento es obligatorio y marca el límite superior del rango. El valor de stop **no** está incluido en la secuencia generada.
step: Es el tamaño del paso entre los números en la secuencia. Este argumento es opcional y por defecto es 1 si no se especifica.

Es importante destacar que la secuencia generada por range() es inmutable y no se puede modificar. Si deseas obtener una lista con los valores generados por range(), puedes convertir la salida a una lista utilizando la función list().

```python
# Generar una secuencia de números del 0 al 4 (excluyendo el 5)
for i in range(5):
    print(i)

# Generar una secuencia de números del 2 al 8 (excluyendo el 9) con un paso de 2
for i in range(2, 10, 2):
    print(i)

# Convertir la secuencia generada por range en una lista
my_list = list(range(5))
print(my_list)  # Output: [0, 1, 2, 3, 4]

```

La función range() también puede aceptar tres argumentos: Echa un vistazo al código del editor.

El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada giro del bucle (como puedes sospechar, el valor predeterminado del incremento es 1).

Nota: el conjunto generado por range() debe ordenarse en un orden ascendente. No hay forma de forzar el range() para crear un conjunto en una forma diferente. Esto significa que el segundo argumento de range() debe ser mayor que el primero.

### break

break es una palabra clave en Python que se utiliza dentro de bucles (por ejemplo, for o while) para salir prematuramente del bucle en caso de que se cumpla una determinada condición. Cuando se encuentra la instrucción break dentro de un bucle, el flujo de control del programa sale inmediatamente del bucle y continúa con la siguiente instrucción después del bucle.

Aquí tienes un ejemplo sencillo de cómo se usa break en un bucle while:

```python
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break

```
En este caso, el bucle "while" imprimirá los números del 0 al 2, pero cuando "i" llega a 3, se ejecuta la instrucción "break", lo que hace que el bucle se detenga inmediatamente y el programa continúe con la siguiente instrucción después del bucle.

### continue

continue es otra palabra clave en Python que se utiliza dentro de bucles (por ejemplo, for o while) para continuar con la próxima iteración del bucle sin ejecutar el resto del código dentro del bucle en la iteración actual.

Cuando se encuentra la instrucción continue dentro de un bucle, el flujo de control del programa salta inmediatamente a la siguiente iteración del bucle, sin ejecutar ninguna de las líneas de código que siguen a la instrucción continue dentro de esa iteración actual.

Aquí tienes un ejemplo sencillo de cómo se usa continue en un bucle for:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)

```
Este código imprimirá los números del 0 al 4, excepto el número 2. Cuando i es igual a 2, se ejecuta la instrucción continue, lo que hace que el bucle pase a la siguiente iteración sin imprimir el número 2.

#### Ejercicio:

Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

* Imprima el enunciado "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO".
* Imprima "No, ¡quiero un gran ESPATIFILIO!" si la cadena ingresada es "espatifilo".
* Imprima "¡ESPATIFILIO!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

```python
# Tomar la cadena como entrada
cadena = input("Ingrese una cadena: ")

# Ejecución condicional para imprimir mensajes diferentes según la cadena ingresada
if cadena == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
elif cadena == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print(f"¡ESPATIFILIO!, ¡No {cadena}!")

```

En este programa, las comparaciones se hacen directamente con las cadenas en mayúsculas ("ESPATIFILIO") y minúsculas ("espatifilo").   
Si la cadena ingresada coincide exactamente con alguna de estas opciones, se imprime el mensaje correspondiente.

# Operadores bit a bit

Los operadores bit a bit son operadores que actúan a nivel de bits en los números binarios que representan los valores enteros. Estos operadores permiten realizar operaciones lógicas y aritméticas bit a bit en los números binarios.

Aquí hay algunos operadores bit a bit comunes:

1. AND Bit a Bit (&):     
  Este operador realiza una operación AND bit a bit entre los bits de los operandos. El resultado es 1 si ambos bits son 1; de lo contrario, es 0.

Ejemplo:

```python
a = 5    # Representación binaria: 101
b = 3    # Representación binaria: 011
resultado = a & b   # Resultado: 1 (binario: 001)

```

2. OR Bit a Bit (|):    
  Este operador realiza una operación OR bit a bit entre los bits de los operandos. El resultado es 1 si al menos uno de los bits es 1.

Ejemplo:

```python
a = 5    # Representación binaria: 101
b = 3    # Representación binaria: 011
resultado = a | b   # Resultado: 7 (binario: 111)

```