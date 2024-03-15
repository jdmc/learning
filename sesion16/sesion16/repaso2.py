"""Clases que representan la funcionalidad de transacciones monetarias"""

class Scoop():
    """Clase que representa un scoop de helado
        Otra linea
    """
    @property
    def flavor(self): #propiedad
        return self.__flavor
    
    def __init__(self, flavor):
        self.__flavor = flavor #atributo

    def __str__(self) -> str:
        return f"{self.flavor}"


class Bowl():
    """Clase que representa un bowl de helado"""

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            self.scoops.append(scoop)
    
    def __str__(self) -> str:
        return f"{self.scoops[0]}"
    
    def __repr__(self) -> str:
        return '\n'.join(s.flavor for s in self.scoops)


#instanciar
s1 = Scoop("chocolate")
s2 = Scoop("vainilla")
s3 = Scoop("fresa")

bowl = Bowl()
bowl.add_scoops(s1, s2, s3)
print(bowl)
#print(bowl.__repr__())



class A():
    def __init__(self) -> None:
        self.data = 10

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print(self.data)    

b = B()

class CustomDict(dict):
    """Clase que representa un diccionario personalizado"""
    
    def __getitem__(self, key):
        
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass    

        return super().__getitem__(key)




d = CustomDict()
d['a'] = 10
print(d['a'])

d[1] = 20
print(d[1])

#print(d['b'])


lista = list(range(10))

for numero in lista:
    if numero == 5:
        break
    print(numero)
else:
    print("Iteracion terminada")