from animal import Animal

class Perro(Animal):

    def comer(self):
        return super().comer() + " y comer como un perro."
