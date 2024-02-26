""" 

Define una clase llamada Libro con los siguientes atributos privados: 
    
    • __titulo: un atributo para almacenar el título del libro. 
    • __autor: un atributo para almacenar el autor del libro. 
    • __anio_publicacion: un atributo para almacenar el año de publicación del libro. 
    
    1.Utiliza propiedades (getters y setters) para acceder y modificar estos atributos privados. 
    Asegúrate de seguir las convenciones de notación de Python. 
    2.Implementa un método detalles_libro que imprima los detalles del libro, incluyendo título, autor y año de publicación. 
    3.Crea una instancia de la clase Libro e inicialízala con valores para el título, autor y año de publicación. 
    4.Utiliza las propiedades y el método detalles_libro para acceder y mostrar la información del libro.
    
     """
     
class Libro:
    def __init__(self, titulo: str, autor: str, anio: str) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        
        
    #getters + setters 
    
    #getter    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def anio(self):
        return self.__anio
    
    #getter
    
    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor
        
    @autor.setter
    def autor(self, valor):
        self.__autor = valor
        
    @titulo.setter
    def anio(self, valor):
        self.__anio = valor
    
    def obtener_titulo(self):
        return self.__titulo
    
    def obtener_autor(self):
        return self.__autor
    
    def obtener_anio(self):
        return self.__anio
