""" Herencia en Python 
1.Define una clase base llamada Vehiculo con los siguientes atributos: 
    •marca: la marca del vehículo. 
    •modelo: el modelo del vehículo. 
    •anno: el año de fabricación del vehículo. 
2.Implementa un método en la clase Vehiculo llamado mostrar_informacion que imprima la marca, el modelo y el año del vehículo. 
3.Crea una clase derivada llamada Automovil que herede de la clase Vehiculo. 
    Agrega un atributo adicional: 
    •tipo_carroceria: el tipo de carrocería del automóvil (por ejemplo, "sedán", "SUV", etc.). 
4.Implementa un método en la clase Automovil llamado arrancar que imprima un mensaje indicando que el automóvil está arrancando. 
5.Crea una instancia de la clase Automovil con información específica de un automóvil, como marca, modelo, año y tipo de carrocería. 
6.Utiliza el método mostrar_informacion de la clase base para mostrar los detalles del automóvil. 
7.Llama al método arrancar para simular el arranque del automóvil. """

class Vehiculo:
    
    def __init__ (self, marca: str, modelo:str, anno:int):
        self.__marca = marca
        self.__modelo = modelo 
        self.__anno = anno