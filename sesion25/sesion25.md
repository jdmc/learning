[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Data Science Python

La ciencia de datos en Python es el proceso de utilizar el lenguaje de programación Python y sus bibliotecas especializadas para recopilar, limpiar, analizar y visualizar datos con el objetivo de obtener información significativa y tomar decisiones informadas.

Python es ampliamente utilizado en la ciencia de datos debido a su facilidad de uso, su amplia variedad de bibliotecas especializadas y su capacidad para trabajar con grandes conjuntos de datos. Algunas de las bibliotecas más populares para la ciencia de datos en Python incluyen:

1. **NumPy**:     
  Para realizar cálculos numéricos y operaciones en matrices y arreglos multidimensionales.
2. **Pandas**:     
  Para manipulación y análisis de datos estructurados, ofreciendo estructuras de datos flexibles como DataFrames.
3. **Matplotlib y Seaborn**:    
   Para visualización de datos, creando gráficos y visualizaciones informativas.
   [Matplotlib](https://github.com/matplotlib/matplotlib?tab=readme-ov-file)
4. **Scikit-learn**:     
  Para aprendizaje automático y modelado predictivo, ofreciendo una amplia gama de algoritmos y herramientas para análisis predictivo.
5. **TensorFlow** y **PyTorch**: Para aprendizaje profundo (deep learning), permitiendo construir, entrenar y desplegar modelos de redes neuronales.

La ciencia de datos en Python implica un proceso iterativo que incluye la comprensión del problema, la adquisición y limpieza de datos, la exploración y análisis de los mismos, la modelización y evaluación de los resultados, y finalmente la comunicación de los hallazgos obtenidos. Es una disciplina interdisciplinaria que combina habilidades de programación, matemáticas, estadísticas y dominio del campo de aplicación específico para resolver problemas complejos y extraer conocimientos valiosos de los datos.

## ETL 

ETL es un acrónimo que significa **Extract**, **Transform**, **Load**, que en español se traduce como Extraer, Transformar y Cargar. Se refiere a un proceso utilizado en la integración y preparación de datos en la ciencia de datos y la gestión de bases de datos.

* **Extract (Extraer)**:  En esta etapa, los datos se extraen de una o varias fuentes de datos, que pueden ser bases de datos, archivos planos, sistemas en la nube, servicios web, entre otros. La extracción puede implicar la lectura de datos de diferentes formatos y fuentes, y su traslado a un área de almacenamiento temporal.

* **Transform (Transformar)**: Una vez que los datos se han extraído, se someten a un proceso de transformación. Durante esta etapa, los datos se limpian, se filtran, se agregan, se modifican o se combinan según sea necesario para cumplir con los requisitos específicos del análisis o del sistema de destino. Esto puede incluir la normalización de datos, la conversión de tipos de datos, la eliminación de duplicados y la creación de nuevas columnas o conjuntos de datos derivados.

* **Load (Cargar)**: Finalmente, los datos transformados se cargan en el sistema de destino, que puede ser una base de datos, un almacén de datos, un lago de datos o cualquier otro repositorio donde se utilizarán para análisis, informes o aplicaciones. La carga de datos puede implicar la inserción de datos en tablas existentes, la creación de nuevas tablas o la actualización de conjuntos de datos existentes.

El proceso **ETL** es fundamental para garantizar la integridad, calidad y disponibilidad de los datos utilizados en proyectos de ciencia de datos, inteligencia empresarial, análisis de datos y otras aplicaciones. Permite consolidar datos de múltiples fuentes, prepararlos para su análisis y asegurar que estén listos para su uso en diferentes sistemas y aplicaciones.

# Pandas

## ¿Qué es Pandas?
Pandas es una biblioteca de código abierto en Python que proporciona estructuras de datos de alto rendimiento y fáciles de usar, así como herramientas de análisis de datos. Es ampliamente utilizado en la comunidad de ciencia de datos y análisis financiero debido a su capacidad para manipular y analizar datos de manera eficiente.

## ¿Para qué se utiliza Pandas?
Pandas se utiliza principalmente para la manipulación, limpieza, transformación y análisis de datos estructurados y etiquetados. Algunos casos de uso comunes incluyen:

1. Exploración y preparación de datos: Pandas permite cargar datos desde una variedad de fuentes (archivos CSV, Excel, bases de datos, etc.) y explorarlos para comprender su estructura y contenido.
2. Limpieza y transformación de datos: Facilita la limpieza de datos eliminando valores nulos, manejo de valores atípicos, normalización de datos, y transformaciones complejas como la agregación y la combinación de datos.
3. Análisis y manipulación de datos: Proporciona herramientas para realizar operaciones de filtrado, selección, agrupación y agregación de datos, así como para calcular estadísticas descriptivas y aplicar funciones personalizadas a los datos.
4. Visualización de datos: Aunque Pandas no es una biblioteca de visualización, se integra bien con bibliotecas de visualización como Matplotlib y Seaborn para crear gráficos y visualizaciones a partir de datos.

## ¿Cómo se utiliza Pandas?
Pandas se importa típicamente como **import pandas as pd**. Las dos estructuras de datos principales en Pandas son **Series** y **DataFrame**:

* **Series**: Es una estructura de datos unidimensional que puede contener datos de cualquier tipo.
* **DataFrame**: Es una estructura de datos bidimensional similar a una tabla de base de datos, que consta de filas y columnas etiquetadas.

Para utilizar Pandas, primero se cargan los datos en un DataFrame utilizando funciones como **pd.read_csv()** o **pd.read_excel()**. Una vez cargados los datos, se pueden realizar diversas operaciones como filtrado, selección, agregación, transformación y visualización utilizando métodos y funciones proporcionados por Pandas.

## Ventajas de Pandas:

1. Eficiencia en el manejo de datos: Pandas está diseñado para manejar eficientemente grandes conjuntos de datos, lo que lo hace adecuado para aplicaciones de análisis de datos.
2. Flexibilidad en la manipulación de datos: Ofrece una amplia gama de funciones y métodos para manipular y transformar datos de manera flexible.
3. Integración con otras bibliotecas: Se integra bien con otras bibliotecas populares de Python como NumPy, Matplotlib y Scikit-learn, lo que permite realizar análisis de datos complejos y generar visualizaciones informativas.
4. Documentación detallada y comunidad activa: Pandas cuenta con una documentación detallada y una comunidad activa de usuarios que proporcionan soporte y recursos adicionales para aprender y utilizar la biblioteca de manera efectiva.

>En resumen, Pandas es una herramienta poderosa y versátil para el análisis de datos en Python, que proporciona una amplia gama de funcionalidades para manipular, limpiar y analizar datos de manera eficiente y efectiva. Es una biblioteca fundamental para cualquier persona que trabaje con datos en Python.

## Parámetros

Dentro de Pandas, hay una amplia variedad de parámetros que se pueden utilizar en varias funciones y métodos para personalizar el comportamiento de las operaciones realizadas en los datos. Aquí hay una lista de algunos de los parámetros más comunes utilizados en Pandas:

1. index: Permite especificar o cambiar el índice de un DataFrame o Serie.
2. columns: Permite especificar o cambiar los nombres de las columnas de un DataFrame.
3. dtype: Define el tipo de datos de las columnas de un DataFrame o Serie.
4. axis: Indica si una operación se realiza a lo largo de filas (axis=0) o columnas (axis=1).
5. dropna: Controla si se eliminan las filas o columnas que contienen valores nulos durante la limpieza de datos.
6. na_values: Especifica los valores que se consideran como nulos al leer datos desde un archivo.
7. keep_default_na: Controla si se mantienen los valores predeterminados que se consideran nulos al leer datos desde un archivo.
8. sep: Especifica el delimitador utilizado al leer datos desde un archivo de texto.
9. header: Indica qué fila se utiliza como encabezado al leer datos desde un archivo.
10. parse_dates: Indica si se deben analizar automáticamente las fechas al leer datos desde un archivo.
11. encoding: Especifica la codificación utilizada al leer datos desde un archivo de texto.
12. na_filter: Controla si se realiza el filtrado de valores nulos al leer datos desde un archivo.
13. skiprows: Especifica las filas que se deben omitir al leer datos desde un archivo.
14. nrows: Limita el número de filas que se leen al cargar datos desde un archivo.
15. chunksize: Divide el archivo en bloques de tamaño especificado al leer datos desde un archivo grande.

Estos son solo algunos de los parámetros comunes que se encuentran en Pandas. La biblioteca ofrece una amplia gama de funcionalidades y, por lo tanto, una variedad de parámetros que se pueden utilizar para adaptarse a diferentes escenarios de análisis de datos. Consultar la documentación oficial de Pandas proporciona una lista completa de parámetros disponibles para cada función y método.

## Métodos

1. head() y tail(): Devuelven las primeras o últimas filas del DataFrame, respectivamente.

2. info(): Proporciona información sobre el DataFrame, incluyendo el tipo de datos de cada columna y la cantidad de valores no nulos.

3. describe(): Calcula estadísticas descriptivas para cada columna numérica en el DataFrame, como la media, la mediana, el mínimo, el máximo y los cuartiles.

4. unique() y nunique(): Devuelven los valores únicos en una columna y el número de valores únicos, respectivamente.

5. value_counts(): Devuelve la frecuencia de cada valor único en una columna.

6. sort_values() y sort_index(): Ordena el DataFrame por los valores de una columna específica o por el índice, respectivamente.

7. isnull() y notnull(): Devuelven una máscara booleana que indica dónde hay valores nulos o no nulos, respectivamente.

8. drop() y dropna(): Eliminan filas o columnas que contienen valores nulos, respectivamente.

9. fillna(): Rellena los valores nulos en el DataFrame con un valor específico.

10. apply(): Aplica una función a cada elemento del DataFrame.

11. pivot_table(): Crea una tabla dinámica a partir de un DataFrame.

12. merge() y concat(): Combina múltiples DataFrames en uno solo, ya sea mediante la concatenación o la combinación de datos.

13. to_csv() y to_excel(): Guarda el DataFrame en un archivo CSV o Excel, respectivamente.

14. mean(): Este método se utiliza para calcular la media de los valores en un DataFrame o Serie. Por ejemplo, df.mean() calculará la media de cada columna en el DataFrame df.

15. groupby(): Este método se utiliza para agrupar los datos en un DataFrame según los valores de una o más columnas y luego aplicar una función a cada grupo. Por ejemplo, df.groupby('columna').mean() agrupará los datos en el DataFrame df por los valores únicos en la columna especificada y luego calculará la media de cada grupo.

Estos son solo algunos de los muchos métodos disponibles en Pandas. La biblioteca ofrece una amplia gama de herramientas para manipular y analizar datos de manera eficiente en Python. Explorar la documentación oficial de Pandas proporciona una lista completa de métodos y funciones disponibles, así como ejemplos de su uso.

## Pandas VS Excel

Pandas y Excel son dos herramientas utilizadas para tratar datos, pero difieren en varios aspectos:

1. Tipo de herramienta:

* Pandas: Es una biblioteca de Python diseñada específicamente para el análisis y manipulación de datos.
* Excel: Es una aplicación de hoja de cálculo desarrollada por Microsoft.

2. Entorno de trabajo:

* Pandas: Se utiliza en un entorno de programación de Python, lo que permite automatizar tareas, realizar análisis avanzados y trabajar con grandes volúmenes de datos de manera eficiente.
* Excel: Es una herramienta de software de escritorio que proporciona una interfaz gráfica de usuario para trabajar con datos de forma interactiva y visual.

3. Capacidad de automatización:

* Pandas: Permite la automatización de tareas repetitivas y el desarrollo de flujos de trabajo complejos mediante scripts y programación.
* Excel: Ofrece capacidades limitadas para la automatización de tareas y análisis avanzados, especialmente para conjuntos de datos grandes o complejos.

4. Escalabilidad:

* Pandas: Es más escalable y eficiente para manejar grandes volúmenes de datos, ya que está optimizado para el análisis de datos a gran escala.
* Excel: Puede volverse lento o tener limitaciones de rendimiento al manejar conjuntos de datos grandes debido a las limitaciones de memoria y procesamiento.

5. Flexibilidad:

* Pandas: Ofrece una amplia gama de funciones y métodos para manipular, limpiar, transformar y analizar datos de manera flexible y eficiente.
* Excel: Proporciona una variedad de funciones y herramientas para el análisis de datos, pero puede tener limitaciones en términos de complejidad y flexibilidad en comparación con Pandas.

6. Colaboración y compatibilidad:

* Pandas: Al ser una biblioteca de Python, puede integrarse fácilmente con otras herramientas y bibliotecas de análisis de datos en el ecosistema de Python. También es compatible con varios formatos de archivo, incluidos CSV, Excel, SQL, entre otros.
* Excel: Es ampliamente utilizado y tiene una amplia compatibilidad con otros programas de Microsoft Office. Facilita la colaboración y el intercambio de datos entre usuarios que están familiarizados con la aplicación.

>En resumen, Pandas y Excel son herramientas útiles para tratar datos, pero difieren en su enfoque, capacidades y entorno de trabajo. Pandas es más adecuado para análisis de datos avanzados, automatización y trabajo con grandes volúmenes de datos, mientras que Excel es más adecuado para tareas básicas de análisis de datos y visualización interactiva. La elección entre Pandas y Excel depende de las necesidades específicas del proyecto y las preferencias del usuario.









[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 