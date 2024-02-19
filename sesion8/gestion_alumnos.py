# Operaciones CRUD >> Create / Read / Update / Delete


def matricular(alumno: tuple, l_alumnos: list):
    """ sirve para añadir un nuevo alumno al curso""" #docstring
    if l_alumnos is not None and alumno is not None:
        l_alumnos.append(alumno)
    return l_alumnos

def dar_de_baja(alumno: tuple, l_alumnos: list) -> list:
    return [al for al in l_alumnos if al != alumno]
    #return list(filter(lambda al: al != alumno, l_alumnos))


def obtener_alumnos(l_alumnos: list) -> str:
    return ", ".join([" ".join(alumno) for alumno in l_alumnos])

def buscar_indice(alumno: tuple, l_alumnos: list) -> int:
    posicion_alumno = None
    for index, al in enumerate(l_alumnos):
        if al == alumno:
            posicion_alumno = index  
    return posicion_alumno

def modificar(alumno: tuple, alumno_modificado: tuple, l_alumnos: list):
    posicion = buscar_indice(alumno, l_alumnos)
    if posicion is not None:
        l_alumnos[posicion] = alumno_modificado    
    
    return l_alumnos

"""     for index, alum in enumerate(l_alumnos): # buscar en la tupla
        if alum == alumno:
            l_alumnos[index] = alumno_update    
    return l_alumnos """


