def separar (texto):
    palabras = texto.split()
    return palabras
    

def cadena (lista):
    lista_palabra = lista.join(",")
    return lista_palabra

def combo (texto):
    pass
    

ejemplo1 ="Esto es una cadena de texto"

palabras_split = separar(ejemplo1)
print(palabras_split)    


ejemplo2 =["Esto, es, una, lista, de, palabras"]

palabras_join = cadena(ejemplo2)
print(palabras_join)
