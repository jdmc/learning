"""  
¡Debes diseñar un devorador de vocales! Escribe un programa que use:

Un bucle "for".
El concepto de ejecución condicional (if-elif-else).
La sentencia continue.
Tu programa debe:

Pedir al usuario que ingrese una palabra.
Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada. """

# crear una lista de las vocales
eat = ['A', 'E', 'I', 'O', 'U']

# solicitará al usuario que ingrese una palabra
user_word = input("ingresa una palabra: ")   

#convertirá esa palabra a mayúsculas 
user_word = user_word.upper()


for letter in user_word: # recorrerá cada letra de la palabra
    if letter in eat: # Verifica si la letra actual es una vocal
        continue #Si la letra es una vocal (A, E, I, O, U), se ignorará y el bucle continuará con la siguiente letra sin imprimir, es decir continue la iteración
    print (f"Con la hambre que tenemos te compartimos las consonantes restantes:",letter) # Si la letra no es una vocal, la imprime (es una consonante)