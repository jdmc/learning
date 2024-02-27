class Alumno:
    #datos (atributos, estado)
    def __init__(self, indent: str, nombre: str, apellido: str, curso: int ):
        self.__identificador = indent
        self.__nombre = nombre
        self.__apellido = apellido
        self.__curso = curso
        self.__notas = []

    #getters y setters
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
        

    #comportamiento (responsabilidad)
    def obtener_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"    
    
    def estudiar(self):
        print("Estudiando...")

    def examinar(self):
        print("Examinando...")
    
    #metodo magico
    def __str__(self):
        return f"{self.__nombre} {self.__apellido}"  
        