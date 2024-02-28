from animal import Animal

class Granjero():
    
    #constructor
    def __init__(self, animales: list[Animal]) :
        self.__animales = animales
    
    #metodos
    def dar_de_comer(self): 
        for animal in self.__animales:
            print(animal.comer())