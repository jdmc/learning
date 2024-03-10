# Lista de tuplas (nombre, calificación)
estudiantes = [("Juan", 75), ("María", 50), ("Carlos", 80), ("Ana", 65), ("Pedro", 55)]

# Utiliza la comprensión de listas para filtrar los nombres de los estudiantes que aprobaron el examen

cracks = [ aprobado[0] for aprobado in estudiantes if aprobado[1] >= 60 ]

print(" Estudiantes cracks con 60 o más puntiación:", cracks)

# Lista de tuplas (nombre del producto, precio, cantidad en stock)
productos = [("Camisa", 25, 10), ("Pantalón", 60, 5), ("Zapatos", 80, 0), ("Bufanda", 40, 3), ("Gorra", 20, 8)]

# Utiliza la comprensión de listas para filtrar los nombres de los productos que cumplen con las condiciones

caro = [quiero[0] for quiero in productos if quiero[1] >50 and quiero[2] > 0 ]

print ("Quiero producto caro y disponible:", caro )


# Lista de tuplas (nombre del estudiante, lista de calificaciones)
estudiantes = [("Juan", [85, 92, 88]), ("María", [75, 80, 95]), ("Carlos", [90, 85, 88]), ("Ana", [85, 90, 95]), ("Pedro", [80, 85, 90])]

# Utiliza la comprensión de listas para filtrar los nombres de los estudiantes que cumplen con las condiciones 1 >= 90

crack = [coco[0] for coco in estudiantes if any (nota >= 90 for nota in coco[1])]

print ("/"*50)

print( "Coco bello más de 90:", crack)

