
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

>En resumen, la estrategia AAA consiste en Preparar el entorno de prueba, Actuar sobre el código que se está probando y Afirmar que el resultado es el esperado. Esta estrategia ayuda a escribir pruebas unitarias claras, concisas y efectivas que son fáciles de mantener y entender.

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 