import json

# Abre el archivo nearby.json en modo lectura
with open('nearby.json', 'r') as archivo:
    # Carga el contenido del archivo JSON en una estructura de datos de Python
    datos = json.load(archivo)

# Ahora puedes trabajar con los datos como lo harías con cualquier otra estructura de datos de Python
for clave, dict_anidado in datos.items():
    print(clave)
    for clave2, valor2 in dict_anidado.items():
        print(f"{clave2!r}: {valor2!r}")
        

""" La letra r dentro de una cadena de formato en Python indica que el valor debería ser representado utilizando su representación "repr" en lugar de su representación "str". 
La representación "repr" intenta mostrar el valor de una manera que sea lo más cercana posible a su definición en el código fuente, 
mientras que la representación "str" está más orientada hacia la legibilidad humana. 
Esto es útil para depurar y entender exactamente qué contiene una variable, especialmente si es un objeto complejo.


El !r dentro de la cadena de formato indica que el valor debe ser representado utilizando su representación "repr". 
En otras palabras, !r le dice a Python que utilice la función repr() para obtener una representación del objeto en lugar de la función str(). """
