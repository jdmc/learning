# Exceptions

Las excepciones son un mecanismo para **controlar los errores** en Python.

Cuando se produce un error en un programa, se lanza una excepción. 
La excepción contiene información sobre el error, como el tipo de error y la ubicación donde se produjo.

#### El programa puede manejar la excepción de diferentes maneras:

**Capturar la excepción**: Se puede usar un bloque try-except para capturar la excepción y realizar una acción específica.
**Propagar la excepción**: Se puede permitir que la excepción se propague a una función que la llame.
**Ignorar la excepción**: En algunos casos, se puede ignorar la excepción.

#### Ventajas de usar excepciones:

**Mejora la robustez del programa:**    
El programa puede continuar ejecutándose incluso si se produce un error.

**Facilita la depuración:**    
 Las excepciones proporcionan información útil sobre los errores.

**Mejora la legibilidad del código:**    
 El código es más fácil de leer y entender.

#### Tipos de excepciones:

**Excepciones estándar:**     
Son excepciones que forman parte de la instalación estándar de Python.    

**Excepciones personalizadas:**    
 Son excepciones que se crean por el usuario.

```python
diccionario  = dict(a=1, b=2)

try:
    #resultado = 14 / 0
    #print(resultado)
    data = diccionario["c"]

except (ZeroDivisionError, TypeError):
    print("El error es de tipo numerico")
except KeyError as kex:
    print(f"Clave inexistente:{kex}")
except Exception as ex:
    print(f"Ha habido un error: {ex}")


def convertir_a_entero(data:str) -> int:
    resultado = None
    try:
        resultado = int(data)
    except ValueError:
        pass
    
    return resultado

resultado_entero = convertir_a_entero("Hola")



diccionario = {
    "111H": "Juan",
    "222H": "Paloma"
}

try:
    #del diccionario
    diccionario["111H"] = "Miguel"
    print(diccionario)
except NameError:
    print("Diccionario no existente")
except Exception:
    print("Error general")
else:
    print("Se ha completado satisfactoriamente la operacion")
finally:
    print("Operacion terminada")

    ```





