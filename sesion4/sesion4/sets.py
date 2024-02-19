# conjuntos

conjunto1 = set()

conjunto1.add(1)
conjunto1.add(1)
print(conjunto1)
conjunto1.add(20)
print(conjunto1)


conjunto2 = {1,2,3,4,5,6,7}

conjunto1.update(conjunto2)
print(conjunto1)

conjunto3 = {1.2,5.6,2.3,5.1,2,5}
print(conjunto3)

#conjunto2.remove(10)
#print(conjunto2)

conjunto2.discard(10)
print(conjunto2)

item = conjunto2.pop()
print(item)

item = conjunto2.pop()
print(item)

set1 = {1,2,3}
set2 = {2,3,5}

#operaciones de conjuntos
set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)





