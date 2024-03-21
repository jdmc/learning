"""
Módulo principal que define la clase `EmpresaTransporte` y las funcionalidades de la aplicación.

Atributos:
    _vehiculos: Diccionario que almacena los vehículos disponibles.

"""

from vehiculo import Vehiculo
from coche import coche

class EmpresaTransporte:
  """
  Clase que representa la empresa de transporte.

  Atributos:
    _vehiculos: Diccionario que almacena los vehículos disponibles.
  """

  def __init__(self):
    """
    Constructor que inicializa la lista de vehículos disponibles.
    """
    self._vehiculos = {}
    

  def registrar_vehiculo(self, vehiculo):
    """
    Registra un nuevo vehículo en la flota de la empresa.

    Parámetros:
      vehiculo: El vehículo a registrar.
    """
    if isinstance(vehiculo, Vehiculo):
      self._vehiculos[vehiculo._modelo] = vehiculo
      print(f"Vehículo {vehiculo._modelo} registrado correctamente.")
    else:
      print(f"Error: El objeto no es un vehículo.")
        

empresa = EmpresaTransporte()

coche1 = coche("Toyota Corolla", 2023, "Gasolina", "Automóvil", True)
empresa.registrar_vehiculo(coche1)

