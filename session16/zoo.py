"""
Repasa raspectos relevantes de POO
"""

class Zoo():
    """Clase que representa un zoológico"""
    def __init__(self) -> None:
        self.animals = []
    
    
    def add_animals(self, *animals):
        """Agrega animales al zoológico"""
        for animal in animals:
            self.animals.append(animal)

    def __repr__(self) -> str:
        """Retorna una representación del zoológico"""
        return '\n'.join(str(animal) for animal in self.animals)    

    def animals_by_color(self, color: str):
        """Retorna una lista con los animales del color especificado"""
        return [animal for animal in self.animals if animal.color == color]

    def animals_by_legs(self, legs: int):
        """Retorna una lista con los animales con la cantidad de patas especificada"""
        #return [animal for animal in self.animals if animal.legs == legs]
        return list(filter(lambda animal: animal.legs == legs, self.animals))
    

    def num_of_legs(self):
        """Retorna la cantidad total de patas en el zoológico"""
        return sum(animal.legs for animal in self.animals)