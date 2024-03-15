import json

# Abre el archivo nearby.json en modo lectura
with open('nearby.json', 'r') as archivo:
    # Carga el contenido del archivo JSON en una estructura de datos de Python
    datos = json.load(archivo)

# Ahora puedes trabajar con los datos como lo harías con cualquier otra estructura de datos de Python
print(datos)
