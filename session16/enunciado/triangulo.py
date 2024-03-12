from figura import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3, altura):
        super().__init__(lado1, lado2)
        self.altura = altura
        self.lado3 = lado3