class Vehiculo:
    def __init___(self, model, year, combusitble):
        self._modelo = model
        self._year = year
        self._combusitble = combusitble
    
    def mostrar_informacion(self):
        return f"{self._modelo} >> {self._combusitble} ** {self._year}"