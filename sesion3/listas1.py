


# valores_booleanos = [] #lista vacia
valores_booleanos = [True, True, False, True, True, False] 

numero_trues = 0
numero_falses = 0
# numero_trues, numero_falses = 0, 0

""" for valor_booleano in valores_booleanos:
    if valor_booleano == True:
        numero_trues = numero_trues + 1
    elif valor_booleano == False:
        numero_falses = numero_falses + 1
 """
for valor_booleano in valores_booleanos:
    numero_trues = numero_trues + 1 if valor_booleano == True else numero_trues   
    numero_falses = numero_falses + 1 if valor_booleano == False else numero_falses 
    print(numero_trues, numero_falses)  

print(f"Numero de trues:{numero_trues}", f"Numero de falses:{numero_falses}", sep=" --- ")

#programacion = ["python", "Java", "Kotlin", "Typescript", "C#"]

def crear_data():
    program = list() #variable local
    #anyadir items  a la lista
    program.append("Python")
    program.append("JAVA")
    program.append("Kotlin")
    program.append("TS")
    program.append("C#")
    program.append("java")


    return program

def eliminar_duplicados(lista_lenguajes):
    lista_sin_duplicados = [] #nueva lista vacia
    for lenguaje in lista_lenguajes:
        
        if lenguaje in lista_sin_duplicados:
            continue
        lista_sin_duplicados.append(lenguaje)
        
        """
        if lenguaje not in lista_sin_duplicados:
            lista_sin_duplicados.append(lenguaje)
        """
    
    return lista_sin_duplicados

"""
Pedir un lenguaje al usuario
evitando que se produzca en la lista programacion
duplicidades
"""

#definicion de una funcion
def listar_lenguajes(lista_lenguajes):
    for lenguaje in lista_lenguajes:
        print(lenguaje)  
    print("-" * 60)

def normalizar_datos(lista_lenguajes):
    #convertir todos los lenguajes a minuscula
    lista_lenguajes_normalizada = list() #variable local
    for lenguaje in lista_lenguajes:
        lista_lenguajes_normalizada.append(lenguaje.lower())  

    return lista_lenguajes_normalizada 

#cargar datos
programacion = crear_data() #invocacion

#listar_lenguajes(programacion) #invocacion

programacion_normalizada = normalizar_datos(programacion) #invocacion y retorno

#programacion_normalizada = normalizar_datos(eliminar_duplicados(programacion)) #invocacion y retorno


listar_lenguajes(programacion_normalizada)

programacion_normalizada_sin_duplicados = eliminar_duplicados(programacion_normalizada)
#programacion_normalizada_sin_duplicados = eliminar_duplicados(normalizar_datos(crear_data()))

listar_lenguajes(programacion_normalizada_sin_duplicados)

lenguaje = input("Lenguaje?:")
if programacion_normalizada_sin_duplicados != None:
    if type(programacion_normalizada_sin_duplicados) == list:
        if lenguaje != None and lenguaje != "":
            programacion_normalizada_sin_duplicados.append(lenguaje.lower()) if lenguaje.lower() not in programacion_normalizada_sin_duplicados else None # None equivale a nop (no operation) 
            #lenguaje not in programacion and programacion.append(lenguaje) 
            
#despues
listar_lenguajes(programacion_normalizada_sin_duplicados)        
   
            







