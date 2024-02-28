from animal import Animal

class Gallina(Animal):
    
    def comer(self):
        return super().comer() + "y picotear como una gallina"