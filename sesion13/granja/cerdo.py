from animal import Animal

class Cerdo(Animal):
    
    def comer(self):
        return super().comer() + "y comer como un cerdo"