from vehiculo import Vehiculo

class coche (Vehiculo):
    def __init__(self, model, year, combusitble, tipo, disponible):
        super().__init__(self, model, year, combusitble, tipo)
        self._disponible = disponible
        
        
    def get_disponible(self):
        return self._disponible
    