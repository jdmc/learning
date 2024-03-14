
[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# expresion regular / regular expression

En Python, una expresión regular (o regular expression en inglés) es una secuencia de caracteres que define un patrón de búsqueda. Se utilizan principalmente para buscar y manipular cadenas de texto de manera flexible y eficiente. Las expresiones regulares son extremadamente útiles cuando se trabaja con cadenas de texto complejas y se necesitan realizar operaciones como **búsqueda**, **extracción**, **reemplazo** o **validación** de patrones.

Python proporciona un módulo llamado **re** que permite trabajar con expresiones regulares. Este módulo ofrece funciones y métodos para compilar expresiones regulares, buscar coincidencias en cadenas de texto, y realizar operaciones de manipulación de texto basadas en patrones.

Aquí hay un ejemplo básico de cómo usar expresiones regulares en Python para buscar un patrón específico en una cadena de texto:

```python
import re

# Función principal: re.search()
# Patrón: Buscar la palabra "apple" en cualquier parte de la cadena.
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'I have an apple and a banana.'

# Buscar coincidencias utilizando la expresión regular con re.search()
matches = re.search(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')


```
En este ejemplo, la expresión regular r'apple' se compila y luego se utiliza para buscar la palabra "apple" en la cadena de texto. La función re.search() devuelve un objeto Match si se encuentra una coincidencia, de lo contrario, devuelve None. Luego, podemos usar el método group() del objeto Match para obtener la cadena que coincide con el patrón.

## Funciones VS Patrones

Entiendo que puede haber cierta confusión entre los términos "funciones principales" y "tipos de expresiones" en el contexto de expresiones regulares en Python. 

1. Funciones principales (principal functions):     
  En el contexto de expresiones regulares en Python, las "funciones principales" se refieren a las funciones proporcionadas por el módulo **re** que se utilizan para trabajar con expresiones regulares y cadenas de texto. Estas funciones principales incluyen **re.search()** y **re.match()**, que son las funciones principales para buscar patrones en cadenas de texto. Otros ejemplos de funciones principales incluyen **re.findall()**, **re.sub()**, **re.split()**, entre otras. Estas funciones son esenciales para realizar operaciones como búsqueda, extracción, reemplazo y división de cadenas de texto utilizando expresiones regulares.

2. Tipos de expresiones (types of expressions):     
  En el contexto de expresiones regulares, los "tipos de expresiones" se refieren a los **patrones** específicos que se utilizan para buscar coincidencias en las cadenas de texto. Estos patrones están compuestos por una combinación de caracteres literales, metacaracteres, clases de caracteres, cuantificadores, agrupaciones y referencias, entre otros elementos. Los tipos de expresiones varían dependiendo de la complejidad del patrón que se está buscando y de los requisitos específicos del usuario. Por ejemplo, una expresión regular puede ser un patrón simple como **r'apple'**, que busca la palabra "apple" en una cadena de texto, o puede ser un patrón más complejo que incluya múltiples metacaracteres, clases de caracteres y cuantificadores para buscar un patrón más específico.

En resumen, las "funciones principales" se refieren a las funciones proporcionadas por el módulo **re** para trabajar con expresiones regulares, mientras que los "tipos de expresiones" se refieren a los patrones específicos que se utilizan en las funciones principales para buscar coincidencias en las cadenas de texto. Ambos son conceptos fundamentales para comprender y utilizar efectivamente expresiones regulares en Python.

## Funciones principales

En Python, el módulo re proporciona dos funciones principales para buscar patrones en cadenas de texto: re.search() y re.match(). Ambas funciones utilizan expresiones regulares para buscar coincidencias en cadenas de texto, pero difieren ligeramente en su comportamiento. Aquí hay una explicación de cada una:

**re.search(pattern, string)**: Esta función busca en toda la cadena de texto string cualquier ocurrencia del patrón pattern. Si encuentra una coincidencia en cualquier parte de la cadena, devuelve un objeto Match, que contiene la información sobre la primera coincidencia encontrada. Si no se encuentra ninguna coincidencia, devuelve None.

```python
import re

# Función principal: re.search()
# Patrón: Buscar la palabra "apple" en cualquier parte de la cadena.
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'I have an apple and a banana.'

# Buscar coincidencias utilizando la expresión regular con re.search()
matches = re.search(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')


```

En este ejemplo, re.search() encuentra la palabra "apple" en la cadena de texto y devuelve un objeto Match.

**re.match(pattern, string)**: Esta función intenta hacer coincidir el patrón pattern solo al principio de la cadena de texto string. Si encuentra una coincidencia al principio de la cadena, devuelve un objeto Match. Si no hay coincidencia al principio de la cadena, devuelve None.

```python
import re

# Función principal: re.match()
# Patrón: Buscar la palabra "apple" solo al principio de la cadena.
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'apple pie is delicious.'

# Buscar coincidencias utilizando la expresión regular con re.match()
matches = re.match(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')


```
En este ejemplo, re.match() encuentra la palabra "apple" al principio de la cadena de texto y devuelve un objeto Match.

Ambas funciones son útiles para buscar patrones en cadenas de texto, pero la diferencia principal radica en **dónde comienzan a buscar**. re.search() busca en toda la cadena de texto, mientras que re.match() busca solo al principio de la cadena. Dependiendo de sus necesidades, puede optar por utilizar una u otra función.

## Patrones de expresiones regulares

Las expresiones regulares pueden variar en complejidad y funcionalidad dependiendo de las necesidades específicas del usuario. 

Algunos de los tipos comunes de expresiones regulares incluyen:

1. Caracteres Literales:     
  Son caracteres simples que coinciden exactamente con ellos mismos en una cadena de texto. Por ejemplo, la expresión regular "hello" coincidirá exactamente con la cadena "hello".

2. Metacaracteres:     
  Son caracteres especiales que representan clases de caracteres o realizan funciones especiales. Algunos metacaracteres comunes incluyen:

* .: Coincide con cualquier carácter excepto el salto de línea.
* ^: Coincide con el comienzo de una cadena de texto.
* $: Coincide con el final de una cadena de texto.
* \: Se utiliza para escapar metacaracteres o para introducir secuencias especiales como \d, \w, etc.

3. Clases de caracteres:     
  Permiten especificar conjuntos de caracteres que coinciden con un solo carácter en la cadena de texto. Algunos ejemplos incluyen:

* [abc]: Coincide con cualquiera de los caracteres dentro de los corchetes (a, b o c).
* [0-9]: Coincide con cualquier dígito del 0 al 9.
* [^0-9]: Coincide con cualquier carácter que no sea un dígito del 0 al 9.


4. Cuantificadores:     
  Especifican cuántas veces debe aparecer un patrón para que se considere una coincidencia. Algunos ejemplos incluyen:

* *: Coincide con cero o más repeticiones del patrón anterior.
* +: Coincide con una o más repeticiones del patrón anterior.
* ?: Coincide con cero o una repetición del patrón anterior.
* {n}: Coincide exactamente con n repeticiones del patrón anterior.
* {m, n}: Coincide con al menos m y como máximo n repeticiones del patrón anterior.

5. Agrupaciones y referencias:     
  Permiten agrupar partes de una expresión regular para aplicar cuantificadores o realizar operaciones específicas. Además, las referencias hacia atrás (\1, \2, etc.) permiten hacer referencia a grupos previamente definidos dentro de la expresión regular.

Estos son solo algunos ejemplos de los tipos de expresiones regulares disponibles en Python y otros lenguajes de programación. La complejidad y la variedad de las expresiones regulares permiten realizar tareas sofisticadas de búsqueda y manipulación de texto.





[Regular Expressions 101](https://regex101.com/) 

[Regular Expressions r ](https://regexr.com/) 

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 