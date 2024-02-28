from animal import Animal

class Perro(Animal):
    
    def comer(self):
        super().comer() + "y comer como un perro"