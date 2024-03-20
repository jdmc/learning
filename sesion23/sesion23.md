
[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# pydoc

**pydoc** es una herramienta de documentación incluida en Python que se utiliza para generar documentación a partir de módulos, clases, funciones y métodos escritos en Python. Proporciona una interfaz de línea de comandos y una interfaz web para acceder a la documentación generada.

Las principales funciones de pydoc incluyen:

1. Generación de documentación: Puedes utilizar pydoc para generar documentación a partir de módulos, clases, funciones y métodos escritos en Python. La documentación se genera automáticamente a partir de los docstrings (cadenas de documentación) que se incluyen en el código fuente de Python.

2. Acceso a la documentación: Puedes utilizar pydoc para acceder a la documentación de los módulos, clases, funciones y métodos directamente desde la línea de comandos o a través de una interfaz web. Esto te permite consultar la documentación de cualquier parte del código Python sin necesidad de navegar por los archivos de código fuente.

3. Búsqueda de módulos y funciones: pydoc proporciona una función de búsqueda que te permite buscar módulos y funciones por nombre. Esto puede ser útil cuando estás buscando documentación sobre una función específica o tratando de encontrar un módulo que proporciona cierta funcionalidad.

4. Servidor web integrado: pydoc incluye un servidor web integrado que te permite acceder a la documentación a través de un navegador web. Esto puede ser útil si prefieres navegar por la documentación de forma interactiva o si estás trabajando en un entorno donde no tienes acceso a la línea de comandos.

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

[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 