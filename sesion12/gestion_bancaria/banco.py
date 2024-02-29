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
        if numero_cuenta in [cuenta.numero_cuenta for cuenta in self.cuentas]:
            # Verificar si el número de cuenta ya existe en el banco
            raise CuentaExistenteError(cuenta.numero_cuenta)  # Lanzar una excepción si el número de cuenta ya existe
        self.__cuentas.append(cuenta)  # Agregar la cuenta a la lista de cuentas del banco
        

        
""" 
Me daba error en la parte principal:

File banco.py, line 16, in agregar_cuenta
    if cuenta.numero_cuenta in [cuenta.numero_cuenta for cuenta in self.cuentas]:
       ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Cuenta' object has no attribute 'numero_cuenta'
    
    En la línea 16 if cuenta.numero_cuenta in [cuenta.numero_cuenta for cuenta in self.cuentas]:, 
    el error se produce porque intento acceder al atributo numero_cuenta de cada objeto cuenta en la lista self.cuentas. 
    Sin embargo, debería acceder al atributo numero_cuenta de cada objeto Cuenta en la lista self.cuentas. 
    Esto se puede corregir simplemente eliminando el cuenta. del primer cuenta.numero_cuenta.

 """