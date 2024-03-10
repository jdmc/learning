# Lista de tuplas (nombre, edad)
personas = [("Juan", 30), ("María", 25), ("Carlos", 35), ("Ana", 28)]

# Crea un diccionario donde las claves sean los nombres y los valores sean las edades
mi_dict = dict(personas)

print(mi_dict)

print("@" *50)

# Lista de nombres
nombres = ["Juan", "María", "Carlos", "Ana", "Juan", "María", "Juan", "Carlos", "María"]

# Crea un diccionario donde las claves sean los nombres y los valores sean la cantidad de veces que aparece cada nombre

contar_nombres= {}

for clave in nombres: 
    if clave in contar_nombres:
        contar_nombres[clave] += 1
    else: 
        contar_nombres[clave] = 1

print (contar_nombres)

# Lista de nombres de frutas
frutas = ["Manzana", "Banana", "Naranja", "Pera"]

# Lista de precios correspondientes
precios = [2.50, 1.20, 1.80, 2.00]

# Crea un diccionario donde las claves sean los nombres de las frutas y los valores sean los precios de cada fruta
dict_conjunto = {}

for i in range(len(frutas)):
    fruta = frutas[i]
    precio = precios[i]
    dict_conjunto[fruta] = precio

print("&" * 50)
print(dict_conjunto)


# Lista de palabras
palabras = ["python", "es", "un", "lenguaje", "de", "programacion", "es", "muy", "potente", "y", "versatil", "python"]

# Crea un diccionario donde las claves sean las palabras y los valores sean la cantidad de veces que aparece cada palabra

dict_palabra = {}

for palabra in palabras:
    if palabra in dict_palabra:
        dict_palabra[palabra] +=1
    else:
        dict_palabra[palabra] = 1
    
print("#" * 50)   
print(dict_palabra)

# Lista de números
numeros = [5, 2, 3, 2, 5, 1, 3, 4, 5, 2]

# Crea un diccionario donde las claves sean los números y los valores sean una lista de índices donde aparece cada número en la lista original
lista_dict = {}

for indix in range(len(numeros)): # Iterar sobre los índices de la lista
    num = numeros[indix]
    if num in lista_dict:
        lista_dict[num].append(indix)  # Si el número ya está en el diccionario, agrega el índice actual a su lista de índices
    else:
        lista_dict[num] = [indix] # Si el número no está en el diccionario, crea una nueva entrada con el número como clave y una lista que contenga el índice actual como valor
 
print("++" * 50)          
print(lista_dict)

    