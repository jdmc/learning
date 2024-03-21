class Vehiculo:
    def __init___(self, model, year, combusitble, tipo):
        self._modelo = model
        self._year = year
        self._combusitble = combusitble
        self._tipo = tipo
    
    def mostrar_informacion(self):
        return f"{self._tipo} : {self._modelo} >> {self._combusitble} ** {self._year}"
    
    
    # crear diccionario vehiculos Clave = modelo valor = Vehiculo