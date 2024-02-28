""" 1.Define una clase llamada Persona con los siguientes atributos privados: 
    • __nombre: un atributo para almacenar el nombre de la persona. 
    • __edad: un atributo para almacenar la edad de la persona. 
2.Implementa el método mágico __str__ para que al imprimir una instancia de Persona, muestre una representación legible del objeto (por ejemplo, "Nombre: [nombre], Edad: [edad]"). 
3.Implementa el método mágico __add__ para que, al sumar dos instancias de Persona, devuelva una nueva instancia con la suma de las edades y el nombre concatenado. 
4.Crea dos instancias de la clase Persona e inicialízalas con diferentes nombres y edades. 
5.Imprime cada instancia para verificar el funcionamiento del método __str__. 6.Suma las dos instancias utilizando el operador + y muestra el resultado. """


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    

@property