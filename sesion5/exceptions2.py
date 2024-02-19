
try:
    index = 1
    valores = [1,2,3,4,5,6]
    if index > len(valores) - 1:
        raise IndexError(f"Has superado el limite de indice posible")
    else:
        print(valores[index])
except IndexError:
    print("INdice sobrepasado")
except Exception:
    print("Error general")
else:
    print("Acceso correcto")
finally:
    print("Operacion finalizada")
    valores = None

