class Libro:

    @property
    def titulo(self):
        return self.__titulo
    
    def __init__(self, titulo:str, numero_paginas: int):
        self.__titulo = titulo
        self.__numero_paginas = numero_paginas

    def __str__(self):
        return f"{self.__titulo}"
    
    def __repr__(self):
        return f"<Libro> - {self.__titulo} - {self.__numero_paginas}"
    

    def __del__(self):
        print("Objeto destruido")



quijote = Libro('Don Quijote', 450)

print(quijote)

print(repr(quijote))

quijote = None


class Documento:

    #atributos de clase
    numero_documentos = 0
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self.__titulo = nuevo_titulo

    @property
    def autor(self):
        return self.__autor
        
    
    def __init__(self, titulo:str, autor: str):
        #atributo (privado)
        self.__titulo = titulo
        self.__autor = autor
        Documento.numero_documentos += 1 

    def imprimir(self):
        pass

    @classmethod
    def obtener_documento_informado(cls, autor: str):
        return cls("Titulo Dummy", autor)
    
    @staticmethod
    def metodo_estatico(resenya: str):
        print("Reseña documento:" ,resenya)



"""
documento_word = Documento.obtener_documento_informado('Pedro Perez')
print(documento_word.autor, documento_word.titulo, sep="--")

Documento.metodo_estatico('Documento validado')

print(Documento.numero_documentos)
print(documento_word.numero_documentos)

documento2 = Documento('Bild', 'Thomas')
print (documento2.numero_documentos)

Documento.numero_documentos = 1
print (documento2.numero_documentos)

documento2.numero_documentos = 10
print (documento2.numero_documentos)

print (documento_word.numero_documentos)

"""

"""
documento1 = Documento('Valores bursatiles', 'Joshua')
print(Documento.numero_documentos)
documento2 = Documento('Parrila TV', 'Pedro')
print(Documento.numero_documentos)
documento3 = Documento.obtener_documento_informado('Juan')
print(Documento.numero_documentos)
documento2.numero_documentos = 10
print(Documento.numero_documentos)
print(documento2.numero_documentos)
print(documento1.numero_documentos)
"""




    

