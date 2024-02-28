from cuenta import Cuenta, CuentaExistenteError

class Banco:
    
    @property
    def cuentas(self):
        return self.__cuentas
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__cuentas = list()
        
    def agregar_cuenta(self, cuenta: Cuenta):
        if cuenta.numero_cuenta in [cuenta.numero_cuenta for cuenta in self.cuentas]:
            raise CuentaExistenteError(cuenta.numero_cuenta)
        self.__cuentas.append(cuenta)
