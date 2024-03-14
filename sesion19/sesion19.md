
[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# expresion regular / Regular expression

En Python, una expresión regular (o regular expression en inglés) es una secuencia de caracteres que define un patrón de búsqueda. Se utilizan principalmente para buscar y manipular cadenas de texto de manera flexible y eficiente. Las expresiones regulares son extremadamente útiles cuando se trabaja con cadenas de texto complejas y se necesitan realizar operaciones como búsqueda, extracción, reemplazo o validación de patrones.

Python proporciona un módulo llamado re que permite trabajar con expresiones regulares. Este módulo ofrece funciones y métodos para compilar expresiones regulares, buscar coincidencias en cadenas de texto, y realizar operaciones de manipulación de texto basadas en patrones.

Aquí hay un ejemplo básico de cómo usar expresiones regulares en Python para buscar un patrón específico en una cadena de texto:

```python
import re

# Definir la expresión regular
pattern = r'apple'

# Cadena de texto en la que se realizará la búsqueda
text = 'I have an apple and a banana.'

# Buscar coincidencias utilizando la expresión regular
matches = re.search(pattern, text)

if matches:
    print('Encontrado:', matches.group())
else:
    print('No encontrado')

```
En este ejemplo, la expresión regular r'apple' se compila y luego se utiliza para buscar la palabra "apple" en la cadena de texto. La función re.search() devuelve un objeto Match si se encuentra una coincidencia, de lo contrario, devuelve None. Luego, podemos usar el método group() del objeto Match para obtener la cadena que coincide con el patrón.


[Regular Expressions](https://regex101.com/) 

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 