from ejercicio_geomet import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
        
    def __init__(self, lado1, lado2, lado3):
        super().__init__ (lado1,lado2)
        self.__lado3 = lado3
        
    def calcular_area(self):
        return super().calcular_area()