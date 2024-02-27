from .alumno import Alumno
#CRUD
def matricular(indent: str, nombre: str, apellido: str, curso: int, l_alumnos: list[Alumno]):
    l_alumnos.append(Alumno(indent, nombre, apellido, curso))
    return l_alumnos

def mostrar_alumnos(l_alumnos: list[Alumno]):
    for alumno in l_alumnos:
        print(alumno)