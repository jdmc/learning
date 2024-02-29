from lista_num import ListaNumeros
# ListaOperaciones que herede de ListaNumeros
class ListaOperaciones(ListaNumeros):
    #metodo
    def __init__(self, lista, operacion) -> None:
        # herede de ListaNumeros
        super()__init__(lista)
        # Añade un atributo adicional
        self.__operacion = operacion
        
    # crear metodo según el valor de operacion, realice la operación correspondiente en la lista de números y devuelva el resultado.    
    def realizar_operacion():
        operacion = lista * 2
        return operacion
        
