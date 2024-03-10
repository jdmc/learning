# Lista original
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizando comprensión de listas para filtrar los números pares
numeros_pares = [num for num in numeros if num % 2 == 0]

# Imprimiendo la lista de números pares
print("Números pares:", numeros_pares)


# Lista original
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utiliza la comprensión de listas para filtrar los números impares

numeros_impares = [impares for impares in numeros if impares % 2 != 0]

print ("*" * 50)

print("Números impares:", numeros_impares)

# Lista original
palabras = ["python", "java", "javascript", "c", "ruby", "swift", "html", "css"]

# Utiliza la comprensión de listas para filtrar las palabras con más de 5 letras

palabra_larga = [px for px in palabras if len(px) > 5]

print ("#" * 50)

print ("La palabra con más de 5 letras son:", palabra_larga)

# Lista original
numeros = [10, 20, 30, 40, 50, 60, 70]

# Utiliza la comprensión de listas para filtrar los números mayores que el promedio 280/7 = 40
n_mayor = [ num_x for num_x in numeros if num_x > 40]

print ("-" * 50)
print ("Número mas de 40 son:", n_mayor)

# Lista original
palabras = ["python", "apple", "banana", "orange", "kiwi", "avocado", "grape"]

# Utiliza la comprensión de listas para filtrar las palabras que comienzan con "a"

palabra_a = [ a for a in palabras if a[0 == a] ]

print ("+" * 50)

print("Palabras empiezan con A: ", palabra_a )

