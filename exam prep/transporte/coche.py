from vehiculo import Vehiculo

class coche (Vehiculo):
    def __init__(self, model, year, combusitble, disponible):
        super().__init__(self, model, year, combusitble)
        self._disponible = disponible