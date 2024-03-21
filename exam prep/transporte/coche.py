"""
Módulo que define la clase `Coche` que hereda de la clase `Vehiculo`.

Atributos:
    _disponible: Indica si el vehículo está disponible para ser asignado a un conductor.

Hereda de:
    Vehiculo
"""

from vehiculo import Vehiculo

class coche (Vehiculo):
    """
    Clase que representa un coche en la flota de la empresa.

    Atributos:
        _disponible: Indica si el vehículo está disponible para ser asignado a un conductor.

    Hereda de:
        Vehiculo
    """
    def __init__(self, model, year, combusitble, tipo, disponible):
        """
        Constructor que inicializa los atributos del coche.
    
            Parámetros:
                modelo: El modelo del coche.
                año: El año del coche.
                combustible: El tipo de combustible del coche.
                tipo: El tipo de vehículo (automóvil, camión, motocicleta).
                disponible: Indica si el vehículo está disponible para ser asignado a un conductor.
        """
        super().__init__(self, model, year, combusitble, tipo)
        self._disponible = disponible
        
        
    def get_disponible(self):
        """
        Devuelve si el vehículo está disponible.
    
        Retorno:
            True si el vehículo está disponible, False en caso contrario.
        """
        return self._disponible
    