""" Listas en Python

Las listas en Python son un tipo de dato que se utiliza para almacenar una colección ordenada y mutable de elementos.

Las listas se definen entre corchetes y los elementos se separan por comas.

mi_lista = ["Hola", 1, True]

En este ejemplo, se crea una lista con tres elementos: una cadena, un número entero y un valor booleano.

Las listas son muy versátiles y se pueden usar para almacenar cualquier tipo de dato, incluso otras listas.

Las listas son mutables, lo que significa que se pueden modificar los elementos de una lista después de que se ha creado.

Se puede agregar, eliminar o modificar elementos de una lista.

Las listas son una herramienta poderosa para organizar y almacenar datos en Python.

Aquí hay algunos ejemplos de cómo se pueden usar las listas:

Almacenar una lista de nombres.
Almacenar una lista de números.
Almacenar una lista de tareas.

Las listas son una herramienta fundamental para el desarrollo de aplicaciones en Python. """


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


"""
** Append en Python

append() es un método que se utiliza para agregar un elemento al final de una lista en Python.

El método append() toma un solo argumento, que es el elemento que se desea agregar a la lista.

Ejemplo:

*****************************

mi_lista = ["Hola", 1, True]

mi_lista.append("nuevo elemento")

print(mi_lista)

**************************
 En este ejemplo, se agrega el elemento "nuevo elemento" al final de la lista mi_lista. 

La lista final será ["Hola", 1, True, "nuevo elemento"].

El método append() es una forma sencilla de agregar elementos a una lista.

Es importante tener en cuenta que el método append() no devuelve ningún valor.

Aquí hay algunos ejemplos adicionales de cómo se puede usar el método append():

Agregar un número al final de una lista de números.
Agregar una cadena al final de una lista de cadenas.
Agregar una lista al final de una lista de listas.

El método append() es una herramienta útil para trabajar con listas en Python. """


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
   
            







