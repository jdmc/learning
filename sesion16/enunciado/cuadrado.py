from figura import FiguraGeometrica

class cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)
        