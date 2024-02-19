""" 

Se debe implementar if __name__ == "__main__": cuando un archivo de Python puede ser:

Ejecutado como un programa principal: En este caso, el código dentro del bloque if __name__ == "__main__": se ejecutará.

Importado como un módulo: En este caso, el código dentro del bloque if __name__ == "__main__": no se ejecutará.

Razones para usar if __name__ == "__main__"::

Evitar la ejecución de código no deseado: Si un archivo se puede importar como un módulo, no queremos que se ejecute todo el código del archivo cuando se importe.
Permitir diferentes comportamientos: El código dentro del bloque if __name__ == "__main__": puede ser diferente al código que se ejecuta cuando se importa el archivo como un módulo.

En resumen, se debe implementar if __name__ == "__main__": cuando un archivo de Python necesita tener diferentes comportamientos dependiendo de si se ejecuta como un programa principal o se importa como un módulo.

 """

if __name__ == "__main__":
    print("Programa pricipal en ejecucion")

    # lo que no se puede hacer (definicion) con las variables
    """
    No pueden emepezar con numero
    No simbolos especiales
    nombre-y-apellido
    nombre! = ""
    SEGUNDOS.POR.MINUTO = 10
    """
    # lower snake case
    nombre_y_apellido = "Juan Lopez"

    # ctes
    PI = 3.1415
    SEGUNDOS_POR_MINUTO = 10

    '''
    Dado (pedir al usuario / input(preguta)) un nombre y apellido, 
    el programa mostrara el num. 
    de caracteres tanto del nombre com del apellido
    '''
    # peticion de datos al usuario
    nombre = input("Nombre?:")
    apellido = input("Apellido?:")

    # peticion de datos de numero de caraxcteres de nombre y apellido
    print(f"El num. de caracteres de tu nombre es {len(nombre)} y el de tu apellido es {len(apellido)}")

     

