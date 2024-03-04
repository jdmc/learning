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
    
#1 Solicitar la cantidad de bloques disponibles
bloques = int(input("Ingrese la cantidad de bloques disponibles: "))

# 2 + 3 Inicializar variables
altura = 0
bloques_utilizados = 0

# 4 Construir la pirámide
while bloques_utilizados <= bloques:
    altura += 1
    bloques_utilizados += altura

# Calcular la altura final de la pirámide
altura -= 1

# Imprimir la altura de la pirámide
print("La altura de la pirámide construida es:", altura)


""" while bloques_utilizados <= bloques:: 
Este es el encabezado de un bucle while. 
Indica que el bucle continuará ejecutándose mientras la cantidad de bloques utilizados sea menor o igual a la cantidad total de bloques disponibles. 
Si en algún momento la cantidad de bloques utilizados supera la cantidad total de bloques disponibles, el bucle se detendrá.

altura += 1: 
En cada iteración del bucle, aumentamos la variable altura en 1. 
Esto significa que estamos construyendo una nueva capa de la pirámide.

bloques_utilizados += altura: 
Aquí actualizamos la variable bloques_utilizados sumando la altura actual de la pirámide. 
Esto representa la cantidad total de bloques que hemos utilizado hasta el momento.

En resumen, este bucle while se encarga de construir la pirámide capa por capa, 
aumentando la altura de la pirámide en 1 en cada iteración y actualizando la cantidad total de bloques utilizados. 
El bucle se detiene cuando la cantidad total de bloques utilizados supera la cantidad total de bloques disponibles. """
