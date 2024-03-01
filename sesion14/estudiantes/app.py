from estudiante import Estudiantes
from collections import namedtuple


Estudiante = namedtuple('Estudiante', 'nombre, edad, nota')
#lista con 5 estudiantes
juan = Estudiante('Juan', 20, 8.5)
juan = Estudiante('Juan', 20, 8.5)
juan = Estudiante('Juan', 20, 8.5)
juan = Estudiante('Juan', 20, 8.5)
juan = Estudiante('Juan', 20, 8.5)

class Estudiantes(list):
    pass

# instancias
estudiante = Estudiantes


# modulo random


# nota random
print(random.randint(1, 100))  # Salida: un número aleatorio entre 1 y 100

# edades random
print(random.randint(1, 100))  # Salida: un número aleatorio entre 1 y 100

 


# funcion promedio notas

# funcion mayor nota


# Resultado Print > lista estudiantes | promedio notas | estudiante nota más alta