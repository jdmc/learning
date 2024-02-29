from figura import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
        
    def __init__(self, lado1, lado2):
        super().__init__ (lado1, lado2)
        
    def calcular_area(self):
        super.calcular_area()
        area= self.lado1 * self.lado2
        return area