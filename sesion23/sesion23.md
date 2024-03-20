
[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# pydoc

**pydoc** es una herramienta de documentación incluida en Python que se utiliza para generar documentación a partir de módulos, clases, funciones y métodos escritos en Python. Proporciona una interfaz de línea de comandos y una interfaz web para acceder a la documentación generada.

Las principales funciones de pydoc incluyen:

1. **Generación de documentación**: Puedes utilizar pydoc para generar documentación a partir de módulos, clases, funciones y métodos escritos en Python. La documentación se genera automáticamente a partir de los docstrings (cadenas de documentación) que se incluyen en el código fuente de Python.

2. **Acceso a la documentación**: Puedes utilizar pydoc para acceder a la documentación de los módulos, clases, funciones y métodos directamente desde la línea de comandos o a través de una interfaz web. Esto te permite consultar la documentación de cualquier parte del código Python sin necesidad de navegar por los archivos de código fuente.

3. **Búsqueda de módulos y funciones**: pydoc proporciona una función de búsqueda que te permite buscar módulos y funciones por nombre. Esto puede ser útil cuando estás buscando documentación sobre una función específica o tratando de encontrar un módulo que proporciona cierta funcionalidad.

4. **Servidor web integrado**: pydoc incluye un servidor web integrado que te permite acceder a la documentación a través de un navegador web. Esto puede ser útil si prefieres navegar por la documentación de forma interactiva o si estás trabajando en un entorno donde no tienes acceso a la línea de comandos.

```python
import pydoc

# Generar documentación HTML para el módulo 'math' y guardarlo en un archivo llamado 'math_doc.html'
pydoc.writedoc('math')

# Generar documentación HTML para la clase 'str' y guardarla en un archivo llamado 'str_doc.html'
pydoc.writedoc(str)

# Generar documentación HTML para la función 'sum' y guardarla en un archivo llamado 'sum_doc.html'
pydoc.writedoc(sum)

```
Este script generará documentación en formato HTML para el módulo math, la clase str y la función sum, y guardará la documentación en archivos separados llamados math_doc.html, str_doc.html y sum_doc.html, respectivamente.

Puedes ejecutar este script en un entorno de Python para generar la documentación en HTML y luego abrir los archivos HTML generados en un navegador web para ver la documentación resultante.

>En resumen, pydoc es una herramienta útil para generar y acceder a la documentación de código Python de forma rápida y sencilla. Es una herramienta estándar en Python y está disponible para su uso en todas las instalaciones de Python.

## HTML

Puedes generar la documentación en formato HTML utilizando pydoc. Puedes hacerlo utilizando la opción -w seguida del nombre del módulo, clase, función o método para el que deseas generar la documentación en HTML.

Aquí tienes un ejemplo de cómo generar un archivo HTML de la documentación para un módulo llamado mi_modulo:

```bash

pydoc -w mi_modulo

```
Este comando generará un archivo HTML llamado mi_modulo.html en el directorio actual. Puedes abrir este archivo HTML en un navegador web para ver la documentación generada en formato HTML.

Además, puedes generar la documentación en HTML para varios elementos al mismo tiempo pasando múltiples nombres de módulos, clases, funciones o métodos como argumentos:

```bash	
pydoc -w mi_modulo mi_clase mi_funcion

```

Esto generará archivos HTML separados para cada elemento especificado.

Recuerda que para que **pydoc** funcione correctamente, es necesario que el módulo, clase, función o método tenga un docstring adecuado que pydoc pueda analizar y convertir en documentación.

## Servidor

El comando python -m pydoc -p se utiliza para iniciar un servidor web que proporciona acceso a la documentación generada para los módulos de Python. Al ejecutar este comando desde la línea de comandos, se inicia un servidor web local que escucha en un puerto específico (por defecto, el puerto 8000) y permite acceder a la documentación generada a través de un navegador web.

Aquí está el significado de cada parte del comando:

* python: Este comando invoca el intérprete de Python.
* -m pydoc: Esto indica que se debe utilizar el módulo pydoc de Python.
* -p: Esto indica que se debe iniciar un servidor web para proporcionar acceso a la documentación.

Por lo tanto, al ejecutar python -m pydoc -p desde la línea de comandos, se iniciará un servidor web local y se mostrará un mensaje en la consola que indica la URL a la que se puede acceder para ver la documentación. Por ejemplo:

```bash
Server ready at http://localhost:8000/

```
Para acceder a la documentación, simplemente abre un navegador web y visita la URL proporcionada en el mensaje de la consola. Esto abrirá la interfaz web de pydoc, donde puedes buscar y navegar por la documentación de los módulos de Python instalados en tu sistema.

## Comandos

Además del comando python -m pydoc -p, hay otros comandos útiles relacionados con pydoc que puedes utilizar desde la línea de comandos para acceder a la documentación de Python:

1. Mostrar documentación en la consola:

```bash
python -m pydoc nombre_del_modulo

```
Este comando muestra la documentación del módulo especificado directamente en la consola.

2. Generar documentación HTML:
```bash
python -m pydoc -w nombre_del_modulo

```
Este comando genera la documentación HTML del módulo especificado y guarda el resultado en un archivo HTML.

3. Buscar documentación:
```bash
python -m pydoc -k palabra_clave

```
Este comando busca módulos, clases, funciones y métodos que contengan la palabra clave especificada en sus nombres o docstrings.

4. Listar módulos disponibles:
```bash
python -m pydoc -l

```
Este comando lista todos los módulos instalados en tu sistema que pydoc puede documentar.

5. Obtener ayuda sobre comandos:
```bash
python -m pydoc -h

```
Este comando muestra una ayuda breve sobre cómo utilizar pydoc, incluyendo una lista de todos los argumentos y opciones disponibles.

Estos son algunos de los comandos más comunes que puedes utilizar con pydoc para acceder y explorar la documentación de Python desde la línea de comandos. Cada comando proporciona una forma conveniente de acceder a diferentes aspectos de la documentación de Python y puede ser útil en diferentes situaciones dependiendo de tus necesidades.

# Unit Tests

En general, las pruebas unitarias (unit tests) son una práctica de programación que implica escribir código específico para verificar que unidades individuales de código (como funciones, métodos o clases) funcionan como se espera. Estas pruebas se diseñan para validar el comportamiento de unidades de código aisladas de manera independiente de otras partes del sistema.

En Python, la biblioteca estándar **unittest** proporciona un marco de trabajo para escribir y ejecutar pruebas unitarias. **unittest** facilita la creación y ejecución de pruebas, así como la organización de pruebas en conjuntos lógicos. Aquí hay una descripción general de cómo utilizar unittest en Python:

1. Escribir pruebas:
Para comenzar a escribir pruebas unitarias con unittest, primero debes definir clases de prueba que hereden de unittest.TestCase. Dentro de estas clases, escribirás métodos de prueba que verifican el comportamiento de unidades específicas de código. 
Estos métodos de prueba suelen comenzar con el prefijo **test_**.

Por ejemplo:

```python
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_enteros(self):
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

```

2. Ejecutar pruebas:
Para ejecutar las pruebas definidas, puedes ejecutar el script directamente desde la línea de comandos. Esto ejecutará todas las pruebas definidas en el archivo.

3. Assertions:
Dentro de los métodos de prueba, se utilizan afirmaciones (assertions) para verificar que los resultados obtenidos coincidan con los resultados esperados. unittest proporciona una variedad de métodos de aserción útiles, como assertEqual, assertTrue, assertFalse, entre otros.

4. Configuración y limpieza:
unittest proporciona métodos de configuración y limpieza que te permiten ejecutar código antes y después de cada prueba, así como antes y después de cada clase de prueba.

5. Organización de pruebas:
Puedes organizar tus pruebas en módulos y clases de prueba para facilitar la gestión y ejecución de las pruebas. Además, unittest proporciona la capacidad de agrupar pruebas relacionadas en suites de pruebas.

6. Reportes de pruebas:
Después de ejecutar las pruebas, unittest proporciona informes detallados sobre los resultados de las pruebas, incluidos los casos de prueba pasados, fallados y omitidos.

>En resumen, **unittest** es una biblioteca estándar de Python que facilita la escritura y ejecución de pruebas unitarias para verificar el comportamiento de unidades de código individuales. Es una herramienta poderosa para garantizar la calidad y la integridad del código, así como para facilitar el mantenimiento y la refactorización del código.

## A A A

La estrategia AAA en el contexto de las pruebas unitarias se refiere a tres principios importantes que se deben seguir al escribir pruebas unitarias. 

Estos principios son:

1. **Arrange (Preparar)**: En esta etapa, se prepara el entorno de prueba estableciendo cualquier estado necesario o configuración inicial. Esto puede incluir la creación de objetos, la configuración de variables y la preparación de cualquier otro contexto necesario para la prueba.

2. **Act (Actuar)**: En esta etapa, se lleva a cabo la acción que se va a probar. Esto implica llamar a la función o método que se está probando y ejecutar la operación que se quiere verificar.

3. **Assert (Afirmar)**: En esta etapa, se verifica el resultado de la acción realizada en la etapa anterior. Se utiliza una afirmación (assertion) para verificar que el resultado obtenido coincida con el resultado esperado. Si la afirmación falla, significa que la prueba ha fallado.

Siguiendo esta **estrategia AAA**, las pruebas unitarias están bien organizadas y tienen una estructura clara. Esto hace que sea más fácil entender lo que está sucediendo en cada prueba y diagnosticar problemas cuando las pruebas fallan.

Supongamos que tenemos una función llamada **calcular_descuento** que toma un precio original y un porcentaje de descuento, y devuelve el precio después de aplicar el descuento. Queremos escribir una prueba unitaria para esta función utilizando la estrategia AAA.

```python
import unittest

def calcular_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_con_descuento = precio_original - descuento
    return precio_con_descuento

class TestCalcularDescuento(unittest.TestCase):
    def test_descuento_correcto(self):
        # Arrange (Preparar)
        precio_original = 100
        porcentaje_descuento = 20
        
        # Act (Actuar)
        precio_con_descuento = calcular_descuento(precio_original, porcentaje_descuento)
        
        # Assert (Afirmar)
        self.assertEqual(precio_con_descuento, 80, "El precio con descuento debería ser 80")

if __name__ == '__main__':
    unittest.main()

```

En este ejemplo:

* Arrange (Preparar): Creamos las variables precio_original y porcentaje_descuento y les asignamos los valores necesarios para la prueba.

* Act (Actuar): Llamamos a la función calcular_descuento con los valores preparados en la etapa anterior para calcular el precio con descuento.

* Assert (Afirmar): Verificamos que el resultado devuelto por la función coincida con el resultado esperado. En este caso, estamos comprobando que el precio con descuento sea 80 cuando el precio original es 100 y el porcentaje de descuento es 20.

Al seguir la estrategia AAA, la prueba unitaria está claramente estructurada y es fácil de entender. Esto hace que sea más fácil para otros desarrolladores comprender lo que está sucediendo en la prueba y diagnosticar problemas si la prueba falla.

>En resumen, la estrategia AAA consiste en Preparar el entorno de prueba, Actuar sobre el código que se está probando y Afirmar que el resultado es el esperado. Esta estrategia ayuda a escribir pruebas unitarias claras, concisas y efectivas que son fáciles de mantener y entender.

## assertions 

En el módulo **unittest** de Python, hay una variedad de métodos de **aserción (assertion)** disponibles para verificar diferentes condiciones durante las pruebas unitarias. 

Aquí hay una lista de algunos de los métodos de aserción más comunes y una descripción de lo que hacen:

1. **assertEqual(a, b, msg=None)**:
Verifica que a y b sean iguales. Si no son iguales, la prueba falla y se muestra un mensaje de error opcional (msg).

2. **assertNotEqual(a, b, msg=None)**:
Verifica que a y b no sean iguales. Si son iguales, la prueba falla y se muestra un mensaje de error opcional (msg).

3. **assertTrue(expr, msg=None)**:
Verifica que expr sea verdadero. Si expr es falso, la prueba falla y se muestra un mensaje de error opcional (msg).

4. **assertFalse(expr, msg=None)**:
Verifica que expr sea falso. Si expr es verdadero, la prueba falla y se muestra un mensaje de error opcional (msg).

5. **assertIs(a, b, msg=None)**:
Verifica que a sea b. Esto verifica si a y b son el mismo **objeto (identidad)**. Si no son el mismo objeto, la prueba falla y se muestra un mensaje de error opcional (msg).

6. **assertIsNot(a, b, msg=None)**:
Verifica que a no sea b. Esto verifica si a y b no son el mismo **objeto (identidad)**. Si son el mismo objeto, la prueba falla y se muestra un mensaje de error opcional (msg).

7. **assertRaises(exception, callable, *args, **kwargs)**:
Verifica que callable (una función o método) lance una excepción del tipo especificado (exception) cuando se llama con los argumentos args y kwargs. Si no se lanza una excepción, la prueba falla.

8. **assertIn(a, b, msg=None)**:
Verifica que a esté en b. Esto verifica si a es un elemento de b. Si a no está en b, la prueba falla y se muestra un mensaje de error opcional (msg).

9. **assertNotIn(a, b, msg=None)**:
Verifica que a no esté en b. Esto verifica si a no es un elemento de b. Si a está en b, la prueba falla y se muestra un mensaje de error opcional (msg).

10. **assertIsNone(a, msg=None)**:
Verifica que a sea None. Si a no es None, la prueba falla y se muestra un mensaje de error opcional (msg).

11. **assertIsInstance(obj, cls, msg=None)**:
Verifica que obj sea una instancia de la clase cls. Si obj no es una instancia de cls, la prueba falla y se muestra un mensaje de error opcional (msg).

Estos son solo algunos de los métodos de aserción disponibles en unittest. Cada método se puede utilizar para verificar diferentes condiciones durante las pruebas unitarias y proporciona información detallada sobre lo que falló si la prueba no pasa.

### msg=None

En el caso de los métodos de aserción en el módulo unittest de Python, si la prueba pasa sin problemas, no se muestra ningún mensaje. Sin embargo, si se proporciona un mensaje opcional (msg) y la prueba falla, ese mensaje se incluirá en la salida de la prueba como parte de la explicación del fallo.

Por ejemplo, considera este código de prueba:

```python
import unittest

class TestEjemplo(unittest.TestCase):
    def test_algo(self):
        self.assertEqual(1, 1, "1 no es igual a 1")

if __name__ == '__main__':
    unittest.main()

```
En este caso, la prueba test_algo verifica que 1 sea igual a 1. Como es de esperar, esta prueba pasará sin problemas. Si ejecutas este código, no verás ningún mensaje de salida, porque la prueba pasa y no se necesita ninguna explicación adicional.

Ahora, si cambiamos el valor esperado en la aserción para que falle:

```python
import unittest

class TestEjemplo(unittest.TestCase):
    def test_algo(self):
        self.assertEqual(1, 2, "1 no es igual a 2")

if __name__ == '__main__':
    unittest.main()

```
En este caso, la prueba fallará, y verás un mensaje de salida que incluye el mensaje opcional proporcionado:

```bash
F
======================================================================
FAIL: test_algo (__main__.TestEjemplo)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 5, in test_algo
    self.assertEqual(1, 2, "1 no es igual a 2")
AssertionError: 1 no es igual a 2

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

```
Como puedes ver, el mensaje "1 no es igual a 2" se muestra junto con la descripción de la prueba que falló. Esto ayuda a identificar rápidamente qué esperaba la prueba y por qué falló.

## Métodos Especiales

En el contexto de las pruebas unitarias, **setUp** y **tearDown** son métodos especiales que se pueden definir en una clase de prueba (heredando de unittest.TestCase) para configurar y limpiar el entorno de prueba antes y después de cada método de prueba dentro de esa clase.

1. setUp: Este método se llama antes de ejecutar cada método de prueba en la clase de prueba. Se utiliza para configurar el entorno de prueba necesario, como la creación de objetos o la inicialización de variables, que son comunes a todas las pruebas en la clase.

2. tearDown: Este método se llama después de ejecutar cada método de prueba en la clase de prueba. Se utiliza para limpiar y restaurar el estado del entorno de prueba a su estado original, por ejemplo, cerrar conexiones de bases de datos o liberar recursos utilizados en las pruebas.

Estos métodos son útiles para evitar la **duplicación** de código en las pruebas y garantizar que cada prueba se ejecute en un entorno de prueba limpio y consistente.

Respecto a las versiones de **clase** en unittest, se refiere a cómo se organizan y ejecutan las pruebas dentro de las clases de prueba. unittest proporciona dos estilos de clases de prueba: el estilo antiguo basado en funciones y el estilo basado en clases.

* **Estilo basado en funciones**: 
  En este estilo, las pruebas son simplemente funciones dentro de un módulo de prueba, y las clases de prueba no se utilizan. Cada función de prueba comienza con el prefijo test_. Este estilo es más simple y adecuado para pruebas simples.

```python
import unittest

def test_suma():
    assert suma(1, 2) == 3

def test_resta():
    assert resta(5, 3) == 2

if __name__ == '__main__':
    unittest.main()

```
* **Estilo basado en clases**: 
  En este estilo, las pruebas están organizadas en clases de prueba que heredan de unittest.TestCase. Cada método de prueba dentro de la clase comienza con el prefijo test_. Este estilo es más flexible y permite la organización de pruebas más complejas y la reutilización de código de configuración y limpieza.

```python
import unittest

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

if __name__ == '__main__':
    unittest.main()

```
Ambos estilos son válidos y pueden ser utilizados según la preferencia del desarrollador y la complejidad de las pruebas.

## skipping

En el contexto de las pruebas unitarias, skip no es un método especial, sino una función o decorador que se utiliza para indicar que una prueba debe ser omitida o saltada. Esto puede ser útil cuando una prueba no es aplicable en ciertas circunstancias o cuando se está trabajando en una característica que aún no está implementada.

unittest proporciona varias formas de omitir pruebas:

* **unittest.skip(reason)**: 
  Esta función se utiliza como un decorador para indicar que una prueba debe ser omitida. Puedes proporcionar una razón opcional para explicar por qué la prueba se está omitiendo.

```python
import unittest

class TestOperaciones(unittest.TestCase):
    @unittest.skip("Prueba no aplicable en esta versión")
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)

if __name__ == '__main__':
    unittest.main()

```
* **unittest.skipIf(condition, reason)**: 
  Esta función se utiliza como un decorador para omitir una prueba si la condición dada es verdadera.

```python
import unittest

class TestOperaciones(unittest.TestCase):
    @unittest.skipIf(sys.version_info < (3, 7), "Prueba no aplicable en Python menor a 3.7")
    def test_division(self):
        self.assertEqual(division(6, 2), 3)

if __name__ == '__main__':
    unittest.main()

```

* **unittest.skipUnless(condition, reason)**: 
  Esta función se utiliza como un decorador para omitir una prueba a menos que la condición dada sea verdadera.

```python
import unittest

class TestOperaciones(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith("win"), "Prueba solo aplicable en Windows")
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

if __name__ == '__main__':
    unittest.main()

```

Estas funciones de omisión son útiles cuando necesitas controlar qué pruebas se ejecutan en función de ciertas condiciones o circunstancias, permitiéndote mantener tus pruebas organizadas y relevantes para el contexto de desarrollo.

## pytest


[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 