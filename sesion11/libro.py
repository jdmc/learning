class Libro:

        
        
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
    
    #setter
    
    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor
        
    @autor.setter
    def autor(self, valor):
        self.__autor = valor
        
    @anio.setter
    def anio(self, valor):
        self.__anio = valor
        
        
    def __init__(self, titulo: str, autor: str, anio: str) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def detalles_libro(self):
        return f"{self.titulo} - {self.autor} - {self.anio}"
        
    
    def obtener_titulo(self):
        return self.__titulo
    
    def obtener_autor(self):
        return self.__autor
    
    def obtener_anio(self):
        return self.__anio
