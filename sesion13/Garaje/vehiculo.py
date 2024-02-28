class Vehiculo:
    
    def __init__ (self, marca: str, modelo:str, anno:int):
        self._marca = marca
        self.__modelo = modelo 
        self.__anno = anno
        
    def mostrar_informacion (self,):        
        return f"{self._marca} -- {self.__modelo} -- {self.__anno}"