from animal import Animal

class Dog(Animal):
    """Clase que representa un perro"""
    def __init__(self, name: str) -> None:
        self.name = name

    def num_legs(self):
        return 4
    
    