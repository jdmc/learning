
l = list()
l2 = [1,2,3,4]

class Data(list):
    def calcular_promedio(self):
        return sum(self) / len(self)
    


data = Data([1,2,3,4,5])

print(data[0])
for numero in data:
    print(numero)

promedio = data.calcular_promedio()
print("Promedio:", promedio)
