

def pedir_temperaturas():
    temp_max = float(input('Temp max?:'))
    temp_min = float(input('Temp min?:'))

    return temp_max, temp_min


semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
temperaturas_semanales = list()

for _ in range(len(semana))[:2]:
    #t_max, t_min = pedir_temperaturas()
    #temperaturas_semanales.append((t_max, t_min)) #tupla por dia
    ...

print(temperaturas_semanales)


tupla = (2,5,8)
print(list(tupla))

print(tuple([1,1,1,3]))

