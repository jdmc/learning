from animal import Animal

class Vaca(Animal):
    
    def comer(self):
        super().comer() + "y rumiar como una vaca"