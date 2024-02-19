

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(numeros) != 0: #no vacia
    pass

numeros[-1] = 8 #update

"""
nombre = "Juan"
nombre[0] = "H"
"""


print(numeros)

#cuantos 8's hay?
print(numeros.count(0))

print(numeros[:3])

tramo = numeros[0:2]
print(tramo, type(tramo))

numeros[0:2] = 1,14
print(numeros)
print("-" * 50)

#copia de lista
numeros_clonado = numeros[:]

print(id(numeros_clonado))
print(id(numeros))

print("-" * 50)

numerosv2 = numeros
print(id(numerosv2))
print(id(numeros))

numerosv2[-1] = 20

print(numerosv2)
print(numeros)





