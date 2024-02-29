from cliente import Cliente  # Importar la clase Cliente desde el módulo cliente.py

class SaldoNegativoError(Exception):  # Definir una nueva excepción para saldo negativo >> Parte 2: 2
    def __init__(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"La operación resultaría en un saldo negativo: {self.saldo}"  # Mensaje de error personalizado

class CuentaExistenteError(Exception):  # Definir una nueva excepción para cuenta existente >> Parte 2: 2
    def __init__(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def __str__(self):
        return f"El número de cuenta '{self.numero_cuenta}' ya existe"  # Mensaje de error personalizado

class Cuenta:
    cuentas_existentes = set()  # Conjunto para almacenar números de cuenta existentes

    def __init__(self, numero_cuenta:str, saldo:float, propietario: Cliente) -> None: # Inicializar una nueva cuenta con número de cuenta, saldo y propietario        
        self._numero_cuenta = numero_cuenta  # Atributo privado para el número de cuenta
        self.__saldo = saldo  # Atributo privado para el saldo
        self.__propietario = propietario  # Atributo privado para el propietario (instancia de la clase Cliente)
        Cuenta.cuentas_existentes.add(numero_cuenta)  # Agregar el número de cuenta a las cuentas existentes

    def mostrar_informacion(self):
        # Método para mostrar información de la cuenta (número de cuenta, saldo y propietario)
        return f"{self._numero_cuenta} - {self.__saldo} - {self.__propietario}"

    def depositar(self, cantidad):
        # Método para depositar una cantidad en la cuenta
        self.__saldo += cantidad

    def retirar(self, cantidad):
        # Método para retirar una cantidad de la cuenta
        nuevo_saldo = self.__saldo - cantidad  # Calcular el nuevo saldo después de la retirada
        if nuevo_saldo < 0:
            raise SaldoNegativoError(nuevo_saldo)  # Lanzar una excepción si el saldo resultante es negativo Parte 2: 1A
        self.__saldo = nuevo_saldo  # Actualizar el saldo de la cuenta
