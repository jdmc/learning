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

eat = ['A', 'E', 'I', 'O', 'U']

user_word = input("ingresa una palabra: ")   

user_word = user_word.upper()

for letter in user_word:
    if letter in eat:
        continue
    print (letter)