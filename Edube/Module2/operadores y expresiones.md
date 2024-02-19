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

```python

i = i + 2 * j ⇒ i += 2 * j

var = var / 2 ⇒ var /= 2

rem = rem % 10 ⇒ rem %= 10

j = j - (i + var + rem) ⇒ j -= (i + var + rem)

x = x ** 2 ⇒ x **= 2

```

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

1. Paréntesis () - Utilizados para agrupar expresiones y alterar el orden de evaluación.>> De acuerdo con las reglas aritméticas, las sub-expresiones dentro de los paréntesis siempre se calculan primero.
2. Exponente ** - Realiza operaciones de exponenciación.  
3. Negación - (unario) - Negación unaria.  
4. Multiplicación *,   División /  , División entera //  , Módulo % - Operaciones aritméticas básicas.  
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

# Puntos Clave

1. Una expresión es una combinación de valores (o variables, operadores, llamadas a funciones, aprenderás de ello pronto) las cuales son evaluadas y dan como resultado un valor, por ejemplo, 1 + 2.

2. Los operadores son símbolos especiales o palabras clave que son capaces de operar en los valores y realizar operaciones matemáticas, por ejemplo, el * multiplica dos valores: x * y.

3. Los operadores aritméticos en Python:   
* \+ (suma),
* \- (resta),   
* \* (multiplicación),  
* \/ (división clásica: regresa un flotante siempre),  
* \% (módulo: divide el operando izquierdo entre el operando derecho y regresa el residuo de la operación, por ejemplo, 5 % 2 = 1),   
* \** (exponenciación: el operando izquierdo se eleva a la potencia del operando derecho, por ejemplo, 2 ** 3 = 2 * 2 * 2 = 8),   
* \// (división entera: retorna el número resultado de la división, pero redondeado al número entero inferior más cercano, por ejemplo, 3 // 2.0 = 1.0).

4. Un operador unario es un operador con solo un operando, por ejemplo, -1, o +3.

5. Un operador binario es un operador con dos operados, por ejemplo, 4 + 5, o 12 % 5.

6. Algunos operadores actúan antes que otros, a esto se le llama - jerarquía de prioridades:   
   Unario + y - tienen la prioridad más alta.   
   Después: **, después: *, /, y %, y después la prioridad más baja: binaria + y -.  

7. Las sub-expresiones dentro de paréntesis siempre se calculan primero, por ejemplo,  15 - 1 * ( 5 *( 1 + 2 ) ) = 0.

8. Los operadores de exponenciación utilizan enlazado del lado derecho, por ejemplo, 2 ** 2 ** 3 = 256.