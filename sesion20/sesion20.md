
[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Clonaciones usando Copy

En Python, las clonaciones utilizando la función **copy()** o el módulo **copy** se refieren a la creación de una copia independiente de un objeto. Esto significa que, después de realizar una clonación, cualquier cambio realizado en el objeto original no afectará a la copia y viceversa.

Existen dos formas comunes de realizar clonaciones en Python:

**1. Clonación superficial (shallow copy)**: 
  En una clonación superficial, se crea una nueva instancia del objeto principal, pero los elementos contenidos dentro del objeto (como listas, diccionarios o cualquier objeto que contenga referencias a otros objetos) aún se comparten entre el objeto original y la copia. Se puede realizar utilizando el método copy() o la función copy.copy() del módulo copy.

  ```python
import copy

original_list = [1, 2, [3, 4]]
cloned_list = copy.copy(original_list)

# Modificar el elemento interno de la lista en la copia
cloned_list[2][0] = 5

print(original_list)  # [1, 2, [5, 4]]
print(cloned_list)    # [1, 2, [5, 4]]

  ```

**2. Clonación profunda (deep copy)**:     
  En una clonación profunda, se crea una copia completamente independiente de todos los elementos, incluidos los elementos internos. Esto significa que no hay ninguna conexión entre el objeto original y la copia. Se puede realizar utilizando el método deepcopy() del módulo copy.

  ```python
import copy

original_list = [1, 2, [3, 4]]
deep_cloned_list = copy.deepcopy(original_list)

# Modificar el elemento interno de la lista en la copia
deep_cloned_list[2][0] = 5

print(original_list)    # [1, 2, [3, 4]]
print(deep_cloned_list) # [1, 2, [5, 4]]

  ```

  Es importante elegir el tipo de clonación adecuado según las necesidades específicas de tu programa. La clonación superficial es más rápida y puede ser suficiente en muchos casos, pero si necesitas una copia completamente independiente de todos los elementos, la clonación profunda es la opción adecuada.

  ## Diferencias

  La diferencia principal entre **copy()** y **deepcopy()** radica en cómo manejan las estructuras de datos anidadas. Aquí está la diferencia:

* **copy()**: La función copy() del módulo copy realiza una clonación superficial de un objeto. Esto significa que solo se copia el objeto principal, pero los objetos anidados dentro de él (como listas, diccionarios, etc.) no se copian por completo. En cambio, las referencias a estos objetos anidados se mantienen, lo que significa que ambas copias (la original y la copia) compartirán los mismos objetos anidados. Por lo tanto, si se modifica un objeto anidado en una copia, también se verá afectado en la original y viceversa.

* **deepcopy()**: Por otro lado, la función deepcopy() del módulo copy realiza una clonación profunda de un objeto. Esto significa que no solo se copia el objeto principal, sino que también se copian todos los objetos anidados dentro de él, y todos los objetos anidados dentro de esos objetos, y así sucesivamente. Como resultado, se crea una copia completamente independiente de la estructura de datos original, donde no hay ninguna conexión entre los objetos originales y los objetos copiados. Por lo tanto, cualquier modificación realizada en un objeto copiado no afectará al objeto original y viceversa.

```python
import copy

# Estructura de datos anidada
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Copia superficial utilizando copy.copy()
copia_superficial = copy.copy(original)

# Copia profunda utilizando copy.deepcopy()
copia_profunda = copy.deepcopy(original)

# Modificar el primer elemento de la lista original
original[0][0] = 'X'

# Imprimir las estructuras de datos originales y copiadas
print("Original:")
print(original)
print("Copia Superficial:")
print(copia_superficial)
print("Copia Profunda:")
print(copia_profunda)

```

```python
Original : # original modificada 1 = X 
[['X', 2, 3], [4, 5, 6], [7, 8, 9]]
Copia Superficial:
[['X', 2, 3], [4, 5, 6], [7, 8, 9]]
Copia Profunda:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

```

Aquí está la explicación:

* En la lista original, modificamos el primer elemento de la primera sublista a 'X'.
* Como la copia superficial copia_superficial comparte las sublistas con original, también refleja el cambio realizado en la lista original.
* Sin embargo, la copia profunda copia_profunda es completamente independiente de original, por lo que no se ve afectada por el cambio en la lista original y permanece igual.

>En resumen, copy() se utiliza para crear una copia superficial que comparte objetos anidados, mientras que deepcopy() se utiliza para crear una copia profunda que no comparte ningún objeto anidado. La elección entre una u otra depende de las necesidades específicas de tu programa y de cómo quieras que se manejen las referencias a los objetos anidados.

# Nonlocal 

**nonlocal** es una palabra clave en Python que se utiliza dentro de funciones anidadas para indicar que una variable definida en un ámbito externo al ámbito local de la función debe ser considerada como no local. Esto significa que Python buscará la variable en los ámbitos exteriores al ámbito local, pero no la considerará global. nonlocal se utiliza principalmente cuando se quiere modificar una variable que está en un ámbito superior al de la función local, pero no es global.

Se utiliza cuando necesitas modificar una variable que está definida en un ámbito superior al de la función actual, pero que no es global. Es útil en situaciones donde tienes funciones anidadas y quieres actualizar una variable que pertenece al ámbito externo pero no al ámbito global.

Aquí tienes un ejemplo de cómo se utiliza nonlocal:

```python
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20

    inner_function()
    print("Valor de x después de llamar a inner_function:", x)

outer_function()

```

En este ejemplo, x está definido en outer_function(), pero queremos modificar su valor dentro de inner_function(). Usamos nonlocal x dentro de inner_function() para indicar que x se refiere a la variable x definida en outer_function(). Después de llamar a inner_function(), el valor de x se actualiza a 20 en lugar de permanecer en 10. 

La salida del código será:

```python
Valor de x después de llamar a inner_function: 20

```

# Walrus

La expresión de asignación Walrus (o simplemente "Walrus operator") es una característica introducida en Python 3.8 que permite asignar valores a variables como parte de una expresión.

Se llama "Walrus" debido a su sintaxis, que se asemeja a los ojos y colmillos de un morsa (:=).

Esta expresión es útil en situaciones donde quieres asignar un valor a una variable y al mismo tiempo usar ese valor en una expresión. Por ejemplo:

```python
# Uso tradicional sin Walrus operator
nombre = input("Ingrese su nombre: ")
if len(nombre) > 10:
    print("El nombre es muy largo")

# Uso con Walrus operator
if len((nombre := input("Ingrese su nombre: "))) > 10:
    print("El nombre es muy largo")

```

En el segundo ejemplo, la expresión nombre := input("Ingrese su nombre: ") asigna el valor ingresado por el usuario a la variable nombre y al mismo tiempo devuelve ese valor, que se usa directamente en la condición del if. Esto hace que el código sea más conciso y fácil de leer en comparación con el enfoque tradicional.

# Closure

Una clausura (closure en inglés) en Python es una función interna que recuerda y tiene acceso al ámbito en el que fue creada, incluso después de que el ámbito ha terminado de ejecutarse. En otras palabras, una clausura es una función definida dentro de otra función que tiene acceso a las variables locales de la función exterior incluso después de que la función exterior haya terminado de ejecutarse.

Las clausuras son útiles cuando quieres crear funciones que mantengan algún estado interno o que realicen acciones específicas, pero que también necesitan acceder a variables definidas en el ámbito externo. Aquí tienes un ejemplo básico de una clausura en Python:

```python
def exterior(x):
    def interior(y):
        return x + y
    return interior

funcion_clausura = exterior(10)
print(funcion_clausura(5))  # Output: 15

```

En este ejemplo, exterior() es una función que toma un argumento x y devuelve otra función llamada interior(). La función interior() suma su argumento y con x, que es una variable del ámbito exterior. Cuando llamamos a exterior(10), obtenemos una referencia a la función interior() que recuerda el valor x como 10. Luego, cuando llamamos a funcion_clausura(5), suma 5 al valor x almacenado en la clausura, produciendo 15.

# JSON

Trabajar con archivos JSON en Python es una tarea común, especialmente cuando se trata de API web o almacenamiento de datos estructurados. Aquí tienes una visión general básica de cómo trabajar con archivos JSON en Python:

**Lectura de Datos JSON**:

Puedes leer datos JSON de un archivo utilizando la función json.load():

```python
import json

# Abrir el archivo JSON
with open('datos.json', 'r') as archivo:
    # Cargar los datos JSON desde el archivo
    datos = json.load(archivo)

# Ahora 'datos' contiene el contenido del archivo JSON como un diccionario o lista de Python
print(datos)

```
**Escritura de Datos JSON**:    

Puedes escribir estructuras de datos de Python (como diccionarios o listas) en un archivo JSON usando la función json.dump():

```python
import json

# Datos de Python que se van a escribir en JSON
datos = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Nueva York'}

# Abrir el archivo JSON en modo escritura
with open('salida.json', 'w') as archivo:
    # Escribir los datos en el archivo JSON
    json.dump(datos, archivo)

```
**Manipulación de Datos JSON**:    

Una vez que hayas cargado los datos JSON en Python, puedes manipularlos como cualquier otra estructura de datos de Python. Por ejemplo:
```python
# Acceder a valores en los datos JSON cargados
print(datos['nombre'])

# Modificar valores en los datos JSON cargados
datos['edad'] = 31

# Agregar nuevos pares clave-valor
datos['país'] = 'EE. UU.'

# Convertir datos de Python de nuevo a JSON
cadena_json = json.dumps(datos)
print(cadena_json)

```
**Manejo de Errores**:    

Cuando trabajas con archivos JSON, es importante manejar posibles errores, como archivo no encontrado o formato JSON inválido. Puedes usar bloques try y except para el manejo de errores.

```python
try:
    with open('datos.json', 'r') as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("¡Archivo no encontrado!")
except json.JSONDecodeError:
    print("¡Formato JSON inválido!")

```

Estos son los pasos básicos para trabajar con archivos JSON en Python. Dependiendo de tu caso de uso específico, es posible que necesites realizar operaciones adicionales o manejar estructuras JSON más complejas.

# Plantillas (Template)

El módulo **string.Template** en Python proporciona una forma sencilla de realizar sustituciones de variables en cadenas de texto utilizando un enfoque basado en plantillas. Este módulo permite definir plantillas de cadena con marcadores de posición que luego se pueden rellenar con valores específicos.

Aquí hay algunas características importantes del módulo **string.Template**:

* **Sintaxis simple**: Las plantillas se definen utilizando **$** como prefijo para las variables. Por ejemplo, $nombre representa una variable llamada nombre.

* **Marcadores de posición seguros**: string.Template es útil cuando se trabaja con cadenas que pueden provenir de fuentes no confiables, ya que escapa automáticamente las sustituciones de variables, lo que evita ataques de inyección de código.

* **Personalizable**: Además de los marcadores de posición simples $nombre, también se pueden utilizar marcadores de posición más complejos como ${nombre}.

* **Fácil de usar**: La API del módulo es simple y fácil de entender, lo que facilita su uso para realizar sustituciones de variables en cadenas de texto.

Aquí hay un ejemplo básico de cómo usar string.Template:

```python
from string import Template

# Definir una plantilla
plantilla = Template("Hola, $nombre!")

# Rellenar la plantilla con valores
mensaje = plantilla.substitute(nombre="Juan")

# Imprimir el mensaje resultante
print(mensaje)  # Output: Hola, Juan!

```
>En resumen, **string.Template** es una herramienta útil para realizar sustituciones de variables de manera segura y sencilla en cadenas de texto en Python. Es especialmente útil en situaciones donde se requiere la generación dinámica de texto o la construcción de mensajes de salida personalizados.


[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 