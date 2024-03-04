""" Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. 
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

La figura ilustra la regla utilizada por los constructores:

  -
 --
--- 

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: 
    si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, 
    terminan su trabajo inmediatamente. 
    
1. Pedir al usuario que ingrese la cantidad de bloques disponibles.
2. Inicializar una variable altura en 0 para mantener un registro de la altura actual de la pirámide.
3. Inicializar una variable bloques_utilizados en 0 para llevar un registro de cuántos bloques se han utilizado hasta ahora.
4. Usar un bucle while para construir la pirámide mientras haya suficientes bloques disponibles.
5. En cada iteración del bucle, agregar una capa a la altura de la pirámide y actualizar la cantidad de bloques utilizados.
6. Imprimir la altura final de la pirámide.
    """
    
# Paso 1: Solicitar al usuario la cantidad de bloques disponibles
bloques_disponibles = int(input("Ingrese la cantidad de bloques disponibles: "))  
    
    
# Paso 2: Inicializar variables
altura = 0
bloques_utilizados = 0
    
# Paso 3: Construir la pirámide
while bloques_utilizados <= bloques_disponibles:
    altura += 1  # Agregar una capa a la altura de la pirámide
    bloques_en_capa = altura  # La cantidad de bloques en esta capa es igual a la altura
    if bloques_utilizados + bloques_en_capa > bloques_disponibles: # Verificar si hay suficientes bloques para construir esta capa
        break  # Si no hay suficientes bloques, salir del bucle    
    bloques_utilizados += bloques_en_capa  # Actualizar la cantidad de bloques utilizados
5
# Paso 4: Imprimir la altura final de la pirámide
print("La altura de la pirámide construida es:", altura)   