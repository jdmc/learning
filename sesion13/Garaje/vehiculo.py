class Vehiculo:
    
    def __init__ (self, marca: str, modelo:str, anno:int):
        self.__marca = marca
        self.__modelo = modelo 
        self.__anno = anno
        
    def mostrar_informacion (self,):        
        return f"{self.__marca} -- {self.__modelo} -- {self.__anno})"