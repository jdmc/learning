En programación, una variable es un contenedor que se utiliza para almacenar y manipular datos en un programa.   
Cada variable tiene un nombre único que se utiliza para hacer referencia a ella, y puede contener un valor que puede cambiar durante la ejecución del programa.  

 Python ofrece "cajas" (contenedores) especiales para este propósito, estas cajas son llamadas variables - el nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.

Las variables se utilizan para almacenar diferentes tipos de datos, como números, texto, listas, objetos, etc.  
Al definir una variable, se reserva un espacio en la memoria de la computadora para almacenar el valor asociado a esa variable.

### ¿Cuáles son los componentes o elementos de una variable en Python?

* Un nombre.
* Un valor (el contenido del contenedor).

Por ejemplo, en Python, puedes definir una variable de la siguiente manera:

```python 

nombre = "Juan"

``` 

En este ejemplo, nombre es el nombre de la variable, y "Juan" es el valor asignado a esa variable.   
Puedes luego utilizar esa variable en el programa para acceder al valor almacenado en ella o para realizar operaciones con ese valor.

Es importante recordar que las variables tienen un ámbito (scope) en el que son válidas. Esto significa que una variable puede estar disponible solo dentro de ciertas partes del programa, como una función o un bloque de código específico. La forma en que se definen y utilizan las variables puede variar dependiendo del lenguaje de programación que estés utilizando.

PEP 8 -- Style Guide for Python Code recomienda la siguiente convención de nomenclatura para variables y funciones en Python:

* Los nombres de las variables deben estar en minúsculas, con palabras separadas por guiones bajos para mejorar la legibilidad (por ejemplo: var, mi_variable).
* Los nombres de las funciones siguen la misma convención que los nombres de las variables (por ejemplo: fun, mi_función).
* También es posible usar letras mixtas (por ejemplo: miVariable), pero solo en contextos donde ese ya es el estilo predominante, para mantener la compatibilidad retroactiva con la convención adoptada.

# Palabras clave

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Son llamadas palabras clave o (mejor dicho) palabras reservadas. Son reservadas porque no se deben utilizar como nombres: ni para variables, ni para funciones, ni para cualquier otra cosa que se desee crear.

# Puntos Clave

1. Una variable es una ubicación nombrada reservada para almacenar valores en la memoria. Una variable es creada o inicializada automáticamente cuando se le asigna un valor por primera vez. (2.1.4.1)

2. Cada variable debe de tener un nombre único - un identificador. Un nombre válido debe ser aquel que no contiene espacios, debe comenzar con un guion bajo (_), o una letra, y no puede ser una palabra reservada de Python. El primer carácter puede estar seguido de guiones bajos, letras, y dígitos. Las variables en Python son sensibles a mayúsculas y minúsculas. (2.1.4.1)

3. Python es un lenguaje de tipo dinámico, lo que significa que no se necesita declarar variables en él. (2.1.4.3) Para asignar valores a las variables, se utiliza simplemente el operador de asignación, es decir el signo de igual (=) por ejemplo, var = 1.

4. También es posible utilizar operadores de asignación compuesta (operadores abreviados) para modificar los valores asignados a las variables, por ejemplo, var += 1, or var /= 5 * 2. (2.1.4.8)

5. Se les puede asignar valores nuevos a variables ya existentes utilizando el operador de asignación o un operador abreviado, por ejemplo (2.1.4.5):

```python
var = 2
print(var)

var = 3
print(var)

var += 1
print(var)
```

6. Se puede combinar texto con variables empleado el operador +, y utilizar la función print() para mostrar o imprimir los resultados, por ejemplo: (2.1.4.4)
```python
var = "007"
print("Agente " + var)
```


