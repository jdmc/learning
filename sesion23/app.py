"""Modulo que contiene una funciones operativas matematicas"""
def contar_vocales(palabra: str) -> int:
    """
    Dada una palabra, retorna el total de vocales que contiene
    :param palabra: str
    :return: int

    >>> contar_vocales("hola")
    2

    >>> contar_vocales("murcielago")
    5

    >>> contar_vocales("klmnbgtr")
    0
    """
    total_vocales = 0
    for letra in palabra:
        if letra in "aeiou":
            total_vocales += 1
    return total_vocales


def sumar_lista_numeros(l: list) -> int:
    pass


#help(contar_vocales)

if __name__ == "__main__":
    import doctest
    doctest.testmod()