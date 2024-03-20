def separar (texto):
    palabras = texto.split()
    return palabras
    

def cadena (lista):
    lista_palabra = ",".join(lista)
    return lista_palabra

def combo_eliminar (texto, palabras):
    for palabra in palabras:
        while palabra in texto:
            texto = texto.replace(palabra, " ")
        return texto
    
# Outcome 1 funcion que devuelve una lista de palabras
ejemplo1 ="Esto es una cadena de texto"

palabras_split = separar(ejemplo1)
print(palabras_split)
print("*" * 50)    

# Outcome 2 funcion que devuelve una cadena de palabras
ejemplo2 =["Esto, es, una, lista, de, palabras"]

palabras_join = cadena(ejemplo2)
print(palabras_join)
print("*" * 50)

# Outcome 3 funcion que devuelve una cadena nueva de palabras
texto1 = "Hola mundo Python, mundo Python"
palabras1 = ["mundo", "Python"]
nuevo_texto1 = combo_eliminar(texto1, palabras1)

texto2 = "Este es un ejemplo con palabras"
palabras2 = ["es", "ejemplo"]
nuevo_texto2 = combo_eliminar(texto2, palabras2)

print(f"Cadena original: '{texto1}'")
print(f"Palabras a eliminar: {palabras1}")
print(f"Nueva cadena: '{nuevo_texto1}'")

print()

print(f"Cadena original: '{texto2}'")
print(f"Palabras a eliminar: {palabras2}")
print(f"Nueva cadena: '{nuevo_texto2}'")
