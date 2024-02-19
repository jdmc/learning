def sumar(x: int, y: int) -> int:
    return x + y

def sumar_v2(*numeros) -> int: #varargs
    return sum(numeros)


def restar(x: int, y: int) -> int:
    return x - y