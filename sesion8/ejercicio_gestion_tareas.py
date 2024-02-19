#haciendo uso de un modulo


def cargar_tareas():
  """
  Carga las tareas desde un archivo y devuelve una lista.
  """
  try:
    with open("tareas.txt", "r") as archivo:
      tareas = [linea.strip().split(",") for linea in archivo]
  except FileNotFoundError:
    print("**Error:** Archivo 'tareas.txt' no encontrado. Se iniciará con una lista vacía.")
    return []
  except Exception as e:
    print(f"**Error inesperado:** {e}")
    return []
  return tareas

def agregar_tarea(tareas):
  """
  Solicita al usuario una nueva tarea y la agrega a la lista.
  """
  nombre = input("Ingrese el nombre de la tarea: ")
  prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
  nueva_tarea = (nombre, prioridad)
  tareas.append(nueva_tarea)
  print("**Tarea agregada correctamente!**")

def guardar_tareas(tareas):
  """
  Guarda la lista de tareas en el archivo.
  """
  try:
    with open("tareas.txt", "w") as archivo:
      for tarea in tareas:
        archivo.write(",".join(tarea) + "\n")
  except Exception as e:
    print(f"**Error al guardar las tareas:** {e}")

def mostrar_tareas(tareas):
  """
  Muestra todas las tareas en la consola.
  """
  if not tareas:
    print("**No hay tareas cargadas.**")
    return
  print("**Lista de tareas:**")
  for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea[0]} ({tarea[1]})")

