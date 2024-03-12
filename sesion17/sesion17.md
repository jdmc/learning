# Files

En Python, los archivos son objetos que representan archivos en el sistema de archivos de la computadora. Estos archivos pueden ser de diferentes tipos, como archivos de texto, archivos binarios, archivos CSV, archivos JSON, etc. Los archivos en Python son utilizados para leer datos desde archivos externos, escribir datos en archivos, manipular archivos existentes, entre otras operaciones relacionadas con archivos.

Aquí hay una breve descripción de algunos tipos de archivos comunes en Python y cómo se utilizan:

**Archivos de texto**: Estos son archivos que contienen texto sin formato. Se pueden leer y escribir utilizando funciones como open(), read(), write(), etc.

```python
# Ejemplo de lectura de un archivo de texto
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)

```

**Archivos binarios**: Estos son archivos que contienen datos binarios en lugar de texto. Se utilizan para almacenar datos que no son texto, como imágenes, videos, archivos ejecutables, etc. Se pueden leer y escribir de manera similar a los archivos de texto, pero con diferentes modos de apertura (rb para leer en modo binario, wb para escribir en modo binario, etc.).

```python
# Ejemplo de lectura de un archivo binario
with open('imagen.png', 'rb') as archivo:
    contenido = archivo.read()

```

**Archivos CSV (Comma-Separated Values)**: Son archivos que contienen datos tabulares, donde los valores están separados por comas u otros delimitadores. Python proporciona el módulo csv para leer y escribir archivos CSV de manera fácil y eficiente.