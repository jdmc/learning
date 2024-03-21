"""
Función que lee un archivo de texto y muestra su contenido por pantalla.

Parámetros:
    ruta_archivo: La ruta al archivo de texto que se desea leer.

Retorno:
    None.
"""
def leer_archivo(ruta_archivo):
  """
  Función que lee un archivo de texto y muestra su contenido por pantalla.

  Parámetros:
      ruta_archivo: La ruta al archivo de texto que se desea leer.

  Retorno:
      None.
  """
  try:
    with open(ruta_archivo, "r") as archivo:
      contenido = archivo.read()
      print(contenido)
  except FileNotFoundError:
    print(f"Error: El archivo {ruta_archivo} no existe.")

ruta_archivo = "ejemplo.txt"
leer_archivo(ruta_archivo)

"""
Función que escribe una lista de datos en un archivo CSV.

Parámetros:
    ruta_archivo: La ruta al archivo CSV que se desea escribir.
    datos: La lista de datos que se desea escribir en el archivo.

Retorno:
    None.
"""
def escribir_archivo(ruta_archivo, datos):
  """
  Función que escribe una lista de datos en un archivo CSV.

  Parámetros:
      ruta_archivo: La ruta al archivo CSV que se desea escribir.
      datos: La lista de datos que se desea escribir en el archivo.

  Retorno:
      None.
  """
  try:
    with open(ruta_archivo, "w", newline="") as archivo:
      writer = csv.writer(archivo)
      writer.writerows(datos)
  except Exception as e:
    print(f"Error al escribir el archivo: {e}")

datos = [["Nombre", "Apellido", "Edad"],
        ["Juan", "Pérez", 25],
        ["María", "Gómez", 30]]

ruta_archivo = "ejemplo.csv"
escribir_archivo(ruta_archivo, datos)
