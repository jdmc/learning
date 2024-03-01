class Pizza:
    def __init__(self, info: dict):
        for clave, valor in info.items():
            setattr(self, clave, valor)


data =  {
    "nombre": "Cuatro estaciones",
    "precio": 20.0,
    "tamanyo": "Extra",
    "ingredientes": ['Atun','Tomate','Queso']
}

cuatro_estaciones = Pizza(data)

print(cuatro_estaciones.ingredientes, cuatro_estaciones.precio)

for attr in ['nombre', 'precio','cocinero']:
    print(getattr(cuatro_estaciones, attr, 'No data'))


atributos_a_borrar = ['precio', 'tamanyo']
for attr in atributos_a_borrar:
    if hasattr(cuatro_estaciones, attr):
        delattr(cuatro_estaciones, attr)


print(cuatro_estaciones.nombre)
#print(cuatro_estaciones.precio)


class A:
    pass

class B(A):
    pass

a = A()
b = B()

b = a

print(isinstance(a, A))
print(isinstance(b, A))

#print(issubclass(B, A))

#print(isinstance('a', int))
#print(isinstance([], (dict, tuple)))





