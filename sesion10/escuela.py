from curso import Curso

class Escuela:
    #constructor
    def __init__(self, nombre:str, director: str):
        self.nombre = nombre
        self.director = director
        self.cursos = list()
    
    def anyadir_curso(self, curso:Curso):
        self.cursos.append(curso)

    def listar_alumnos(self):
        #llamada delegada
        for curso in self.cursos:
            curso.listar_alumnos()
            
    
     # >> Escuela >>> crear los cursos de esa escuela y asociarlos a la misma
     
    # pue.crear_cursos("PCAP1","PCAP2")
    

    #  >> Escuela >>> asignaturas >>pasame la info
    
    #  >> Escuela >>> crear los alumnos de los cursos de la escuela >>pasame la info
    
    #  >> Escuela >>> Matricular