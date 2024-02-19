#tratamiento de clientes
# DNI, Nombre, Apellidos, CP

# lista de diccionarios
"""
clients = [{
    'dni':'111h',
    'nombre': 'Pedro',
    'apellido': 'Lopez',
    'cp': '08009'
}]
"""
# buscar cliente, eliminar cliente, etc

def crear_cliente(data: dict) -> dict:
    id_cliente = data['dni']
    cliente = {id_cliente: data}
    return cliente

def eliminar_cliente(clave: str, diccio: dict):
    if clave in diccio:
        diccio.pop(clave)
        return diccio

def buscar_cliente(dni_cliente: str, diccio_clientes: dict) -> dict: #devuelve dict. str = cadena
    
    return diccio_clientes.get(dni_cliente) # te busca la clave y te deveulve el valor, si no existe devuelve NONE
    
"""     if dni_cliente not in diccio_clientes: return
    return diccio_clientes [dni_cliente] """


def mostrar_cliente(diccio_cliente: dict):
    if diccio_cliente is not None:
        for dni, _ in diccio_cliente.items():
            #print(cliente ['dni'])
            print(dni)
            
clientes = dict()

if __name__ == "__main__":
    
    data_cliente1 = {
            'dni':'111h',
            'nombre': 'Pedro',
            'apellido': 'Lopez',
            'cp': '08009' 
    }
    data_cliente2 = {
            'dni':'222h',
            'nombre': 'Maria',
            'apellido': 'Lopez',
            'cp': '08009' 
    }
    data_cliente3 = {
            'dni':'333h',
            'nombre': 'Paco',
            'apellido': 'Iglesias',
            'cp': '28009' 
    }
    
    clientes.update(crear_cliente(data_cliente1))
    clientes.update(crear_cliente(data_cliente2))
    clientes.update(crear_cliente(data_cliente3))
    
    #print(f"clientes inicio: {clientes}")
    
    mostrar_cliente(clientes)
    
    clave = '222h'
    clientes = eliminar_cliente(clave, clientes)    
    print(f"clientes eliminado 222h: {clientes}")
    mostrar_cliente(clientes)
    
    cliente = buscar_cliente(input ('DNI a buscar?:'),clientes)
    if cliente:
        print(cliente)
    else:
        print("no exsite")
    
    
    
clientes = {
    '111H': {
                'dni':'111h',
                'nombre': 'Pedro',
                'apellido': 'Lopez',
                'cp': '08009'
    }
}


