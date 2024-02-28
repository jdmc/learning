from vehiculo import Vehiculo
from enum import Enum

class TIPO_CARROCERIA(Enum):
    SEDAN= 1,
    BERLINER = 2,
    SUV = 3,
    TT = 4

class Automovil (Vehiculo):
    def __init__(self,  marca: str, modelo: str, anno: str, tipo_carroceria: TIPO_CARROCERIA):
        super().__init__(marca, modelo, anno)
        self.__tipo_carroceria = tipo_carroceria
        
    def mostrar_informacion (self,):        
        return f"{super().mostrar_informacion()} {self.__tipo_carroceria}"
        
        
    def arrancar(self):
        return f"El coche de la marca {self._marca} esta arrancando....:"