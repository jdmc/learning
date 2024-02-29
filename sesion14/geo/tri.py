class Triangulo (FiguraGeometrica):
        
    def __init__ (self, lado1, lado2, altura):
        super().__init__ (lado1,lado2)
        self.__altura = altura
        
    def calcular_area(self):
        return super().calcular_area()