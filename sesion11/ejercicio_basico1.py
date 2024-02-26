"""
Crea una clase llamada Persona que tenga los siguientes atributos: 

• nombre: un atributo para almacenar el nombre de la persona. 
• edad: un atributo para almacenar la edad de la persona. 

1.Agrega un método saludar a la clase Persona que imprima un saludo personalizado con el nombre de la persona. 
2.Crea dos instancias de la clase Persona e inicialízalas con diferentes nombres y edades. 
3.Llama al método saludar para cada instancia de Persona y verifica que se imprima correctamente el saludo.

"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        print(f"Hola, soy {self.__nombre} y tengo {self.__edad} años.")

# Crear dos instancias de Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Llamar al método saludar para cada instancia
persona1.saludar()  # Imprime: Hola, soy Juan y tengo 30 años.
persona2.saludar()  # Imprime: Hola, soy María y tengo 25 años.

""" 
En este ejercicio, se ha creado la clase Persona con los atributos __nombre y __edad, 
y un método saludar que imprime un saludo personalizado con el nombre y la edad de la persona. 

Luego, se crearon dos instancias de la clase Persona con diferentes nombres y edades, 
y se llamó al método saludar para cada instancia para verificar que se imprima correctamente el saludo. """


# Version Ricardo

