def convertir_calificaciones(l_calificaciones: tuple) -> tuple:
    # Convierte una tupla de calificaciones en formato string a una tupla de calificaciones en formato float
    return tuple(list(map(lambda calificacion: float(calificacion), l_calificaciones)))

def preguntar_calificaciones():
    # Solicita al usuario ingresar las calificaciones separadas por espacios y devuelve una tupla de calificaciones
    calificaciones = input("Calificaciones separadas por espacio:?")
    return tuple(calificaciones.split())

def preguntar_asignatura() -> dict:
    # Solicita al usuario ingresar el nombre de la asignatura y las calificaciones de los estudiantes
    asignatura = input("Asignatura:?")
    calificaciones = preguntar_calificaciones()

    # Convierte las calificaciones ingresadas a formato numérico (float)
    calificaciones_numerico = convertir_calificaciones(calificaciones)

    # Crea un diccionario con la asignatura como clave y las calificaciones como valor
    asignatura_calificaciones = {
        asignatura: calificaciones_numerico
    }

    return asignatura_calificaciones
    
def cargar_asignaturas(num_asignaturas: int) -> dict:
    # Crea un diccionario para almacenar todas las asignaturas y sus calificaciones
    asignaturas_local = dict() 
    # Itera sobre el número de asignaturas especificado por el usuario
    for _ in range(num_asignaturas):
        # Solicita al usuario ingresar los datos de una asignatura y los agrega al diccionario de asignaturas
        par_asignatura_calificaciones = preguntar_asignatura()
        asignaturas_local.update(par_asignatura_calificaciones)

    return asignaturas_local
