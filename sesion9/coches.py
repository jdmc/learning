""" La función os.path.join() en Python se utiliza para construir rutas de archivos y directorios de forma segura y portable. 
Toma una serie de partes de la ruta como argumentos y las une utilizando el separador de directorios adecuado para el sistema operativo en el que se está ejecutando el código. Por ejemplo, en sistemas Windows utiliza \ como separador de directorios, mientras que en sistemas Unix y macOS utiliza /.

Por ejemplo, si tienes las partes de la ruta como strings, puedes usar os.path.join() para unirlas de manera segura:
    
    import os

parte1 = 'ruta'
parte2 = 'a'
parte3 = 'archivo.txt'

ruta_completa = os.path.join(parte1, parte2, parte3)
print(ruta_completa)

Este código imprimirá la ruta completa como 'ruta/a/archivo.txt' en sistemas Unix o macOS, y 'ruta\\a\\archivo.txt' en sistemas Windows.

os.path.join() es útil porque maneja automáticamente el uso del separador de directorios correcto, 
lo que hace que tu código sea más portable y menos propenso a errores al trabajar con rutas de archivos y directorios en diferentes sistemas operativos.
 """
import os
import json

coche = None

# Obtener la ruta del directorio actual del script
dir_actual = os.path.dirname(__file__)

# Construir la ruta relativa al archivo coches.json
ruta_archivo = os.path.join(dir_actual, 'data', 'coches.json')

""" # Abrir y cargar el archivo JSON
with open(ruta_archivo, 'r') as f:
    coche = json.load(f) """
    
def leer_json(path: str):
    coches = None
    with open(path, 'r', encoding="utf-8") as f:
        coches = json.load(f)
    return coches

def escribir_json(path: str, data) -> bool:
    assert data is not None, "Data ni puede ser nula!!"
    resultado = None
    try:
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f)
            resultado = True
    except:
        resultado = False
    
    return resultado

coches = leer_json(ruta_archivo)
coches.append({'marca':'Toyota', 'modelo':'Prius'})

if escribir_json(ruta_archivo, coches):
    print("Operacion completada con exito")
else:
    print("Hubo un fallo en la operacion")

#print(coches)

cadena_json = '[{"marca": "Seat", "modelo": "Arkana"}, {"marca": "Seat", "modelo": "Leon"}, {"marca": "Citroen", "modelo": "Berlingo"}, {"marca": "Toyota", "modelo": "Prius"}]'
coches_api = json.loads(cadena_json)
#print(coches_api)

#dump json cadena
print(json.dumps(coches_api))
print(type(json.dumps(coches_api)))