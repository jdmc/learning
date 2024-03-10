# Lista de tuplas (nombre, calificación)
estudiantes = [("Juan", 75), ("María", 50), ("Carlos", 80), ("Ana", 65), ("Pedro", 55)]

# Utiliza la comprensión de listas para filtrar los nombres de los estudiantes que aprobaron el examen

cracks = [ aprobado[0] for aprobado in estudiantes if aprobado[1] >= 60 ]

print(" Estudiantes cracks con 60 o más puntiación:", cracks)

# Lista de tuplas (nombre del producto, precio, cantidad en stock)
productos = [("Camisa", 25, 10), ("Pantalón", 60, 5), ("Zapatos", 80, 0), ("Bufanda", 40, 3), ("Gorra", 20, 8)]

# Utiliza la comprensión de listas para filtrar los nombres de los productos que cumplen con las condiciones

caro = []
