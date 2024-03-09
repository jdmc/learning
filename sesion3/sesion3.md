[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Listas

Las listas en Python son un tipo de dato que se utiliza para almacenar una colección ordenada y mutable de elementos.

Las listas se definen entre corchetes y los elementos se separan por comas.

```python

mi_lista = ["Hola", 1, True]

```

En este ejemplo, se crea una lista con tres elementos: una cadena, un número entero y un valor booleano.

Las listas son muy versátiles y se pueden usar para almacenar cualquier tipo de dato, incluso otras listas.

Las listas son mutables, lo que significa que se pueden modificar los elementos de una lista después de que se ha creado.

Se puede **agregar**, **eliminar** o **modificar** elementos de una lista.

Las listas son una herramienta poderosa para organizar y almacenar datos en Python.

Aquí hay algunos ejemplos de cómo se pueden usar las listas:

* Almacenar una lista de nombres.
* Almacenar una lista de números.
* Almacenar una lista de tareas.

Las listas son una herramienta fundamental para el desarrollo de aplicaciones en Python.

# Append

append() es un método que se utiliza para agregar un elemento al final de una lista en Python.

El método append() toma un solo argumento, que es el elemento que se desea agregar a la lista.

Ejemplo:

```python
mi_lista = ["Hola", 1, True]

mi_lista.append("nuevo elemento")

print(mi_lista)

```
 En este ejemplo, se agrega el elemento "nuevo elemento" al final de la lista mi_lista. 

La lista final será ["Hola", 1, True, "nuevo elemento"].

El método append() es una forma sencilla de agregar elementos a una lista.

Es importante tener en cuenta que el método append() no devuelve ningún valor.

Aquí hay algunos ejemplos adicionales de cómo se puede usar el método append():

* Agregar un número al final de una lista de números.
* Agregar una cadena al final de una lista de cadenas.
* Agregar una lista al final de una lista de listas.

El método append() es una herramienta útil para trabajar con listas en Python.

# Funciones 

En Python, una función es un bloque de código reutilizable que se utiliza para realizar una tarea específica. Las funciones permiten dividir el código en partes más pequeñas y manejables, lo que facilita la organización, comprensión y reutilización del código.

Una función en Python generalmente tiene la siguiente estructura:

```python
def nombre_de_la_funcion(parametros):
    """Documentación de la función (docstring)"""
    # Cuerpo de la función
    # Realiza alguna tarea con los parámetros
    return resultado

```
* **def** es la palabra clave y reservada que se utiliza para definir una función.
* **nombre_de_la_funcion** es el nombre de la función, que se utiliza para llamar a la función más tarde.
* **parametros** son los valores que la función espera recibir cuando se llama. Pueden ser opcionales.
* La cadena de texto entre triple comillas **"""** es la documentación de la función, también conocida como docstring. Proporciona una descripción de lo que hace la función.
* El cuerpo de la función contiene las instrucciones que se ejecutarán cuando se llame a la función.
* **return** es la palabra clave utilizada para devolver un valor de la función. Puede devolver un solo valor o una tupla de valores.

Aquí hay un ejemplo simple de una función que suma dos números:

```python
def suma(a, b):
    """Esta función suma dos números"""
    resultado = a + b
    return resultado

# Llamamos a la función y mostramos el resultado
print(suma(3, 5))  # Imprime 8

```
En este ejemplo, la función **suma** toma dos parámetros a y b, suma estos dos valores y devuelve el resultado. Luego, llamamos a la función con los argumentos 3 y 5, lo que devuelve 8, que se imprime.


## Funcionamiento de las funciones

El funcionamiento de las funciones en Python es bastante sencillo y sigue algunos pasos básicos. Aquí está una descripción general del funcionamiento de las funciones en Python:

1. Definición de la función:     
  Primero, defines la función utilizando la palabra clave **def**, seguida del nombre de la función y los parámetros entre paréntesis. Puedes incluir un bloque de código en el cuerpo de la función que realiza una tarea específica.

```python
def mi_funcion(parametro1, parametro2):
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado

```

2. Llamada a la función:     
  Para ejecutar el código dentro de la función y obtener un resultado, necesitas llamar a la función. Puedes llamar a una función pasando valores conocidos como argumentos.

```python
resultado = mi_funcion(5, 3)

```
En este ejemplo, estamos llamando a la función mi_funcion y pasando los valores 5 y 3 como argumentos. El resultado devuelto por la función se asigna a la variable resultado. 

3. Ejecución del código en la función:     
  Cuando llamas a la función, Python ejecuta el código dentro del cuerpo de la función utilizando los valores proporcionados como argumentos. Dentro de la función, puedes realizar cualquier tarea deseada utilizando los parámetros proporcionados y otras variables.

4. Retorno de valores:     
  Si la función incluye una declaración de retorno (return), el valor especificado en la declaración de retorno se devuelve a la ubicación de la llamada a la función. Esto permite que la función proporcione resultados útiles que pueden ser utilizados en otros lugares del programa.

5. Finalización de la función: 
  Una vez que la función ha completado su tarea y ha devuelto un valor (si es necesario), la ejecución del programa continúa desde el punto donde se realizó la llamada a la función.

> En resumen, las funciones en Python son bloques de código reutilizables que aceptan entradas, realizan operaciones basadas en esas entradas y pueden devolver un resultado. Esto permite que el código sea más modular, más fácil de entender y más fácil de mantener.

### Invocar

"Invocar" en el contexto de la programación se refiere a llamar o ejecutar una función o método. Cuando invocas una función, estás solicitando que se ejecute el bloque de código dentro de esa función con los argumentos especificados, si los hay.

En Python, para invocar una función, simplemente escribes el nombre de la función seguido de paréntesis que contienen los argumentos, si los necesita. 

Por ejemplo:

```python
resultado = suma(3, 5)

```
En este ejemplo, suma es el nombre de la función que se está invocando, y se están pasando los argumentos 3 y 5 para que la función sume esos dos valores.

Del mismo modo, en otros contextos de programación, como en el contexto de la programación orientada a objetos, "invocar" puede referirse a llamar a un método de un objeto. Un método es una función que está asociada a un objeto en particular y opera en los datos asociados a ese objeto. 

Por ejemplo:

```python
mi_string = "Hola, mundo!"
longitud = mi_string.count('o')
```
En este caso, count() es un método del objeto mi_string que cuenta el número de ocurrencias del carácter especificado. Al llamar al método count(), estamos invocando el método en el objeto mi_string para realizar una operación específica en esos datos.

## Funciones parametrizadas

Las funciones parametrizadas, también conocidas como funciones con parámetros, son funciones que aceptan uno o más valores (parámetros) que se pasan cuando la función es llamada. Estos parámetros proporcionan datos a la función que pueden ser utilizados dentro del cuerpo de la función para realizar operaciones específicas.

En Python, puedes definir funciones que acepten cualquier número de parámetros. Estos parámetros se colocan entre paréntesis en la definición de la función y se utilizan como variables dentro del cuerpo de la función. Cuando llamas a la función, proporcionas valores para estos parámetros, que se utilizan como datos de entrada para la función.

Por ejemplo, considera esta función simple en Python:

```python
def saludar(nombre):
    print("¡Hola,", nombre, "!")

```
En esta función, nombre es un parámetro que se utiliza para recibir un valor cuando la función saludar() es llamada. Puedes llamar a esta función con diferentes nombres para saludar a diferentes personas:

```python
saludar("Juan")  # Imprime "¡Hola, Juan !"
saludar("María")  # Imprime "¡Hola, María !"

```
Aquí, cada vez que llamamos a la función saludar(), pasamos un nombre diferente como argumento, y ese nombre se utiliza dentro de la función como el valor del parámetro nombre.

```python
def suma(a, b):
    """Esta función suma dos números."""
    resultado = a + b
    return resultado

```

En esta función suma(a, b), hay dos parámetros: a y b. Cuando llamas a esta función, necesitas proporcionar dos valores como argumentos. 

Por ejemplo:

```python
resultado = suma(5, 3)
print(resultado)  # Imprime 8

```
En este caso, 5 se pasa como el primer argumento (a) y 3 se pasa como el segundo argumento (b). Dentro de la función, estos valores se suman y el resultado, 8, se devuelve y se asigna a la variable resultado.

Puedes llamar a la función suma() con diferentes pares de valores como argumentos, y la función sumará los valores correspondientes en cada llamada. 

Por ejemplo:

```python
resultado = suma(10, 20)
print(resultado)  # Imprime 30

resultado = suma(-3, 8)
print(resultado)  # Imprime 5

```
En cada caso, la función suma() toma los dos valores pasados como argumentos, los suma y devuelve el resultado correspondiente. 
Esto muestra cómo puedes definir y utilizar una función con varios parámetros en Python.

>En resumen, las funciones parametrizadas son funciones que aceptan parámetros o argumentos cuando son llamadas, permitiendo que se realicen operaciones específicas en función de los valores proporcionados. Esto hace que las funciones sean más flexibles y reutilizables, ya que pueden trabajar con diferentes conjuntos de datos sin necesidad de modificar el código de la función en sí.

### Paso de parámetros posicionales
El paso de parámetros posicionales es un método común de pasar argumentos a una función en Python. En este enfoque, los valores pasados como argumentos se asignan a los parámetros de la función basándose en su posición en la lista de argumentos.

Cuando llamas a una función y proporcionas argumentos, estos argumentos se asignan a los parámetros de la función en el **mismo orden** en el que se pasan. Por lo tanto, el primer argumento se asigna al primer parámetro, el segundo argumento al segundo parámetro, y así sucesivamente.

Aquí tienes un ejemplo de paso de parámetros posicionales:

```python
def saludar(nombre, apellido):
    print("¡Hola,", nombre, apellido, "!")

```
Cuando llamas a esta función, debes proporcionar dos valores: uno para nombre y otro para apellido, en ese orden. 

Por ejemplo:

```python
saludar("Juan", "Pérez")  # Imprime "¡Hola, Juan Pérez !"

```
En este ejemplo, "Juan" se pasa como el primer argumento, por lo que se asigna al parámetro nombre, y "Pérez" se pasa como el segundo argumento, por lo que se asigna al parámetro apellido.

El paso de parámetros posicionales es el método más común de pasar argumentos a una función en Python y es bastante intuitivo. Sin embargo, debes asegurarte de pasar los argumentos en el orden correcto para evitar errores en la ejecución de tu código.

### Paso de argumentos con palabra clave

El paso de argumentos con palabra clave es otra forma de pasar argumentos a una función en Python. En este enfoque, en lugar de depender del orden de los argumentos para asignar valores a los parámetros de la función, **especificas explícitamente** qué parámetro debe recibir qué valor utilizando el nombre del parámetro.

Para utilizar el paso de argumentos con palabra clave, al llamar a una función, proporcionas los argumentos junto con el nombre del parámetro al que deseas asignar ese valor. Esto ofrece una mayor claridad y flexibilidad en comparación con el paso de argumentos por posición, ya que puedes especificar los valores de los parámetros en cualquier orden.

Aquí tienes un ejemplo de paso de argumentos con palabra clave:

```python
def saludar(nombre, apellido):
    print("¡Hola,", nombre, apellido, "!")

```

Cuando llamas a esta función, puedes pasar los argumentos utilizando la sintaxis nombre=valor:

```python
saludar(apellido="Pérez", nombre="Juan")  # Imprime "¡Hola, Juan Pérez !"

```
En este ejemplo, estamos llamando a la función saludar() y pasando los argumentos utilizando la palabra clave nombre y apellido. Esto asegura que los valores se asignen correctamente a los parámetros nombre y apellido de la función, independientemente del orden en que se pasen los argumentos.

El paso de argumentos con palabra clave proporciona una mayor claridad en el código y evita confusiones al especificar los valores de los parámetros. También permite omitir argumentos opcionales y proporcionar solo los valores que son relevantes para la llamada de la función.


## Argumento (un poquito más sobre el)

En Python, un argumento se refiere a **un valor que se pasa a una función o método cuando se llama**. Los argumentos proporcionan los datos que la función necesita para **realizar su tarea**. Dependiendo de cómo se defina la función, puede aceptar diferentes tipos de argumentos:

### Argumentos posicionales: 
Son los argumentos que se pasan a una función en el mismo orden en que están definidos en la firma de la función. Por ejemplo:

```python
def saludar(nombre, saludo):
    print(f"{saludo}, {nombre}!")

# Llamada a la función con argumentos posicionales
saludar("Juan", "Hola")

```
En este caso, "Juan" se pasa como el primer argumento (nombre) y "Hola" como el segundo argumento (saludo).

### Argumentos de palabra clave: 

Son los argumentos que se pasan a una función utilizando su nombre, lo que permite especificar los valores para parámetros específicos independientemente de su posición. Por ejemplo:

```python

saludar(saludo="Hola", nombre="María")

```
En este caso, los nombres de los parámetros (nombre y saludo) se utilizan para asociar los valores pasados a la función.

### Argumentos por defecto:

Son argumentos que tienen un valor predeterminado establecido en la firma de la función. Si no se proporciona un valor para estos argumentos al llamar a la función, se utilizará el valor predeterminado. Por ejemplo:

```python
def contar_hasta(numero, inicio=1):
    for i in range(inicio, numero + 1):
        print(i)

# Llamada a la función con un solo argumento
contar_hasta(5)

```
En este caso, el argumento inicio tiene un valor predeterminado de 1, por lo que si no se proporciona un segundo argumento al llamar a contar_hasta(), la cuenta comenzará desde 1.

Los argumentos en Python son extremadamente versátiles y pueden combinarse de varias maneras para proporcionar flexibilidad en la definición y llamada de funciones.

### Combinar Argumentos

Es posible combinar argumentos posicionales y de palabra clave al llamar a una función en Python. Esto significa que puedes pasar algunos argumentos por su posición y otros utilizando su nombre de parámetro.

Cuando combinas argumentos posicionales y de palabra clave, los **argumentos posicionales** deben ir **primero** en la lista de argumentos, seguidos por los argumentos de palabra clave. Esto es necesario para evitar ambigüedades en la asignación de valores a los parámetros de la función.

Aquí tienes un ejemplo que ilustra cómo combinar argumentos posicionales y de palabra clave:

```python
def saludar(nombre, apellido):
    print("¡Hola,", nombre, apellido, "!")

```
Puedes llamar a esta función de la siguiente manera, proporcionando un argumento posicional (nombre) y un argumento de palabra clave (apellido):

```python
saludar("Juan", apellido="Pérez")  # Imprime "¡Hola, Juan Pérez !"

```

En este ejemplo, "Juan" se pasa como un argumento posicional, por lo que se asigna al parámetro nombre, y "Pérez" se pasa como un argumento de palabra clave, por lo que se asigna al parámetro apellido.

Del mismo modo, también puedes combinar argumentos de palabra clave y argumentos posicionales en diferentes posiciones:

```python
saludar(apellido="Pérez", nombre="Juan")  # Imprime "¡Hola, Juan Pérez !"

```
Ambos enfoques son válidos y permiten especificar claramente qué valores corresponden a qué parámetros, lo que hace que el código sea más legible y menos propenso a errores.

# return, la instrucción

La instrucción 'return' en Python se utiliza dentro de una función para devolver un valor específico de esa función. Cuando la ejecución de una función alcanza una declaración 'retur'n, la función se detiene y el valor especificado después de return se devuelve como resultado de la función.

La instrucción return puede aparecer en cualquier lugar dentro del cuerpo de una función, y una vez que se alcanza, la ejecución de la función se detiene inmediatamente. También puede haber múltiples declaraciones return dentro de una función, pero solo una se ejecutará en cada llamada a la función.

Aquí hay un ejemplo simple que muestra cómo funciona la instrucción return:

```python
def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(3, 5)
print(resultado_suma)  # Imprimirá 8

```

En este ejemplo, cuando la función suma(a, b) se llama con los argumentos 3 y 5, calcula la suma de estos dos valores y devuelve el resultado utilizando la instrucción return. Luego, el valor devuelto (8) se asigna a la variable resultado_suma y se imprime.

Es importante tener en cuenta que si no se especifica una declaración return en una función, la función devuelve None por defecto al finalizar su ejecución.

También puedes utilizar la instrucción return sin un valor para finalizar la ejecución de la función sin devolver ningún valor específico. Por ejemplo:

```python
def saludar(nombre):
    if nombre:
        print("¡Hola,", nombre, "!")
        return
    print("¡Hola, mundo!")

saludar("Juan")  # Imprimirá "¡Hola, Juan !"
saludar("")      # Imprimirá "¡Hola, mundo!"

```

En este ejemplo, si se proporciona un nombre, la función imprime un saludo personalizado y luego se detiene la ejecución de la función con return. Si no se proporciona un nombre, se imprime un saludo predeterminado y la función se detiene sin devolver ningún valor específico.


## return sin una expresión

La instrucción 'return' sin una expresión simplemente finaliza la ejecución de la función y devuelve None como valor de retorno. Esto es útil cuando una función no necesita devolver ningún valor específico o cuando solo necesita realizar ciertas acciones y no necesariamente devolver un resultado.

Aquí tienes un ejemplo simple que muestra cómo usar return sin una expresión:

```python
def saludar():
    print("¡Hola, mundo!")
    # No hay una declaración 'return' con una expresión aquí

saludo = saludar()
print(saludo)  # Imprimirá None

```
En este ejemplo, la función saludar() simplemente imprime "¡Hola, mundo!" y no tiene una declaración return con una expresión. Por lo tanto, cuando llamamos a la función saludar(), se ejecuta el código dentro de la función y luego termina, devolviendo None automáticamente.

Puedes ver que cuando asignamos el resultado de saludar() a la variable saludo, saludo contendrá None, ya que esa es la "salida" de la función saludar().

La instrucción return sin una expresión es especialmente útil en casos donde la función realiza algún tipo de acción o operación pero no necesita devolver ningún resultado específico.

En Python, la instrucción return no es obligatoria en una función. Si una función no incluye explícitamente una declaración return, la función devolverá None de forma implícita al finalizar su ejecución.

Por lo tanto, es completamente válido escribir una función sin una declaración return, especialmente si la función no necesita devolver ningún valor específico. La omisión de return es común en funciones que realizan acciones, como imprimir mensajes en la consola o modificar objetos, pero no necesitan devolver ningún resultado calculado.

## return con una expresión

Una declaración return con una expresión en Python es aquella en la que devuelves un valor específico de la función. Este valor puede ser cualquier expresión válida en Python, como una variable, una operación matemática, una cadena de texto, una lista, etc.

Aquí tienes un ejemplo de una función que utiliza return con una expresión para devolver la suma de dos números:

```python
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)  # Imprimirá 8

```

En este ejemplo, la función suma(a, b) toma dos argumentos, a y b, y devuelve la suma de estos dos números utilizando la expresión return a + b. Cuando se llama a la función con suma(3, 5), devuelve 8, que se asigna a la variable resultado y luego se imprime.

Puedes utilizar return con cualquier expresión que desees devolver como resultado de la función. 

Por ejemplo:

```python
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))  # Imprimirá True
print(es_par(5))  # Imprimirá False

```

En este ejemplo, la función es_par(numero) devuelve True si el número dado es par y False si es impar, utilizando una expresión condicional con return.

### None

En Python, None es un valor especial que representa la ausencia de un valor o la falta de cualquier valor específico. Es similar a null en otros lenguajes de programación.

None se utiliza comúnmente para indicar que una variable no está asignada o que una función no devuelve ningún valor específico. Puedes pensar en None como un marcador para indicar que algo está vacío o sin definir.

Aquí tienes algunos ejemplos de cómo se utiliza None en Python:

* Asignación de variables a None:

```python
variable_sin_valor = None

```
En este caso, variable_sin_valor se declara pero no se le asigna ningún valor específico. Por defecto, Python asigna None a esta variable.

* Devolución de None desde una función:

```python
def funcion_sin_retorno():
    print("Esta función no devuelve ningún valor")

resultado = funcion_sin_retorno()
print(resultado)  # Imprimirá None

```

En este ejemplo, la función funcion_sin_retorno() no tiene una declaración return, por lo que devuelve automáticamente None. Cuando se asigna el resultado de la función a una variable y se imprime, se mostrará None.

* Comprobación de igualdad con None:

```python
variable = None

if variable is None:
    print("La variable no tiene ningún valor asignado")
else:
    print("La variable tiene un valor asignado:", variable)

```
Aquí, 'is None' se utiliza para verificar si variable no tiene ningún valor asignado.

None es un tipo de dato propio en Python y se puede utilizar en comparaciones y comprobaciones de igualdad. Es importante tener en cuenta que None no es lo mismo que False o 0, aunque None, False y 0 se consideran todos como valores falsos en contextos booleanos.

### global

En Python, la palabra clave 'global' se utiliza dentro de una función para indicar que una variable definida dentro de esa función pertenece al ámbito global en lugar de al ámbito local de la función.

Cuando defines una variable dentro de una función sin usar la palabra clave global, esa variable se considera local a esa función y no se puede acceder a ella desde fuera de la función. Sin embargo, si necesitas modificar una variable global desde dentro de una función, puedes utilizar la palabra clave global para indicar que deseas trabajar con la variable global y no crear una variable local con el mismo nombre.

Aquí tienes un ejemplo que demuestra el uso de la palabra clave global:

```python
x = 10  # Variable global

def modificar_global():
    global x  # Indica que 'x' es una variable global
    x = 20   # Modifica el valor de 'x' a nivel global

print("Antes de llamar a la función:", x)  # Imprime el valor de 'x' antes de llamar a la función
modificar_global()                         # Llama a la función que modifica 'x'
print("Después de llamar a la función:", x) # Imprime el valor de 'x' después de llamar a la función

```
En este ejemplo, definimos una variable global 'x' con el valor 10. Luego, creamos una función modificar_global() que utiliza la palabra clave global para indicar que x es una variable global. Dentro de la función, modificamos el valor de x a 20. Cuando llamamos a la función y luego imprimimos el valor de x, vemos que el valor de x ha sido modificado globalmente.

Es importante tener en cuenta que el uso de variables globales puede dificultar la comprensión y el mantenimiento del código, ya que pueden ser modificadas desde cualquier parte del programa. Por lo tanto, se recomienda utilizarlas con moderación y preferir el uso de variables locales siempre que sea posible.

# Iteracion, Iterar, Iterable, Iteradores

Iterar es el proceso de recorrer elementos en una secuencia uno por uno. Un objeto iterable es aquel que se puede recorrer o iterar, es decir, que se puede utilizar en un bucle para acceder a sus elementos secuencialmente. Los iteradores son objetos que facilitan la iteración sobre un iterable, manteniendo un estado interno que recuerda el elemento actual en la secuencia y permite avanzar al siguiente elemento.

Un objeto iterable en Python es cualquier objeto que implemente el método \__iter__(), que devuelve un iterador. Por otro lado, un iterador en Python es cualquier objeto que implemente el método \__next__(), que devuelve el siguiente elemento de la secuencia o lanza una excepción StopIteration cuando se alcanza el final de la secuencia.

Aquí tienes un ejemplo para entender mejor estos conceptos:

```python
# Creamos una lista, que es un objeto iterable
mi_lista = [1, 2, 3, 4, 5]

# Creamos un iterador a partir de la lista
mi_iterador = iter(mi_lista)

# Iteramos sobre los elementos utilizando el iterador
while True:
    try:
        # Obtenemos el siguiente elemento del iterador
        elemento = next(mi_iterador)
        print(elemento)
    except StopIteration:
        # Cuando se alcanza el final de la lista, se lanza StopIteration
        break

```

En este ejemplo, mi_lista es un objeto iterable, y mi_iterador es un iterador creado a partir de la lista. Luego, utilizamos un bucle while junto con el método next() para iterar sobre los elementos de la lista utilizando el iterador. Cada llamada a next() devuelve el siguiente elemento de la lista, y cuando se alcanza el final de la lista, se lanza la excepción StopIteration, lo que nos permite salir del bucle.

Aquí está la secuencia de eventos:

1. Tenemos un objeto iterable, que en este caso es una lista (mi_lista).
2. Creamos un iterador a partir de este objeto iterable usando la función iter() (mi_iterador = iter(mi_lista)).
3. Utilizamos un bucle while para iterar sobre los elementos del iterable.
4. En cada iteración del bucle, llamamos a next() para obtener el siguiente elemento del iterador (elemento = next(mi_iterador)).
5. Cuando alcanzamos el final del iterable y no hay más elementos para iterar, next() lanza una excepción StopIteration.
6. Capturamos esta excepción usando un bloque try-except, lo que nos permite salir del bucle while y finalizar la iteración.

Entonces, efectivamente, el bucle while es responsable de mantener la iteración mientras haya elementos en el iterable. Y repetimos la iteración accediendo al siguiente elemento en cada iteración del bucle hasta que alcanzamos el final del iterable.

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 