from cuenta import Cuenta, CuentaExistenteError  # Importar la clase Cuenta y la excepción CuentaExistenteError desde el módulo cuenta.py

class Banco:
    @property
    def cuentas(self):
        # Propiedad para acceder a la lista de cuentas del banco
        return self.__cuentas

    def __init__(self, nombre) -> None:
        # Inicializar un nuevo banco con un nombre
        self.__nombre = nombre  # Atributo privado para el nombre del banco
        self.__cuentas = list()  # Inicializar la lista de cuentas del banco como una lista vacía

    def agregar_cuenta(self, cuenta: Cuenta):
        # Método para agregar una cuenta al banco
        if cuenta.numero_cuenta in [cuenta.numero_cuenta for cuenta in self.cuentas]:
            # Verificar si el número de cuenta ya existe en el banco
            raise CuentaExistenteError(cuenta.numero_cuenta)  # Lanzar una excepción si el número de cuenta ya existe
        self.__cuentas.append(cuenta)  # Agregar la cuenta a la lista de cuentas del banco

