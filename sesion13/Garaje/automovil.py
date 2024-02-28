from vehiculo import Vehiculo

class Automovil (Vehiculo):
    def __init__(self,  marca: str, modelo: str, anno: str,   tipo_carroceria: str, arrancar):
        super().__init__(tipo_carroceria)
        self.__tipo_carroceria = tipo_carroceria
        
        
    def arrancar(self):
        return f"El coche de la marca {self.__marca} esta arrancado.:"