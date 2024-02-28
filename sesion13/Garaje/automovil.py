from vehiculo import Vehiculo

class Automovil (Vehiculo):
    def __init__(self,  marca: str, modelo: str, anno: str, tipo_carroceria: str):
        super().__init__(marca, modelo, anno)
        self.__tipo_carroceria = tipo_carroceria
        
        
    def arrancar(self):
        return f"El coche de la marca {self.__marca} esta arrancando....:"