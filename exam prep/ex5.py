class Vehiculo():
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

class Coches(Vehiculo): # clase que representa un coche, hereda de la clase vehiculo 
    def __init__(self, marca, modelo, anno, color, numero_puertas): # constructor de la clase
        super().__init__(marca, modelo, anno, color) # herencia de la clase vehiculo
        self._numero_puertas = numero_puertas
        
    def get_numero_puertas(self):
        return self._numero_puertas
    
# Outcome Vehiculo
vehiculo = Vehiculo("Toyota", "Corolla", 2023, "Blanco") # padre

coche = Coches("Toyota", "Corolla", 2023, "Blanco", "4") # hijo

print(f"Vehiculo:", vehiculo.mostrar_informacion())

print(f"Marca:", coche.get_marca())

print(f"Modelo:",coche.get_modelo())

print(f"Color:",coche.get_color())

print(f"Año:",coche.get_anno())

print(f"Numero de puertas:",coche.get_numero_puertas())



print(f"Que es?",vehiculo, coche)

