# if ternario

numero = int(input("Numero?:"))

""" if numero % 2 == 0:
    print("Es par") 
else:
    print("Es impar") """

mensaje = "Es impar" if numero % 2 != 0 else "Es par"
print(mensaje)

a = 2 if numero % 2 != 0 else 1

print(f"a:{a}")