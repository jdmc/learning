# En Python, los operadores básicos incluyen:

## 1.Aritméticos: Se utilizan para realizar operaciones matemáticas básicas.

\+ (suma)  
\-  (resta)  
\* (multiplicación)  
\/ (división)  
\// (división entera) >> La division entera también se le suele llamar en inglés floor division.    
\% (módulo) >> El resultado de la operación es el **residuo** que queda de la división entera. En otras palabras, es el valor que sobra después de dividir un valor entre otro para producir un resultado entero.  
\** (exponente)  

Operadores Aritméticos: **exponenciación**  
Un signo de ** (doble asterisco) es un operador de exponenciación (potencia).   
El argumento a la izquierda es la base, el de la derecha, el exponente.  

Las matemáticas clásicas prefieren una notación con superíndices, como el siguiente: 2^3.     
Los editores de texto puros no aceptan esa notación,   
por lo tanto Python utiliza ** en lugar de la notación matemática, por ejemplo, 2 ** 3.  

## 2.Comparación: Se utilizan para comparar dos valores y devolver un resultado booleano (True o False).

\== (igual a)  
\!= (diferente de)  
\< (menor que)  
\> (mayor que)  
\<= (menor o igual que)  
\>= (mayor o igual que)  

## 3.Asignación: Se utilizan para asignar valores a variables.

\= (asignación simple)  
\+= (suma y asignación)  
\-= (resta y asignación)  
\*= (multiplicación y asignación)  
\/= (división y asignación)  
\//= (división entera y asignación)  
\%= (módulo y asignación)  
\**= (exponente y asignación)  

## 4.Lógicos: Se utilizan para realizar operaciones lógicas en valores booleanos.

and (y lógico)  
or (o lógico)  
not (negación lógica)  

## 5.Bit a Bit: Se utilizan para realizar operaciones bit a bit en enteros.

\& (AND bit a bit)  
\| (OR bit a bit)  
\^ (XOR bit a bit)  
\~ (NOT bit a bit)  
\<< (desplazamiento a la izquierda)  
\>> (desplazamiento a la derecha)  

## 6.Miembro: Se utilizan para verificar si un valor está presente en una secuencia.

in (está presente)  
not in (no está presente)  

## 7.Identidad: Se utilizan para verificar si dos objetos son el mismo objeto.

is (es el mismo objeto)  
is not (no es el mismo objeto)  

Estos son los operadores básicos en Python que se utilizan para realizar una variedad de operaciones, desde aritméticas hasta comparaciones y asignaciones.

# Lista de prioridades  

lista de prioridades con los operadores en Python, de mayor a menor prioridad:

1. Paréntesis () - Utilizados para agrupar expresiones y alterar el orden de evaluación.  
2. Exponente ** - Realiza operaciones de exponenciación.  
3. Negación - (unario) - Negación unaria.  
4. Multiplicación *, División /, División entera //, Módulo % - Operaciones aritméticas básicas.  
5. Suma +, Resta - - Operaciones aritméticas básicas.  
6. Concatenación de cadenas + - Une cadenas.  
7. Operadores de comparación ==, !=, <, >, <=, >=, in, not in, is, is not - Realizan comparaciones entre valores.  
8. Operadores lógicos not - Negación lógica.  
9. Operadores lógicos and - Conjunción lógica.  
10. Operadores lógicos or - Disyunción lógica.  
11. Asignación =, +=, -=, *=, /=, //=, %=, **= - Asignan valores a variables.  
12. Operadores de identidad is, is not - Comprueban si dos variables se refieren al mismo objeto.  
13. Operadores de pertenencia in, not in - Verifican si un valor está presente en una secuencia.  
14. Operadores de bits &, |, ^ - Operaciones de bits AND, OR, XOR.  
15. Operadores de desplazamiento de bits <<, >> - Desplazan bits a la izquierda o a la derecha.  
16. Negación de bits ~ - Realiza la negación de bits.  

Es importante tener en cuenta estas prioridades al escribir expresiones para asegurarse de que se evalúen en el orden deseado. Siempre puedes usar paréntesis para forzar el orden de evaluación si es necesario.