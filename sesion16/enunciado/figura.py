from abc import ABCMeta, abstractmethod

class FiguraGeometrica(metaclass=ABCMeta):
    def nombre(self, nombre):
        self._nombre = nombre 
        
        
    def calcular_area(self, area):
        pass
        
    def calcular_perimetro(self, perimetro):
        pass
        
        