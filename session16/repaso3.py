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
        return f"Zoo con {len(self.animals)} animales"

    def animals_by_color(self, color: str):
        """Retorna una lista con los animales del color especificado"""
        return [animal for animal in self.animals if animal.color == color]

    def animals_by_legs(self, legs: int):
        """Retorna una lista con los animales con la cantidad de patas especificada"""
        return [animal for animal in self.animals if animal.legs == legs]

    def num_of_legs(self):
        """Retorna la cantidad total de patas en el zoológico"""
        return sum(animal.legs for animal in self.animals)


# Crear un zoológico
zoo = Zoo()

# Agregar animales al zoológico
zoo.add_animals(lion, elephant, spider, python, flamingo)

# Comprobar la representación del zoológico
print(zoo)

# Obtener animales por color
print("Animales amarillos:", zoo.animals_by_color("amarillo"))
print("Animales negros:", zoo.animals_by_color("negro"))

# Obtener animales por cantidad de patas
print("Animales con 4 patas:", zoo.animals_by_legs(4))
print("Animales con 2 patas:", zoo.animals_by_legs(2))

# Obtener la cantidad total de patas en el zoológico
print("Cantidad total de patas en el zoológico:", zoo.num_of_legs())