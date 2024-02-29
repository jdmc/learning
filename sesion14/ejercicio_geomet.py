""" 
Figuras Geoniétricas
1. Define una clase base llamada FiguraGeometrica con los siguientes
atributos:
• ladol: longitud del primer lado.
• lado2: longitud del segundo lado.

2. Implementa un método en la clase FiguraGeometrica llamado
calcular_area que imprima un mensaje genérico indicando que se
está calculando el área.

3. Crea dos clases derivadas de FiguraGeometrica:
• Rectangulo: con un atributo adicional lado3 (longitud del tercer
lado).
• Triangulo: con un atributo adicional altura (altura del triángulo).

4. Sobrescribe el método calcular_area en las clases derivadas para
que calcule y muestre el área específica de cada figura geométrica.

5. Crea instancias de Rectangulo y Triangulo con valores específicos
para los lados adicionales.

6. Llama al método calcular_ area para cada instancia y verifica que se
imprima el cálculo del área correspondiente.

Ayuda:
• FiguraGeometrica (Clase Base)
• Atributos:
• ladol
• lado2
• Método:
• calcular area
• Rectangulo (Clase Derivada de FiguraGeometrica)
• Atributos adicionales:
• lado3
• Triangulo (Clase Derivada de FiguraGeometrica)
• Atributos adicionales:
• Altura """

class FiguraGeometrica:
    
    def __init__(self, lado1, lado2) -> None:
        self.__lado1 = lado1
        self.__lado2 = lado2
        
    def calcular_area (self):
        print("calculando area")
        
class Rectangulo(FiguraGeometrica):
        
    def __init__(self, lado1, lado2, lado3):
        super().__init__ (lado1,lado2)
        self.__lado3 = lado3
        
    def calcular_area(self):
        return super().calcular_area()
            
class Triangulo (FiguraGeometrica):
        
    def __init__ (self, lado1, lado2, altura):
        super().__init__ (lado1,lado2)
        self.__altura = altura
        
    def calcular_area(self):
        return super().calcular_area()