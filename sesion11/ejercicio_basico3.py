""" Define una clase llamada Libro con los siguientes atributos privados: 
    
    • __titulo: un atributo para almacenar el título del libro. 
    • __autor: un atributo para almacenar el autor del libro. 
    • __anio_publicacion: un atributo para almacenar el año de publicación del libro. 
    
    1.Utiliza propiedades (getters y setters) para acceder y modificar estos atributos privados. 
    Asegúrate de seguir las convenciones de notación de Python. 
    2.Implementa un método detalles_libro que imprima los detalles del libro, incluyendo título, autor y año de publicación. 
    3.Crea una instancia de la clase Libro e inicialízala con valores para el título, autor y año de publicación. 
    4.Utiliza las propiedades y el método detalles_libro para acceder y mostrar la información del libro.   """  

from libro import Libro
from libreria import Libreria

if __name__ == "__main__":

    quijote = Libro("Don Quijote de la Mancha", "M. Cervantes", "1575")
    historia_interminable = Libro("Historia Interminable", "M. Ende", "1984")

    libreria = Libreria(quijote, historia_interminable)

    print(len(libreria))

    libreria.anyadir_libro(Libro("El mundo azul", "J. Perez", "1991"))
    
    print(len(libreria))

    libreria.anyadir_libro(quijote + historia_interminable)

    print(len(libreria))

    libreria.listar_libros()

    print("_" * 50)

    ultimo_libro_entrado = libreria[-1]
    print(ultimo_libro_entrado.titulo)