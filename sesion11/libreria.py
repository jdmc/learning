from libro import Libro

class Libreria:

    def __init__(self, *libros: tuple) -> None:
        self.__libros = list()
    
    def anyadir_libro(self, libro: Libro):
        self.__libros.append(libro)

    def __len__(self):
        return len(self.__libros)