from cuenta import Cuenta, NumeroCuentaExistenteError

class Banco:
    
    @property
    def cuentas(self):
        return self.__cuentas
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__cuentas = list()
        
    def agregar_cuenta(self, cuenta: Cuenta):
        self.__cuentas.append(cuenta)
