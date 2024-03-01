from cliente import Cliente

class Cuenta:

    def __init__(self, numero_cuenta: str, saldo: float, propietario: Cliente) -> None:
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__propietario = propietario

    def mostrar_informacion(self):
        return f"{self.__numero_cuenta} - {self.__saldo} - {self.__propietario}"
