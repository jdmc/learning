from rectangulo import Rectangulo
from triangulo import Triangulo
from figura_geometrica import Figura_Geometrica


triangulo = Triangulo(2,3,1,2)
rectangulo = Rectangulo(2,5)

figuras: list[Figura_Geometrica] = list()

figuras.extend([triangulo, rectangulo])

for figura in figuras:
    print(figura.calcular_area())

#help(triangulo)

print(triangulo.__dict__)

