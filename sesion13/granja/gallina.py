from animal import Animal

class Gallina(Animal):
    
    def comer(self):
        super().comer() + "y picotear como una gallina"