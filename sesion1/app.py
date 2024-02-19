data = print("Hola Python") #statement no hay devolucion
print("Data:" + str(data))
n_items = len("Hola") # expression

# bloque de codigo
# estructura condicional

# crear una variable o declaracion de una variable y asignacion de un valor
nota = 4 #entero
a, b, c = 1, 4, 7

print(b)

if nota == 5: # ?? True (expresion booleana)
    print("estas aprobado") # indentacion
else: # sino
    print("seguir preguntando")   # indentacion
    nota = "6.7" # string o cadena

print("Fuera del bloque else")


#tipos de datos
data = 19 # int
print(type(data))

nota = 5
print(type(nota)) # float

nombre = "Amador" # str
print(type(nombre))

nombre = 'Amador' # str
print(type(nombre))

#expresion booleana
# notacion: snake
has_sacado_un_cinco = (nota == 5)
#print(type(nota == 5)) # bool
print(has_sacado_un_cinco) # False / True

# str
""" En Python, "str" es una abreviatura de "cadena de caracteres" o "string" en inglés. 
Es un tipo de dato que se utiliza para representar texto, ya sea una sola letra, una palabra, 
una frase o incluso un conjunto de caracteres más grande.

Por ejemplo, en Python, podemos crear una cadena de caracteres de la siguiente manera:


mensaje = "Hola, mundo!"

En este caso, "Hola, mundo!" es una cadena de caracteres, y la variable mensaje contiene esa cadena.

Las cadenas de caracteres pueden contener cualquier combinación de letras, números, símbolos y espacios. 
También pueden contener caracteres de escape como "\n" para representar saltos de línea o "\t" para representar tabulaciones.

Las cadenas de caracteres en Python son inmutables, lo que significa que no se pueden modificar una vez que se han creado. 
Sin embargo, se pueden manipular y trabajar con ellas utilizando una variedad de métodos y operaciones de cadena proporcionadas por Python.

En resumen, "str" en Python se refiere al tipo de dato que se utiliza para representar y trabajar con texto. """


# funciones embebidas o built-in
longitud_nombre = len(nombre)
print("Este nombre tiene una longitud de " + str(longitud_nombre)) # 6


# cadena_numero = int("hola") imposible conversion
# print(type(cadena_numero))


# int
""" El "int" en Python es una abreviatura de "integer", que en español se traduce como "entero". 
Es un tipo de dato que se utiliza para representar números enteros, es decir, números sin parte decimal.

Por ejemplo, en Python, podemos crear un número entero de la siguiente manera:


numero = 42
En este caso, 42 es un número entero, y la variable numero contiene ese número.

Los números enteros pueden ser positivos, negativos o cero, y pueden ser tan grandes o tan pequeños como lo permita la memoria de la computadora.

Puedes realizar operaciones matemáticas comunes con números enteros en Python, como suma, resta, multiplicación y división. 
Python también proporciona funciones y métodos integrados para trabajar con números enteros, como abs() para obtener el valor absoluto, pow() para calcular potencias y muchos más.

En resumen, "int" en Python se refiere al tipo de dato que se utiliza para representar y trabajar con números enteros. """

#preguntar al usuario
pregunta = "Cuantos anyos tienes?"
respuesta = int(input(pregunta))

print(f"Tienes {respuesta} anyos.")
#print("Tienes {} anyos.".format(respuesta))

if respuesta > 20:
    print("Acceso activado")
else:
    print("Entrada prohibida")
