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



