""" Un módulo en Python es un archivo que contiene un conjunto de definiciones y declaraciones, como:

Funciones: Bloques de código reutilizables que realizan una tarea específica.
Variables: Almacenan datos que pueden ser utilizados por diferentes partes del programa.
Clases: Plantillas para crear objetos con características y comportamientos específicos.
Sentencias ejecutables: Instrucciones que se interpretan y ejecutan por el intérprete de Python.
Los módulos se utilizan para organizar el código en Python y para compartir código entre diferentes programas.

Ventajas de usar módulos:

Reutilización de código: Se puede evitar escribir el mismo código varias veces.
Modularidad: Se puede dividir un programa en partes más pequeñas y manejables.
Organización: Se puede mejorar la legibilidad y la mantenibilidad del código.
Encapsulamiento: Se puede ocultar la implementación de detalles específicos a otras partes del programa.
Cómo usar módulos:

Importar un módulo: Se utiliza la palabra clave import para importar un módulo en otro programa.
Acceder a las definiciones del módulo: Se puede acceder a las funciones, variables, clases y sentencias ejecutables del módulo utilizando el nombre del módulo como prefijo.

***********FROM***************

También existe el uso de from cuando se usa un módulo.
La palabra clave from se utiliza para importar nombres específicos de un módulo.

Ventajas de usar from:

Simplifica el código: No es necesario usar el nombre del módulo como prefijo para acceder a los nombres importados.
Mejora la legibilidad: El código es más fácil de leer y entender.
Desventajas de usar from:

Puede ser confuso: Si se importan muchos nombres del mismo módulo, puede ser difícil recordar qué nombre se refiere a qué.
Puede ocultar la procedencia de los nombres: No es evidente de dónde provienen los nombres importados.

En general, se recomienda usar import cuando se importan varios nombres de un módulo, y usar from cuando solo se importan unos pocos nombres 

 """
from calculadora import sumar, restar, sumar_v2
#import calculadora as calc

def calcular(x: int = 0, y: int = 0, z: int = 0) -> int:
    return x + y + z

def matricular_alumnos(curso: dict,**d_alumnos):
    curso.update(d_alumnos)
    return curso

if __name__ == "__main__":

    alumnos = {
        "111H": "juan",
        "222H": "maria",
        "333H": "jaime"

    }

    #matricular nuevos alumnos
    nuevos_alumnos = {
        "444H": "luis",
        "555H": "silvia",
    }
    print(f"ANTES MAT:{alumnos}")
    alumnos = matricular_alumnos(curso=alumnos,**nuevos_alumnos)
    print(f"DESPUES MAT:{alumnos}")

    print("-" * 50)
    
    #resultado = calc.sumar(10,3)
    resultado = sumar(10,3)
    print(f"Resultado:{resultado}")

    resultado = sumar_v2(10,3,1,1,1,1,1,1,1,1,1)
    print(f"Resultado_sumarv2:{resultado}")

    valores_a_sumar = [2,5,2,8,0]
    resultado = sumar_v2(*valores_a_sumar)

    #resultado = calc.restar(10,3)
    resultado = restar(10,3)
    print(f"Resultado:{resultado}")

    resultado2 = calcular(3)
    print(f"Resultado2:{resultado2}")

