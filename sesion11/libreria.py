from libro import Libro
from libreria import Libreria

if __name__ == "__main__":

    quijote = Libro("Don Quijote de la Mancha", "M. Cervantes", "1575")
    historia_interminable = Libro("Historia Interminable", "M. Ende", "1984")

    libreria = Libreria(quijote, historia_interminable)

    print(len(libreria))

    libreria.anyadir_libro(Libro("El mundo azul", "J. Perez", "1991"))
    
    print(len(libreria))