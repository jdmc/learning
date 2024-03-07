# diccionario

Un diccionario en Python, también conocido como "dict", 
es un tipo de dato que se utiliza para almacenar una colección de datos en forma de pares clave-valor.

## Características:

**Claves** únicas: Cada clave en un diccionario debe ser única.
**Valores**: Los valores pueden ser de cualquier tipo de dato en Python, como cadenas, números, listas o incluso otros diccionarios.
**Acceso rápido**: Los diccionarios proporcionan un acceso rápido a los valores mediante sus claves.
**Mutabilidad**: Los diccionarios son mutables, lo que significa que se pueden agregar, eliminar o modificar sus elementos después de su creación.

### Creación de un diccionario:

Se puede crear un diccionario usando dos métodos:

Notación literal:

```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

Función dict:

mi_diccionario = dict(nombre="Juan", edad=30, ciudad="Madrid")

```

### Acceso a los valores:

Se puede acceder a un valor en un diccionario usando la clave entre corchetes:

```python 


nombre = mi_diccionario["nombre"] # Almacena "Juan" en la variable nombre

``` 

Agregar elementos:

Se pueden agregar nuevos elementos a un diccionario usando la clave como índice y el valor que se desea agregar:

```python 
mi_diccionario["telefono"] = "123456789"

```

Eliminar elementos:

Se pueden eliminar elementos de un diccionario usando la función del:

```python 
del mi_diccionario["ciudad"]

```

** Iterar sobre un diccionario:

Se puede iterar sobre un diccionario usando un bucle for:

```python 

for clave in mi_diccionario:
  print(clave, mi_diccionario[clave])

```

Diccionarios y listas:

Los diccionarios son una alternativa más eficiente que las listas para almacenar datos que se pueden identificar por una clave única.

Ejemplos de uso:

Almacenar información de usuarios en un sistema.
Almacenar datos de configuración de una aplicación.
Almacenar datos de una encuesta. """

```python 

#diccionario -> estructura compuesta de pares clave:valor

diccio1 = dict(a=1,b=2,c=3)
diccio2 = {
    "a": 1,
    "b":2,
    "c":3,
}

#se accede al valor a través de la clave
#print(diccio1["f"] if "f" in diccio1 else "No accesible")

print(diccio2["a"])
#KeyError -> cuando no existe la clave por la que queremos preguntar


diccio1["d"] = 20 #alta

print(diccio1)

#edicion
diccio1["a"] = 10 #update
print(diccio1)

#procesar por lotes
new_data = {
    'h': 90,
    'm': 100
}

diccio1.update(new_data)
print(diccio1)

for clave, valor in diccio1.items():
    print(f"Clave:{clave} Valor:{valor}")


x, y, z = diccio2.items()
print(x, y, z)

valores = list(diccio2.values())
print(valores)
print(type(valores))

claves = list(diccio2.keys())
print(claves)
print(type(claves))
```

## pop vs popitem

en Python, además de "pop()", existe el método "popitem()" que también se utiliza para eliminar elementos de un diccionario. 
Sin embargo, hay diferencias importantes entre pop() y popitem().

Aquí hay una comparación entre pop() y popitem():

### pop():

Elimina un elemento del diccionario basado en la clave especificada.
Toma la clave como argumento.
Devuelve el valor asociado a esa clave.
Específicamente elimina el elemento con la clave dada.

### popitem():

**Elimina y devuelve** un par "clave-valor" arbitrario (último insertado) del diccionario.
No toma argumentos.
No se puede predecir qué elemento será eliminado, ya que el método selecciona arbitrariamente un par clave-valor para eliminar.

Es útil cuando se quiere eliminar elementos en un orden no especificado, 
por ejemplo, para procesar elementos en un diccionario en un orden aleatorio o pseudoaleatorio.

Aquí tienes un ejemplo que muestra cómo funcionan pop() y popitem():


#### Definir un diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

#### Utilizar pop() para eliminar el elemento con la clave 'b'
valor_b = mi_diccionario.pop('b')
print("Valor de 'b' eliminado:", valor_b)
print("Diccionario actualizado:", mi_diccionario)

#### Utilizar popitem() para eliminar un par clave-valor arbitrario
par_clave_valor = mi_diccionario.popitem()
print("Par clave-valor eliminado:", par_clave_valor)
print("Diccionario actualizado:", mi_diccionario)

Es importante tener en cuenta que popitem() se utiliza generalmente cuando se desea **eliminar** elementos de un diccionario sin preocuparse por el orden en que fueron insertados, 

mientras que pop() se utiliza cuando se desea eliminar un elemento específico basado en su clave.

```python

#eliminar items
item_eliminado = diccio2.pop("a")
print(diccio2, item_eliminado)

item_eliminado = diccio2.popitem()
print(diccio2)

diccio2.clear()
print(diccio2)

del diccio2
#print(diccio2)

#obtencion o lectura
valor_item = diccio1.get("a")
print(valor_item)

valor_item = diccio1.get("v", -999)
print(valor_item)


mi_diccionario = {
    'a': 100,
    'b': 200,
    'c': 300
}

papelera = dict() #vacia
par_eliminado = mi_diccionario.popitem() # tupla
papelera.update(dict([par_eliminado]))
print(papelera)



papelera.update(dict([diccio1.popitem()]))
nuevo_diccionario = dict([("a",6), ("c", 4)]) #diccio1.items() // ("a",([1,2,3])) -> dupla
papelera.update(nuevo_diccionario)

print(papelera)

```
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














