""" En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
Si es par, evalúa un nuevo c0 como c0 Ã· 2.
De lo contrario, si es impar, evalúe un nuevo  c0  como 3 Ã c0 + 1.
Si c0 â  1, salta al punto 2.
La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

Por supuesto, es una tarea extremadamente compleja usar una computadora para probar 
la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), 
pero puede usar Python para verificar algunos números individuales. 
Tal vez incluso encuentres el que refutaría la hipótesis.

Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. 
También queremos que cuente los pasos necesarios para lograr el objetivo. 
Tu código también debe mostrar todos los valores intermedios de c0.

Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito. """

def collatz_conjecture(n):
    steps = 0
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    print(1)  # Imprime el último valor de c0
    return steps

# Solicitar al usuario que ingrese un número natural
while True:
    try:
        number = int(input("Ingresa un número natural (entero positivo diferente de cero): "))
        if number <= 0:
            print("Por favor, ingresa un número entero positivo diferente de cero.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

steps_needed = collatz_conjecture(number)
print(f"Se necesitaron {steps_needed} pasos para alcanzar 1.")



""" La conjetura de Collatz, también conocida como conjetura de Syracuse o conjetura 3x + 1, 
es una hipótesis matemática que fue propuesta por el matemático Lothar Collatz en 1937. 

La conjetura establece lo siguiente:

Comenzamos con cualquier número entero positivo (también se incluye el cero).

Si el número es par, lo dividimos por 2.
Si el número es impar, lo multiplicamos por 3 y luego sumamos 1.
Repetimos el proceso con el nuevo número obtenido.
La conjetura sugiere que sin importar cuál sea el número inicial, eventualmente alcanzaremos el número 1.

Por ejemplo, si comenzamos con el número 6, seguimos estos pasos:

1. Comenzamos con 6.
2. Como 6 es par, lo dividimos por 2, lo que nos da 3.
3. Como 3 es impar, lo multiplicamos por 3 y sumamos 1, lo que nos da 10.
4. 10 es par, lo dividimos por 2, lo que nos da 5.
5. 5 es impar, lo multiplicamos por 3 y sumamos 1, lo que nos da 16.
6. 16 es par, lo dividimos por 2, lo que nos da 8.
7. 8 es par, lo dividimos por 2, lo que nos da 4.
8. 4 es par, lo dividimos por 2, lo que nos da 2.
9. 2 es par, lo dividimos por 2, lo que nos da 1.
Y ahora hemos alcanzado el número 1. Según la conjetura de Collatz, sin importar con qué número comencemos, eventualmente llegaremos al número 1. """