from gestion_alumnos import matricular, modificar, obtener_alumnos, dar_de_baja
from ficheros import leer_data, escribir_data
import transformers as trans

def mostrar_alumnos(l_alumnos: list):
    for alumno in l_alumnos:
        print(alumno)

if __name__ == "__main__":
    nombre_alumnos = leer_data('alumnos.txt')
    mostrar_alumnos(nombre_alumnos)

    #crear una lista de tuplas formadas por el nombre y el apellido
    #['a b', 'c d', 'e f'] -> [('a','b'),('c','d'),('e','f')]
    alumnos = trans.transformar_data(nombre_alumnos)

    #print(f"ANTES de MAT:{alumnos}")
    alumnos = matricular(('Fabio','Scanferla'), alumnos)
    #print(f"DESPUES de MAT:{alumnos}")

    alumnos = modificar(('Luis','Albert'),('Luis','Alberto'), alumnos)
    #print(f"DESPUES de MODI:{alumnos}")

    alumnos = dar_de_baja(('Marta', 'Gomez'), alumnos)

    alumnos_dump = obtener_alumnos(alumnos)



    #dump de datos de alumnos sobre un fichero llamado alumnos_out.txt ubicado en el directorio data
    escribir_data('alumnos_out.txt', alumnos_dump)        




    

    

    


    