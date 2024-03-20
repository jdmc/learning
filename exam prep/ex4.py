class Vehiculo: # clase que representa un vehiculo
    def __init__(self, marca, modelo, anno, color): # constructor de la clase vehiculo
        #parametros de la clase
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._anno =  anno

    
    def mostrar_informacion(self):
        return f"{self._marca} -- {self._modelo} -- {self._color} ** {self._anno}"

    def get_marca(self):
        return self._marca
    
    def get_modelo(self):
        return self._modelo
    
    def get_anno(self):
        return self._anno
    
    def get_color(self):
        return self._color
    

# Outcome Vehiculo
vehiculo = Vehiculo("Toyota", "Corolla", 2023, "Blanco")

print(f"Vehiculo:", vehiculo.mostrar_informacion())

print(f"Marca:", vehiculo.get_marca())

print(f"Modelo:",vehiculo.get_modelo())

print(f"Color:",vehiculo.get_color())

print(f"Año:",vehiculo.get_anno())



print(f"Que es?",vehiculo)

    
    