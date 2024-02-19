""" El bucle while en Python es una estructura de control que se utiliza para ejecutar un bloque de código repetidamente mientras se cumpla una condición.

Sintaxis:

while condicion:
  bloque_de_codigo

Explicación:

while: Indica el inicio del bucle.
condicion: Es una expresión booleana que determina si el bucle se ejecuta o no.
bloque_de_codigo: Es el conjunto de instrucciones que se ejecuta si la condición es verdadera.

Ejemplo:

numero = 1

while numero <= 5:
  print(numero)
  numero += 1

En este ejemplo, el bucle while se ejecuta cinco veces, ya que la condición numero <= 5 es verdadera para los valores de numero entre 1 y 5. 
En cada iteración, se imprime el valor de numero y luego se incrementa en 1.

Bucle infinito:

Si la condición del bucle while siempre es verdadera, el bucle se ejecutará infinitamente.

Ejemplo:

while True:
  print("Hola")

Este código imprimirá "Hola" infinitamente hasta que se interrumpa manualmente.

Uso del break:

La palabra clave break se puede usar para salir de un bucle while antes de que se cumpla la condición.

Ejemplo:

numero = 1

while True:
  print(numero)
  if numero == 5:
    break
  numero += 1

Este código imprimirá los números del 1 al 5 y luego saldrá del bucle while.

Uso del continue:

La palabra clave continue se puede usar para omitir el resto del cuerpo del bucle y pasar a la siguiente iteración.

Ejemplo:

numero = 1

while numero <= 10:
  if numero % 2 == 0:
    continue
  print(numero)
  numero += 1

Este código solo imprimirá los números impares del 1 al 9.

El bucle while es una herramienta poderosa para ejecutar un bloque de código repetidamente mientras se cumpla una condición. """


contador = 1
total = 0


while contador <= 3 or total <= 10:
    print(f"Contador:{contador}")
    print(f"Total:{total}")
    total += contador
    contador += 1

print("-" * 50)

contador = 1
total = 0


while contador <= 3 and total <= 10:
    print(f"Contador:{contador}")
    print(f"Total:{total}")
    total += contador
    contador += 1


i = 0
lista = [1,2,3,4,5]
while i < 10 and i < len(lista):
    
    if lista[i] > 4:
        print(f"i:{i}")
        #break
        continue
    
    i += 1
