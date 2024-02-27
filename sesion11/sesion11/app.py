#estructuras de datos -> MEM  - RAM - VOLATIL

#listas, tuplas, diccionarios, conjuntos - BASICAS

from modulo import borrar_elemento

#lista = []
lista = list()


#CRUD
def borrar_elemento(pos: int, lista: list):
    del lista[pos]


d1 = dict([('a',1),('b',2)])

d2 = {
    'c':3,
    'd':5
}

#CRUD
d1['a']
resultado = d1.get('a')

for _, valor in d2.items():
    print(valor)


#set
print("*" * 40)
conjunto1 = {1,2,3,4,5}    
for item in conjunto1:
    print(item)

#iterables y secuencias
conjunto1.add(7)
conjunto1.discard(10)

tupla = (1,2,3,4,5,6)
l = [(1,2),(3,5)]
l[0] = (4,7)
print(l)

for t in  tupla:
    print(t)

print(tupla[0])

tupla2 = tupla[2:] + (10,11)
print(tupla2)

tuple3 = tupla * 3
print(tuple3)

def calcular(p1:int, p2:int = 0):
    return p1 * p2

calcular(1,4)
calcular(1)
resultado = calcular(p2=4,p1=1)

proceso = lambda x : print('Lambda' + x)
proceso('Delta')


def calcular_valores(p1:int, p2:int, f):
    return  f(p1,p2)

#HOF
resultado2 = calcular_valores(1,5,lambda x, y : x + y)
print(resultado2)

resultados = list(map(lambda x: x + 1, [1,2,3,4,5]))
print(resultados)

resultadios_filtro = list(filter(lambda x : x > 4, [3,4,5,6,7]))
print(resultadios_filtro)

#comprehension list
lista_comp = [n * 2 for n in range(1,15) if n % 2 == 0]
print(lista_comp)














    










