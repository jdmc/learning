from escuela import Escuela
from curso import Curso
from asignatura import Asignatura
from alumno import Alumno

if __name__ == "__main__":
    pass
    #crear una escuela
    pue = Escuela("PUE", "Fernando") #instanciar el objeto pue a partir de la clase Escuela
    print(pue.nombre)
    print(pue.director)
    
    #crear los cursos de esa escuela y asociarlos a la misma
    #indicacion de ,.o que se podría hacer unificando en escuela todas las acciones (crear y añadir cursos)
    #pue.crear_cursos("PCAP1","PCAP2")

    python_essentials_1 = Curso("PCAP1")
    python_essentials_2 = Curso("PCAP2")
    pue.anyadir_curso(python_essentials_1)
    pue.anyadir_curso(python_essentials_2)

    
    #asignaturas
    mates = Asignatura("Matematicas", 6.8)
    ingles = Asignatura("Ingles", 6.0)
    programacion = Asignatura("Programacion", 7.0)
    


    #crear los alumnos de los cursos de la escuela
    juan = Alumno('Juan Palomo',23,123)
    maria = Alumno('Maria Pelaez', 22, 1234)
    luis = Alumno('Luis Aute',21,12345)
    alicia = Alumno('Alicia Perez', 21, 123456)
    jaime = Alumno('Jaime Urrutia',24,1234567)

    python_essentials_1.matricular(juan, maria, luis)
    python_essentials_2.matricular(alicia, jaime)

    python_essentials_1.matricular_asignaturas(mates, ingles)
    python_essentials_2.matricular_asignaturas(programacion)
    
    #matricularais en python_essentials_2 dos alumnos mas
    #al listar,  que apareciera el nombre del curso

    #listar alumnos actuales
    pue.listar_alumnos()
    

    #asociar los alumnos a las asignaturas