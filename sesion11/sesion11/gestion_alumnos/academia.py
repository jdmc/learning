from gestion_alumnos.curso import Curso

class Academia:

    def __init__(self) -> None:
        self.cursos = dict([(1, Curso(1, 'Luis Garcia')),(2, Curso(2, 'Alicia Perez')), (3, Curso(3, 'Amaia Lopez'))])

    #comportamiento
    def matricular_alumnos(self, numero_curso: int, *alumnos: tuple):
        curso = self.cursos.get(numero_curso)
        if curso:
            curso.alumnos = list(alumnos)
        
    def obtener_curso(self, num_curso) -> Curso:
        return self.cursos.get(num_curso)