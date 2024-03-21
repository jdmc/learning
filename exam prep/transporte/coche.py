from vehiculo import Vehiculo

class coche (Vehiculo):
    def __init__(self, model, year, combusitble, disponible, tipo):
        super().__init__(self, model, year, combusitble)
        self._disponible = disponible
        self._tipo = tipo
        
    def get_disponible(self):
        return self._disponible
    
    def get_tipo(self):
        return self._tipo