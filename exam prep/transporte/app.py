class EmpresaTransporte:
    def __init__(self, registrar_vehiculo, asignar_conductor, consultar_modelo, consultar_tipo):
        self._registrar_vehiculo = registrar_vehiculo
        self._asignar_conductor = asignar_conductor
        self._consultar_modelo = consultar_modelo
        self._consultar_tipo = consultar_tipo