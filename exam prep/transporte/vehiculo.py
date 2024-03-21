"""
Módulo que define la clase `Vehiculo` que representa un vehículo en la flota de la empresa.

Atributos:
    _modelo: El modelo del vehículo.
    _year: El año del vehículo.
    _combustible: El tipo de combustible del vehículo.
    _tipo: El tipo de vehículo (coche, camión, moto).
"""

class Vehiculo:
    """
    Clase que representa un vehículo en la flota de la empresa.

    Atributos:
        _modelo: El modelo del vehículo.
        _year: El año del vehículo.
        _combustible: El tipo de combustible del vehículo.
        _tipo: El tipo de vehículo (coche, camión, moto).
    """
    def __init___(self, model, year, combusitble, tipo):
        """
        Constructor que inicializa los atributos del vehículo.
    
        Parámetros:
            modelo: El modelo del vehículo.
            year: El año del vehículo.
            combustible: El tipo de combustible del vehículo.
            tipo: El tipo de vehículo (coche, camión, moto).
        """       
        self._modelo = model
        self._year = year
        self._combusitble = combusitble
        self._tipo = tipo
    
    def mostrar_informacion(self):        
        """
        Devuelve una cadena con la información del vehículo.
    
        Retorno:
            Una cadena con la información del vehículo.
        """
        return f"{self._tipo} : {self._modelo} >> {self._combusitble} ** {self._year}"
    
