class Cliente:
    def __init__(self, nombre:str, dni:str) -> None:
        # Inicializar un nuevo cliente con un nombre y un DNI
        self.__nombre = nombre  # Atributo privado para el nombre del cliente
        self.__dni = dni  # Atributo privado para el DNI del cliente

    # MAGIC >> Método mágico para devolver una representación legible del cliente
    def __str__(self):
        return f"{self.__nombre}|{self.__dni}"
