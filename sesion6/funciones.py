""" Funciones en Python:
Las funciones en Python son bloques de código reutilizables que se utilizan para realizar tareas específicas. Permiten organizar el código en unidades más pequeñas y manejables, lo que facilita su lectura, comprensión y mantenimiento.

Partes de una función:

Nombre: Identificador único que se le da a la función.
Parámetros: Valores que se pueden pasar a la función cuando se llama.
Código: Instrucciones que se ejecutan cuando se llama a la función.
Valor de retorno: Valor que la función devuelve al final de su ejecución. """

""" 
Cuándo usar funciones:

Cuando necesitas realizar una tarea específica varias veces en el código.
Cuando quieres dividir el código en partes más pequeñas y manejables.
Cuando quieres mejorar la legibilidad del código.

Ventajas de usar funciones:

Reutilización: Se pueden usar una y otra vez en diferentes partes del código.
Modularidad: Permiten dividir el código en partes más pequeñas y manejables.
Legibilidad: Hacen que el código sea más fácil de leer y entender.
Mantenimiento: Facilitan la detección y corrección de errores. """



from calculadora import sumar, restar, sumar_v2
# from calculadora import * >> importar todo con "*"
#import calculadora as calc >> otra forma de importar

def calcular(x: int = 0, y: int = 0, z: int = 0) -> int:
    return x + y + z

def matricular_alumnos(curso: dict, **d_alumnos ): #** = condicionaros / * = tupla
    curso.update(d_alumnos)
    return curso

if __name__ == "__main__":
    
    alumnos = {
        "111h": ("juan", 19),
        "222h": ("maria", 22),
        "333h": ("jaime", 32),
    }
    
    #matricular nuevos alumnos
    nuevos_alumnos = {
        "444H": "luis",
        "555H": "silvia",
    }
    print(f"ANTES MAT:{alumnos}")
    alumnos = matricular_alumnos(curso=alumnos,**nuevos_alumnos) #** descomponer, lo rompe en pares
    print(f"DESPUES MAT:{alumnos}")

    print("-" * 50)
    
    #resultado = calc.sumar(10,3)
    resultado = sumar(10,3)
    print(f"Resultado:{resultado}")

    resultado = sumar_v2(10,3,1,1,1,1,1,1,1,1,1)
    print(f"Resultado_sumarv2:{resultado}")

    #resultado = calc.restar(10,3)
    resultado = restar(10,3)
    print(f"Resultado:{resultado}")

    resultado2 = calcular(3)
    print(f"Resultado2:{resultado2}")

