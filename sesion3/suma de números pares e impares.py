def separar_pares_impares(lista):
    """
    Función para separar los números pares e impares de una lista dada.
    Retorna dos listas separadas de números pares e impares.
    """
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

def calcular_suma(lista):
    """
    Función para calcular la suma de los elementos en una lista dada.
    Retorna la suma total.
    """
    suma = 0
    for num in lista:
        suma += num
    return suma

def main():
    """
    Función principal del programa (main).
    Una lista vacía llamada "numeros" que se utilizará para almacenar los números enteros ingresados por el usuario (numeros[])
    Solicita al usuario ingresar una lista de números enteros separados por comas (split),
    inicia un bucle infinito que permite al usuario ingresar números hasta que decida finalizar la entrada (while True).
    Se verifica si la entrada del usuario está vacía (strip) (es decir, si el usuario ha presionado Enter sin ingresar ningún número). Si es así, el bucle se rompe y se finaliza la entrada.
    Estos números enteros se agregan a la lista numeros utilizando el método "extend()".
    separa los números pares e impares, calcula sus sumas y los muestra.
    """
    numeros = []
    print("Ingrese números enteros separados por espacios. Presione Enter para finalizar la entrada.")
    while True:
        entrada = input("Ingrese números (o presione Enter para terminar): ")
        if entrada.strip() == "":
            break
        try:
            numeros.extend([int(x) for x in entrada.split(",")])
        except ValueError:
            print("Error: Ingrese solo números enteros separados por comas.")
    
    # Separar los números pares e impares de la lista ingresada
    pares, impares = separar_pares_impares(numeros)
    
    # Calcular la suma de los números pares e impares
    suma_pares = calcular_suma(pares)
    suma_impares = calcular_suma(impares)
    
    # Mostrar los números pares e impares y sus sumas correspondientes
    print("Números pares:", pares)
    print("Números impares:", impares)
    print("Suma de los números pares:", suma_pares)
    print("Suma de los números impares:", suma_impares)

if __name__ == "__main__":
    main()

