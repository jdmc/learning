
def func_a():
    dividendo = input("Ingrese el dividendo: ")
    divisor = input("Ingrese el divisor: ")
    resultado = func_b(float(dividendo), float(divisor))
    print(f"El resultado de dividir {dividendo} entre {divisor} es: {resultado}")
    

def func_b(dividendo: float, divisor: float) -> float:
    return func_c(dividendo, divisor)

def func_c(dividendo: float, divisor: float) -> float:
    return dividendo / divisor


if __name__ == "__main__":
    continuar = True
    while continuar:
        try:
            func_a()
            continuar = input("Desea continuar? (s/n): ").lower() == "s"
        except ZeroDivisionError as zex:
            print(zex)
        except ValueError as vex:
            print(vex)
        else:
            pass
        finally:
            if continuar:
                print("Iteramos sobre la operacion")
            else:
                print("Gracias por usar esta calculadora")