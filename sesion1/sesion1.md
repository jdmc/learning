[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md)  

# Compilation

La "compilación" (o "compilación de código") es el proceso de traducir el código fuente de un programa escrito en un lenguaje de programación de alto nivel (como Python, C++, Java, etc.) a un código ejecutable en lenguaje de máquina que la computadora puede entender directamente. Este proceso generalmente se realiza mediante un programa llamado "compilador".

La compilación es un paso importante en el ciclo de desarrollo de software y es necesario para ejecutar programas en una computadora. Durante la compilación, el compilador realiza varias tareas, que pueden incluir:

1. **Análisis léxico y sintáctico**: El compilador analiza el código fuente para verificar su sintaxis y estructura, identificando tokens y elementos gramaticales según las reglas del lenguaje de programación.

2. **Optimización**: El compilador puede realizar optimizaciones en el código para mejorar su rendimiento, como la eliminación de código muerto, la reorganización de instrucciones para minimizar los accesos a memoria, etc.

3. **Generación de código intermedio**: En algunos casos, el compilador puede generar un código intermedio antes de traducirlo completamente a lenguaje de máquina. Este código intermedio es una representación más abstracta del programa y puede ser más fácil de analizar y optimizar.

4. **Generación de código objeto**: Finalmente, el compilador genera el código objeto o ejecutable a partir del código fuente procesado. Este código objeto contiene instrucciones en lenguaje de máquina que la computadora puede ejecutar directamente.

>En resumen, la compilación es el proceso fundamental que convierte el código fuente de un programa en un formato que la computadora puede entender y ejecutar. Dependiendo del lenguaje de programación y del compilador utilizado, el proceso de compilación puede implicar diferentes etapas y técnicas.


# Interpretation

La "interpretación" es un proceso alternativo al de la compilación en el que el código fuente de un programa se ejecuta directamente por un intérprete, sin necesidad de ser compilado previamente a un código ejecutable de bajo nivel. En el enfoque de la interpretación, el intérprete lee y ejecuta el código fuente línea por línea, traduciéndolo a instrucciones ejecutables sobre la marcha.

Aquí hay algunas características clave de la interpretación:

1. **Ejecución directa**: En lugar de compilar el código a un formato ejecutable de bajo nivel, **el intérprete lee el código fuente** y lo ejecuta directamente. Cada línea de código se traduce a instrucciones ejecutables en tiempo de ejecución.

2. **Proceso paso a paso**: El intérprete procesa el código línea por línea, interpretando y ejecutando cada instrucción a medida que avanza. Esto permite una ejecución más flexible y dinámica del código, ya que los resultados de las instrucciones anteriores pueden influir en las siguientes.

3. **Menor eficiencia**: En general, los programas interpretados tienden a ser **más lentos** que los programas compilados, ya que el intérprete debe realizar la interpretación en tiempo real durante la ejecución. Esto puede ser especialmente notable en programas con bucles o procesamiento intensivo.

4. **Portabilidad**: Los programas interpretados suelen ser **más portátiles** que los programas compilados, ya que el intérprete puede ejecutar el mismo código en diferentes plataformas sin necesidad de recompilación.

5. **Flexibilidad**: La interpretación permite una **mayor flexibilidad** en el desarrollo y la depuración de programas, ya que el código puede ser modificado y probado fácilmente sin necesidad de recompilar.

**Python** es un ejemplo de un lenguaje de programación que generalmente se **interpreta** en lugar de compilarse. Cuando ejecutas un script de Python, el intérprete de Python lee el código fuente y lo ejecuta directamente, interpretando cada línea de código y produciendo resultados en tiempo real. Esto permite un desarrollo rápido y una sintaxis clara, pero puede resultar en una menor eficiencia en comparación con los lenguajes compilados.

## interpreter

# lenguaje de programación

Los "scripting languages" (o lenguajes de secuencias de comandos) son lenguajes de programación diseñados para escribir **scripts**, que son programas informáticos simples que ejecutan una serie de comandos o instrucciones en secuencia. Estos lenguajes están optimizados para la escritura rápida y la ejecución eficiente de scripts, lo que los hace ideales para tareas automatizadas, procesamiento de texto, administración de sistemas, prototipado rápido y otras aplicaciones similares.

## scripts

Los scripts son archivos de texto que contienen una secuencia de comandos o instrucciones que el intérprete o el entorno de ejecución del lenguaje de scripting puede ejecutar directamente. Los scripts no requieren un proceso de compilación previo, ya que el intérprete del lenguaje de scripting puede interpretar y ejecutar el código directamente desde el archivo de script.

Algunos ejemplos populares de lenguajes de secuencias de comandos incluyen:

Python: Un lenguaje de programación de alto nivel conocido por su sintaxis clara y legible, ampliamente utilizado en una variedad de aplicaciones, desde desarrollo web y análisis de datos hasta automatización de tareas y scripting de sistemas.

Bash: Un lenguaje de secuencias de comandos comúnmente utilizado en sistemas operativos tipo Unix (como Linux y macOS) para escribir scripts de shell que automatizan tareas de administración del sistema y procesamiento de archivos.

JavaScript: Un lenguaje de programación interpretado comúnmente utilizado en el desarrollo web para crear aplicaciones interactivas y dinámicas en el navegador.

Perl: Un lenguaje de programación versátil y potente utilizado en una amplia gama de aplicaciones, incluyendo procesamiento de texto, extracción de datos, administración de sistemas y desarrollo web.

Los scripts son una forma eficaz de automatizar tareas repetitivas y simplificar procesos complejos, lo que hace que los lenguajes de secuencias de comandos sean herramientas valiosas para los desarrolladores, administradores de sistemas, científicos de datos y otros profesionales de la informática.


# Sintaxis

La sintaxis se refiere a las reglas y estructuras gramaticales que gobiernan cómo se escribe y se estructura el código en un lenguaje de programación específico. 
Es decir, define la forma correcta en que deben combinarse las palabras clave, operadores, variables y otros elementos del lenguaje para formar instrucciones válidas y comprensibles para el ordenador.

En el contexto de la programación, tener una sintaxis correcta es crucial, ya que un error en la sintaxis puede llevar a que el programa no funcione correctamente o incluso a que no se ejecute en absoluto. Los lenguajes de programación tienen reglas específicas de sintaxis que deben seguirse para que el código sea válido y pueda ser interpretado por el compilador o intérprete del lenguaje.

Por ejemplo, en Python, una sintaxis incorrecta puede ser olvidar los dos puntos (:) al definir una función o un bucle, o escribir mal una palabra clave como if o else.

>En resumen, la sintaxis en programación se refiere a las reglas y convenciones que dictan cómo se estructuran y escriben las instrucciones en un lenguaje de programación específico.

## Sintaxis Python

En Python, hay varias reglas de sintaxis que debes tener en cuenta para escribir código correctamente. Algunas de las más importantes incluyen:

**Indentación**: Python utiliza la indentación para delimitar bloques de código en lugar de llaves o palabras clave de finalización como en otros lenguajes. Los bloques de código deben estar indentados con la misma cantidad de espacios o tabulaciones. La convención más común es usar cuatro espacios para cada nivel de indentación.

```python
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")

```

**Comentarios**: Se pueden agregar comentarios al código utilizando el carácter #. Los comentarios son útiles para documentar y explicar el propósito del código.

```python
# Este es un comentario de una sola línea

"""
Este es un comentario
de varias líneas
"""

```

**Variables**: Deben seguir las reglas de nomenclatura de Python, que generalmente significa comenzar con una letra o un guion bajo (_) seguido de letras, números o guiones bajos. Las variables son sensibles a mayúsculas y minúsculas.

```python
mi_variable = 42

```

**Palabras clave**: Python tiene palabras clave reservadas que no pueden ser utilizadas como nombres de variables u otros identificadores. Algunas de estas palabras clave incluyen if, else, for, while, def, import, entre otras.

**Operadores**: Python soporta una variedad de operadores, como operadores aritméticos (+, -, *, /), operadores de comparación (<, >, ==, !=), operadores lógicos (and, or, not), entre otros.

**Estructuras de control**: Python tiene estructuras de control como if, else, elif, for, while, try, except, entre otras, que tienen una sintaxis específica para controlar el flujo del programa.

Estas son solo algunas de las reglas de sintaxis más fundamentales en Python. Es importante tener en cuenta estas reglas mientras escribes código para asegurarte de que sea válido y funcione correctamente.

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