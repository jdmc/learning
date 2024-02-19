class Curso:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.alumnos = list()
    
    def matricular(self, *alumnos):
        if alumnos is None : return
        self.alumnos.extend(list(alumnos))
        #self.alumnos.extend([alumno for alumno in alumnos])
        #self.alumnos = self.alumnos + [alumno for alumno in alumnos]
        #self.alumnos = self.alumnos + list(alumnos)

    def matricular_asignaturas(self, *asignaturas: tuple):
        for alumno in self.alumnos:
            alumno.matricular_asignaturas(*asignaturas)

    def listar_alumnos(self):
        print("-" * 25, self.nombre, "-" * 25)
        for alumno in self.alumnos:
            #print(alumno.nombre, ",".join(alumno.asignaturas), sep=":")
            print(alumno.nombre, ",".join([asignatura.nombre for asignatura in alumno.asignaturas]), sep=":")