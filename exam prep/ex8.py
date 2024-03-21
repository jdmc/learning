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
