""" Objetivos:
1. Permitir al usuario ingresar múltiples asignaturas y las calificaciones
correspondientes de los estudiantes.
2. Calcular el promedio de calificaciones para cada asignatura.
3. Mostrar el promedio de calificaciones por asignatura. """



""" 
Ayuda:
1. Ingreso y Almacenamiento de Datos: Utiliza un bucle while para
permitir al usuario ingresar asignaturas y sus calificaciones hasta que
decidan salir. Considera usar un diccionario para almacenar el nombre
de la asignatura como clave y las calificaciones (en una tupla) como
valor.
2. Conversión de Calificaciones a Tupla: Las calificaciones ingresadas por
el usuario serán una cadena de texto que necesitas convertir a una
tupla de enteros. Recuerda que las tuplas son inmutables, lo que las
hace ideales para este propósito.
3. Cálculo del Promedio: Escribe una función que tome como argumento
una tupla de calificaciones y retorne el promedio. Usa esta función para
calcular el promedio de cada asignatura.
4. Impresión de Resultados: Itera sobre el diccionario de asignaturas y
calificaciones para imprimir el promedio de cada una. Formatea la
salida para que sea clara y fácil de entender. """

""" #asignatura
asignaturas = {} # creamos diccionario  donde guardamos asignaturas
calificaciones = {} # creamos diccionario  donde guardamos calificaciones 
continuar= True
while continuar: # while true
    asignatura = input( "Ingrese asignatura o 'salir' para terminar: ")
    if asignatura == 'salir':
        continuar = False # break
    else:
         calific= input("Ingrese calificacion") """
         
         
         

#****************************************
""" def calcular_promedio(calificaciones):
    #Calcula el promedio de una lista de calificaciones.
    # Verifica si no hay calificaciones, en cuyo caso devuelve 0 para evitar la división por cero
    if not calificaciones:
        return 0
    # Calcula el promedio sumando todas las calificaciones y dividiendo por el número de calificaciones
    return sum(calificaciones) / len(calificaciones)

# Diccionario para almacenar las asignaturas y las calificaciones de los estudiantes
asignaturas = {}

# Bucle que se ejecutará hasta que se ingrese 'salir'
while True:
    # Solicitar al usuario el nombre de la asignatura o la opción para salir
    asignatura = input("Ingrese el nombre de la asignatura (o 'salir' para terminar): ")
    # Verificar si se debe salir del bucle
    if asignatura.lower() == 'salir':
        break
    # Solicitar al usuario las calificaciones de los estudiantes para la asignatura actual
    calificaciones_str = input(f"Ingrese las calificaciones de los estudiantes para {asignatura} separadas por espacios: ")
    # Convertir la cadena de calificaciones en una tupla de enteros
    calificaciones = tuple(map(int, calificaciones_str.split()))
    # Almacenar las calificaciones en el diccionario de asignaturas con la asignatura como clave
    asignaturas[asignatura] = calificaciones

# Mostrar el promedio de calificaciones por asignatura
print("\nPromedio de calificaciones por asignatura:")
for asignatura, calificaciones in asignaturas.items():
    # Calcular el promedio de calificaciones utilizando la función calcular_promedio
    promedio = calcular_promedio(calificaciones)
    # Imprimir el nombre de la asignatura y su promedio de calificaciones
    print(f" - {asignatura}: {promedio:.2f}") """
    
    
    
    
    
    
#Ricardo **************************************************************************

from proceso import cargar_asignaturas
from calculos import obtener_promedio_asignaturas
import informes

if __name__ == "__main__":
    asignaturas = None
    asignaturas = cargar_asignaturas(2)
    #debug
    print(asignaturas)
    
    #obtencion de promedios
    promedios = obtener_promedio_asignaturas (asignaturas)
    #debug
    #print(promedios)
    
    if promedios:
        informes.mostrar_promedios_por_asignatura(promedios)



