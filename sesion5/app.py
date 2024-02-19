#tratamiento de clientes
# DNI, Nombre, Apellido, CP

def crear_cliente(data: dict) -> dict:
    id_cliente = data['dni']
    cliente = {id_cliente: data}
    return cliente

# pop
""" En Python, "pop()" es un método que se utiliza para eliminar y devolver el elemento en una posición específica de una lista. 
Este método toma un índice como argumento y elimina el elemento en esa posición de la lista, luego devuelve ese elemento.

La sintaxis general del método pop() es la siguiente:

elemento_eliminado = lista.pop(indice)

Donde:

lista es la lista de la cual se desea eliminar un elemento.
indice es la posición del elemento que se desea eliminar.
elemento_eliminado es el elemento que se ha eliminado de la lista y se devuelve como resultado del método.

Por ejemplo:

# Definir una lista
mi_lista = [10, 20, 30, 40, 50]

# Eliminar y devolver el elemento en la posición 2
elemento_eliminado = mi_lista.pop(2)

print("Elemento eliminado:", elemento_eliminado)
print("Lista actualizada:", mi_lista)

En este ejemplo, mi_lista.pop(2) eliminará el elemento en la posición 2 de la lista mi_lista, que es 30. 
El método pop() devolverá este elemento, y luego podemos imprimir tanto el elemento eliminado como la lista actualizada después de la eliminación.

Es importante tener en cuenta que pop() modifica la lista original al eliminar el elemento. 
Si se llama a pop() sin especificar un índice, elimina y devuelve el último elemento de la lista por defecto. """

def eliminar_cliente(clave: str, diccio: dict):
    if clave in diccio:
        diccio.pop(clave)
    return diccio
    

""" En Python, "get()" es un método que se utiliza para obtener el valor asociado a una clave específica en un diccionario. 
Este método toma la clave como argumento y devuelve el valor correspondiente si la clave está presente en el diccionario. 
Si la clave no está presente, get() puede devolver un valor predeterminado en lugar de generar un error.

La sintaxis general del método get() es la siguiente:

valor = diccionario.get(clave, valor_predeterminado)

Donde:

diccionario es el diccionario del cual se desea obtener el valor.
clave es la clave cuyo valor se desea obtener.
valor_predeterminado (opcional) es el valor que se devolverá si la clave no está presente en el diccionario. 
Si no se especifica, el valor predeterminado es None.

Por ejemplo:

# Definir un diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener el valor asociado a la clave 'b'
valor_b = mi_diccionario.get('b')
print("Valor de 'b':", valor_b)

mi_diccionario.get('b') 
devolverá 2 porque la clave 'b' está presente en el diccionario y su valor es 2. 

# Obtener el valor asociado a la clave 'd' (que no existe)
# y usar un valor predeterminado
valor_d = mi_diccionario.get('d', 'No encontrado')
print("Valor de 'd':", valor_d)

mi_diccionario.get('d', 'No encontrado') 
devolverá 'No encontrado' porque la clave 'd' no está presente en el diccionario y se ha proporcionado un valor predeterminado. """


def buscar_cliente(dni_cliente: str, d_clientes: dict) -> dict:
    
    """
    if dni_cliente not in d_clientes: return #None
    return d_clientes[dni_cliente]
    """
    return d_clientes.get(dni_cliente) # si no existe, devuelve None



def mostrar_clientes(d_clientes: dict):
    if d_clientes is not None:
        for dni, _ in d_clientes.items():
            #print(cliente['dni'])
            print(dni)

#buscar cliente, eliminar client, etc
clientes = dict()

if __name__ == "__main__":
    
    data_cliente1 = {
        'dni':'111H',
        'nombre': 'Juan',
        'apellido': 'Lopez',
        'cp': '08009'
    }
    data_cliente2 = {
        'dni':'222H',
        'nombre': 'Maria',
        'apellido': 'Lopez',
        'cp': '08009'
    }
    data_cliente3 = {
        'dni':'333H',
        'nombre': 'Belen',
        'apellido': 'Fernandez',
        'cp': '28090'
    }

    clientes.update(crear_cliente(data_cliente1))
    clientes.update(crear_cliente(data_cliente2))
    clientes.update(crear_cliente(data_cliente3))

    mostrar_clientes(clientes)

    clave = '222H'
    clientes = eliminar_cliente(clave, clientes)
    mostrar_clientes(clientes)

    #preguntar al usuario el dni y buscar dicho cliente
    cliente = buscar_cliente(input('DNI a buscar?:'), clientes)
    if cliente: 
        print(list(cliente.items())[1:])
    else:
        print("No existe")


