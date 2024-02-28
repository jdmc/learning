from cliente import Cliente

class SaldoNegativoError(Exception):
    def __init__(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"La operación resultaría en un saldo negativo: {self.saldo}"

class NumeroCuentaExistenteError(Exception):
    def __init__(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def __str__(self):
        return f"El número de cuenta '{self.numero_cuenta}' ya existe"

class Cuenta:
    
    def __init__(self, numero_cuenta:str, saldo:float, propietario: Cliente) -> None:
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__propietario = propietario # instancia de la clase Cliente
        
    def mostrar_informacion(self):
        return f"{self.__numero_cuenta} - {self.__saldo} - {self.__propietario}"  