import random as rd
import math

print(math.floor((rd.random() * 10)))

print(rd.randint(5, 10))


saludos = ['hola', 'adios', 'hasta luego', 'buenas noches']
print(rd.choice(saludos))

print(rd.sample(saludos, 2))

rd.shuffle(saludos)
print(saludos[0])
