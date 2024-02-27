class Persona:

    #getters
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def edad(self) -> str:
        if self.__edad > 0:
            return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad: int):
        if type(nueva_edad) == int and nueva_edad >= 0:
            self.__edad = nueva_edad
        
        
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        return f"Hola {self.__nombre}"
    


juan = Persona('Juan', 21)
belen = Persona('Belen', 23)

print(juan.saludar())
print(belen.saludar())

juan.edad = -15

print(juan.edad)

print("mas programa...")