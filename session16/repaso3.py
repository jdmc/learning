"""
Repasa raspectos relevantes de POO
"""

class Zoo():
    """Clase que representa un zoológico"""
    def __init__(self) -> None:
        self.animals = []
        
        
    
    
    def add_animals(self, *animals):
        """Agrega animales al zoológico"""
    animals = [
        Animal("Lion", 4),
        Animal("Zebra", 4),
        Animal("Giraffe", 2),
    ]
    zoo.add_animals(*animals)
    self.assertEqual(zoo.animals, animals)

    def __repr__(self) -> str:
        """Retorna una representación del zoológico"""
        pass

    def animals_by_color(self, color: str):
        """Retorna una lista con los animales del color especificado"""
        pass

    def animals_by_legs(self, legs: int):
        """Retorna una lista con los animales con la cantidad de patas especificada"""
        pass

    def num_of_legs(self):
        """Retorna la cantidad total de patas en el zoológico"""
        pass