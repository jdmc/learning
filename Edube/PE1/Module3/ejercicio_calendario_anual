""" Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

Si el número del año es divisible entre cuatro, es un año bisiestro >> Year / 4 
De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, es un año común. 
De lo contrario, es un año bisiesto."""

# Gregoriano = 1582

# comun = 365

# bisiesto = 366

# year_comun = year / 100 > => Año Común

# year_bisiesto = year /4 not 100 || year /100 not 400 || year /100 || year / 400  ||  year / 4 => Año Bisiesto

# usaremos el "%" para verificar si hay "resto" >> "=! 0" al dividir el año segun info aportada para definir año bisiesto o común >> Entonces, year % 4 == 0 verifica si el año es divisible por 4 sin dejar un resto, lo que indica que es un año bisiesto.


year = int(input("Introduce un año: "))

if year < 1582:
    print(f"{year}, No está dentro del período del calendario Gregoriano")
elif(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Año {year} es Bisiesto")
else:
    print(f"Año {year} es Común")