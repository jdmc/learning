[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md)  

# Sintaxis

La sintaxis se refiere a las reglas y estructuras gramaticales que gobiernan cómo se escribe y se estructura el código en un lenguaje de programación específico. 
Es decir, define la forma correcta en que deben combinarse las palabras clave, operadores, variables y otros elementos del lenguaje para formar instrucciones válidas y comprensibles para el ordenador.

En el contexto de la programación, tener una sintaxis correcta es crucial, ya que un error en la sintaxis puede llevar a que el programa no funcione correctamente o incluso a que no se ejecute en absoluto. Los lenguajes de programación tienen reglas específicas de sintaxis que deben seguirse para que el código sea válido y pueda ser interpretado por el compilador o intérprete del lenguaje.

Por ejemplo, en Python, una sintaxis incorrecta puede ser olvidar los dos puntos (:) al definir una función o un bucle, o escribir mal una palabra clave como if o else.

En resumen, la sintaxis en programación se refiere a las reglas y convenciones que dictan cómo se estructuran y escriben las instrucciones en un lenguaje de programación específico.


# str

En Python, 'str' es un tipo de dato que representa una cadena de caracteres, es decir, una secuencia de caracteres Unicode. Las cadenas en Python se pueden definir utilizando comillas simples (') o comillas dobles (").

Aquí tienes algunos ejemplos de cómo usar str en Python:

* Declaración de una cadena:

```python
cadena = 'Hola, mundo!'

```
* Concatenación de cadenas:

```python
cadena1 = 'Hola'
cadena2 = 'mundo'
concatenada = cadena1 + ', ' + cadena2 + '!'

```
* Acceso a caracteres individuales:
```python
cadena = 'Python'
primer_caracter = cadena[0]  # 'P'

```
* Subcadenas:
```python
cadena = 'Python'
subcadena = cadena[2:5]  # 'tho'

```
* Conversión de otros tipos de datos a cadenas:
```python
numero = 42
cadena = str(numero)  # '42'

```
>En resumen, 'str' en Python es un tipo de dato utilizado para representar cadenas de caracteres y se puede usar para manipular texto de diversas formas, como concatenación, acceso a caracteres individuales, extracción de subcadenas y conversión de otros tipos de datos a cadenas.




# int

En Python, 'int' es un tipo de dato que representa números **enteros**. Los enteros en Python pueden ser positivos o negativos y no tienen límite de tamaño, a menos que se supere la cantidad de memoria disponible en el sistema.

Aquí tienes algunos ejemplos de cómo usar int en Python:

* Declaración de un número entero:

```python
numero_entero = 42

```
* Operaciones aritméticas con números enteros:

```python
suma = 10 + 20
resta = 50 - 30
multiplicacion = 5 * 6
division = 100 / 4

```
* Conversión de cadenas a números enteros:

```python
cadena = '42'
numero_entero = int(cadena)  # 42

```
* Representación en base numérica:

```python
numero_binario = 0b1010  # Representación binaria de 10
numero_octal = 0o12  # Representación octal de 10
numero_hexadecimal = 0xA  # Representación hexadecimal de 10

```
> En resumen, int en Python es un tipo de dato utilizado para representar números enteros y se puede usar para realizar operaciones aritméticas, conversión de cadenas a enteros y representación en diferentes bases numéricas.

# sangrado / indentación

El sangrado en Python se refiere a la forma en que se estructura el código utilizando **espacios** o **tabulaciones** al principio de las líneas. En Python, el sangrado es crucial ya que se utiliza para delimitar bloques de código, como aquellos dentro de bucles, funciones, clases y condicionales.

El término "sangrado" y "indentación" se utilizan indistintamente para referirse al espacio o tabulación al principio de una línea de código que define un bloque de instrucciones. Entonces, en el contexto de Python, "sangrado" y "indentación" se refieren a la misma práctica de estructurar el código mediante la alineación de líneas con respecto a otras líneas de código.

Por ejemplo, en un bucle for en Python, el código dentro del bucle se identifica mediante un sangrado consistente:

```python
for i in range(5):
    print(i)  # Este print está dentro del bucle, gracias al sangrado

```
En este caso, el print(i) está dentro del bucle for porque tiene un nivel de sangrado mayor que el for i in range(5):. Si se elimina el sangrado, el código producirá un error de sintaxis.

## 4 espacios

El sangrado en Python suele hacerse con **espacios**, siendo recomendado usar **4 espacios** por nivel de sangrado, aunque también se puede usar una tabulación (aunque es menos común y puede causar problemas de consistencia si se mezclan tabulaciones y espacios).

Es importante mantener una consistencia en el uso del sangrado a lo largo de todo el código, ya que Python utiliza el sangrado como parte de su sintaxis. Un cambio en el sangrado puede cambiar la estructura del código y, por lo tanto, su significado.

>En resumen, el sangrado en Python es una parte fundamental de su sintaxis y se utiliza para delimitar bloques de código, como bucles, funciones, clases y condicionales. Es importante mantener un sangrado consistente para garantizar la legibilidad y funcionalidad del código.

### Sangría francesa

La "sangría francesa" es una convención de estilo que implica alinear verticalmente los elementos de una estructura de datos, como diccionarios o listas, de manera que resulte más legible y estéticamente agradable. En Python, esto significa que los elementos clave-valor de un diccionario, por ejemplo, se alinean verticalmente, como en el ejemplo que proporcionaste:

´´´python

dictionary = {
              "gato":   "chat",
              "perro":  "chien",
              "caballo":"cheval"
              }
´´´

Esta práctica ayuda a mantener una estructura visualmente agradable y facilita la lectura y comprensión del código. Sin embargo, es importante tener en cuenta que esto es más una convención de estilo y preferencia personal que un requisito estricto de Python. La legibilidad del código es fundamental, y diferentes equipos o proyectos pueden tener diferentes convenciones de estilo. Lo más importante es mantener la consistencia dentro de un proyecto o equipo de desarrollo.


# Expresión 

En Python, una expresión es una combinación de valores, variables, operadores y llamadas a funciones que se evalúa para producir un resultado. 
En otras palabras, **una expresión es cualquier fragmento de código que pueda evaluarse y devolver un valor**. 

Por ejemplo:

```python
3 + 5

```
Aquí, 3 + 5 es una expresión que se evalúa como 8.

Las expresiones pueden ser simples, como en el ejemplo anterior, o más complejas, involucrando llamadas a funciones, operaciones lógicas o estructuras de datos más elaboradas. Algunos ejemplos de expresiones más complejas incluyen:

```python
x = 10
y = 5
z = (x + y) * 2

```

En este ejemplo, (x + y) * 2 es una expresión que primero suma los valores de x e y, y luego multiplica el resultado por 2. El resultado de esta expresión se asigna a la variable z.
 De manera similar, expresiones más complejas pueden representar cálculos más elaborados, como operaciones aritméticas, operaciones lógicas, manipulación de datos, etc.

>En resumen, las expresiones en Python son constructos que se evalúan para producir un valor y son fundamentales para la programación en Python.

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md)  