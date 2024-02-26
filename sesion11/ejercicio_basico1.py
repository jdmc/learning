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

class Persona:

    #getters
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def edad(self) -> str:
        return self.__edad

    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        return f"Hola {self.__nombre}"
    


juan = Persona('Juan', 21)
belen = Persona('Belen', 23)

print(juan.saludar())
print(belen.saludar())

"""
La elección entre usar print() o return en un método como saludar() de una clase en Python depende del propósito y el contexto en el que estés utilizando el método.

Uso de print(): print() es útil cuando quieres que el método muestre un mensaje directamente en la consola o en algún otro flujo de salida. 
Esto es útil cuando estás interactuando con el programa a través de la línea de comandos o necesitas que la salida sea visible para el usuario.

Uso de return: return es útil cuando quieres que el método devuelva un valor para que pueda ser utilizado en otro lugar del programa. 
Esto es útil cuando necesitas que el resultado del método se pueda usar para realizar alguna operación posterior o para mostrarlo en otra parte de la interfaz de usuario (por ejemplo, en una interfaz gráfica).

En el caso del método saludar(), si solo estás interesado en mostrar un saludo en la consola o en algún flujo de salida, usar print() es apropiado. 
Por otro lado, si deseas utilizar el saludo en otro lugar del programa o necesitas manipularlo de alguna manera, entonces usar return sería más adecuado.

Aquí hay un ejemplo que ilustra cómo se usaría print() y return en el método saludar():


"""