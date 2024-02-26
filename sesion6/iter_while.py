
contador= 1
total = 0

while contador <= 5 or total <= 10: # con "or" las 2 deben ser falsas para que pare la operación
    print(f"Contador:{contador}")
    print(f"Total:{total}")
    total += contador
    contador +=1
    
    print("-" * 50)
    
contador= 1
total = 0
    
while contador <= 5 and total <= 10: # con "and" SOLO 1 debe ser falsa para que pare la operación
    print(f"Contador:{contador}")
    print(f"Total:{total}")
    total += contador
    contador +=1
    
i = -1
lista = [1,2,3,4,5]
while i < 10 and i < len(lista) - 1:
    i += 1
    print(f"i:{i}")
    if lista[i] > 4:
        #break 
        continue # se puede usar "break" o "continue" SOLO que la "continue NO incrementa el valor" i += 1 hay que ponerlo antes

    
i = -1
lista = [1,2,3,4,5]
for i < 10 and i < len(lista) - 1:
i += 1
print(f"i:{i}")
if lista[i] > 4:
#break 
#continue # se puede usar "break" o "continue" SOLO que la "continue NO incrementa el valor" i += 1 hay que ponerlo antes
pass