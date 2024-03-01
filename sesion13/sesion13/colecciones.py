
from collections import Counter, defaultdict, namedtuple

lista_notas = [7.5, 8.3, 9.0, 8.3,7.0,7.5]

contador_notas = Counter(lista_notas)

#print(contador_notas[7.5])


data = defaultdict(list)

print(data['a'])

data['a'] = [1,2]
print(data['a'])


t = (1,2,3)
t[0]


Cuenta = namedtuple('Cuenta', ['titular', 'saldo'])

cuenta_pedro = Cuenta(titular='Pedro', saldo=1800)

print(cuenta_pedro.titular, cuenta_pedro.saldo)

cuentas = [
            ('Pedro', 1800),
            ('Maria', 1500),
            ('Julia', 1300),
            ('Ramon', 800)
        ] 

cuentas_nominales = list(map(Cuenta._make, cuentas))

print(cuentas_nominales[-1].titular, cuentas_nominales[-1].saldo)


from collections import deque

amigos = deque(('Rafa', 'Maria', 'Ernesto'))
amigos.append('Marcelo')
print(amigos)

amigos.appendleft('Alicia')
print(amigos)

amigos.pop()
print(amigos)

amigos.popleft()
print(amigos)
