from ejercicio_gestion_tareas import cargar_tareas, agregar_tarea, mostrar_tareas, guardar_tareas

tareas = cargar_tareas()

while True:
  print("\n**Opciones:**")
  print("1. Agregar tarea")
  print("2. Mostrar tareas")
  print("3. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    agregar_tarea(tareas)
  elif opcion == "2":
    mostrar_tareas(tareas)
  elif opcion == "3":
    guardar_tareas(tareas)
    print("**¡Hasta la próxima!**")
    break
  else:
    print("**Opción inválida. Ingrese un número del 1 al 3.**")