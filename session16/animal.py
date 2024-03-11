class Animal():
    """Clase que representa un animal"""
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def color(self) -> str:
        return self.__color
    
    @property
    def legs(self) -> int:
        return self.__legs
    
    def __init__(self, name: str, color: str, legs: int) -> None:
        self.__name = name
        self.__color = color
        self.__legs = legs
    
    def __str__(self) -> str:
        return f"{self.name} - {self.color} - {self.legs} patas"
    
    
