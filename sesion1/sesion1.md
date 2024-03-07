# str

En Python, 'str' es un tipo de dato que representa una cadena de caracteres, es decir, una secuencia de caracteres Unicode. Las cadenas en Python se pueden definir utilizando comillas simples (') o comillas dobles (").

Aquí tienes algunos ejemplos de cómo usar str en Python:

* Declaración de una cadena:

```python
cadena = 'Hola, mundo!'

```
* Concatenación de cadenas:

```python
cadena1 = 'Hola'
cadena2 = 'mundo'
concatenada = cadena1 + ', ' + cadena2 + '!'

```
* Acceso a caracteres individuales:
```python
cadena = 'Python'
primer_caracter = cadena[0]  # 'P'

```
* Subcadenas:
```python
cadena = 'Python'
subcadena = cadena[2:5]  # 'tho'

```
* Conversión de otros tipos de datos a cadenas:
```python
numero = 42
cadena = str(numero)  # '42'

```
>En resumen, 'str' en Python es un tipo de dato utilizado para representar cadenas de caracteres y se puede usar para manipular texto de diversas formas, como concatenación, acceso a caracteres individuales, extracción de subcadenas y conversión de otros tipos de datos a cadenas.




# int

En Python, 'int' es un tipo de dato que representa números **enteros**. Los enteros en Python pueden ser positivos o negativos y no tienen límite de tamaño, a menos que se supere la cantidad de memoria disponible en el sistema.

Aquí tienes algunos ejemplos de cómo usar int en Python:

* Declaración de un número entero:

```python
numero_entero = 42

```
* Operaciones aritméticas con números enteros:

```python
suma = 10 + 20
resta = 50 - 30
multiplicacion = 5 * 6
division = 100 / 4

```
* Conversión de cadenas a números enteros:

```python
cadena = '42'
numero_entero = int(cadena)  # 42

```
* Representación en base numérica:

```python
numero_binario = 0b1010  # Representación binaria de 10
numero_octal = 0o12  # Representación octal de 10
numero_hexadecimal = 0xA  # Representación hexadecimal de 10

```
> En resumen, int en Python es un tipo de dato utilizado para representar números enteros y se puede usar para realizar operaciones aritméticas, conversión de cadenas a enteros y representación en diferentes bases numéricas.

# sangrado / indentación

El sangrado en Python se refiere a la forma en que se estructura el código utilizando **espacios** o **tabulaciones** al principio de las líneas. En Python, el sangrado es crucial ya que se utiliza para delimitar bloques de código, como aquellos dentro de bucles, funciones, clases y condicionales.

Por ejemplo, en un bucle for en Python, el código dentro del bucle se identifica mediante un sangrado consistente:

```python
for i in range(5):
    print(i)  # Este print está dentro del bucle, gracias al sangrado

```
En este caso, el print(i) está dentro del bucle for porque tiene un nivel de sangrado mayor que el for i in range(5):. Si se elimina el sangrado, el código producirá un error de sintaxis.

## 4 espacios

El sangrado en Python suele hacerse con **espacios**, siendo recomendado usar **4 espacios** por nivel de sangrado, aunque también se puede usar una tabulación (aunque es menos común y puede causar problemas de consistencia si se mezclan tabulaciones y espacios).

Es importante mantener una consistencia en el uso del sangrado a lo largo de todo el código, ya que Python utiliza el sangrado como parte de su sintaxis. Un cambio en el sangrado puede cambiar la estructura del código y, por lo tanto, su significado.

>En resumen, el sangrado en Python es una parte fundamental de su sintaxis y se utiliza para delimitar bloques de código, como bucles, funciones, clases y condicionales. Es importante mantener un sangrado consistente para garantizar la legibilidad y funcionalidad del código.