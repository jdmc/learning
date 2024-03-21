
def leer_archivo(ruta_archivo):
    """
    Función que lee un archivo de texto y muestra su contenido por pantalla.

    Parámetros:
        ruta_archivo: La ruta al archivo de texto que se desea leer.

    """
    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
        print(f"Contenido del archivo:", {contenido})
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no existe.")

ruta_archivo = "ejemplo.txt"
leer_archivo(ruta_archivo)


def escribir_archivo(ruta_archivo, datos):
    """
    Función que escribe una lista de datos en un archivo CSV.

    Parámetros:
        ruta_archivo: La ruta al archivo CSV que se desea escribir.
        datos: La lista de datos que se desea escribir en el archivo.

    """
    try:
        with open(ruta_archivo, "w") as archivo:
            archivo.write(datos)
            print(f"El archivo {ruta_archivo} se ha escribió correctamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
        
if __name__ == "__main__":
# Crear un archivo de text
    
    datos_contenido = "Este es un nuevo archivo de texto que acabo de crear. "

    ruta_archivo = "ejemplo.txt"
    escribir_archivo(ruta_archivo, datos_contenido)
    
# Leer el archivo "ejemplo" de texto creado
    leer_archivo("ejemplo.txt")
