[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 

# Scrapping

El web scraping (a veces escrito como "scrapping") en Python es una técnica utilizada para extraer datos de páginas web. Esto implica escribir código para recorrer el HTML de una página web, identificar y seleccionar los elementos relevantes, y luego extraer la información deseada para su posterior análisis o almacenamiento.

Aquí hay una breve descripción de cómo y cuándo se utiliza el web scraping en Python:

## ¿Cómo utilizarlo?

**1. Seleccionar la biblioteca adecuada**:    
  Python ofrece varias bibliotecas populares para el scraping web, como BeautifulSoup y Scrapy. BeautifulSoup es más flexible y fácil de comenzar para proyectos pequeños, mientras que Scrapy es más poderoso y es útil para proyectos más grandes y complejos.

**2. Identificar el objetivo**:     
  Determine qué datos específicos necesita extraer de la página web objetivo.

**3. Analizar la estructura de la página web**:     
  Inspeccione el HTML de la página para comprender la estructura y ubicación de los datos que desea extraer.

**4. Escribir el código de scraping**:     
  Utilice las funciones proporcionadas por la biblioteca seleccionada para navegar por el HTML y extraer los datos deseados. Esto puede implicar la identificación de elementos por su clase, etiqueta, identificador u otros atributos.

**5. Procesar y almacenar los datos**:     
  Una vez que haya extraído los datos, puede procesarlos según sea necesario y almacenarlos en una base de datos, archivo CSV u otro formato.

## ¿Cuándo utilizarlo?
El web scraping en Python es útil en varias situaciones, incluyendo:

* Cuando los datos que necesita no están disponibles a través de una API.
* Para recopilar datos de múltiples fuentes en línea para análisis o investigación.
* Automatización de tareas como la recopilación de precios de productos, noticias, información financiera, etc.
* Monitorización de cambios en sitios web específicos.


## Ejemplos:
* **Extracción de precios de productos**:     
  Puede escribir un script para extraer los precios de productos de un sitio web de comercio electrónico como Amazon o eBay.

* **Recopilación de noticias**:     
  Automatice la recopilación de noticias de varios sitios web de noticias para mantenerse actualizado sobre eventos actuales.

* **Seguimiento de precios de vuelos**:     
  Escriba un programa para extraer información sobre precios de vuelos de diferentes sitios web de viajes para encontrar las mejores ofertas.

* **Análisis de datos de redes sociales**:     
  Extraiga datos de perfiles públicos de redes sociales para análisis de sentimientos, seguimiento de tendencias, etc.

Es importante tener en cuenta que al realizar web scraping, es esencial respetar los términos de servicio del sitio web objetivo y no infringir los derechos de autor u otros términos legales.

[Web Scraper y robots.txt](https://codigofacilito.com/articulos/web-scraper)

# librerias 

Existen varias bibliotecas populares en Python que se utilizan para realizar web scraping. Aquí hay algunas de las más comunes:

1. **Beautiful Soup**:     
  Es una biblioteca Python para extraer datos de archivos HTML y XML. Proporciona formas simples de navegar por la estructura del árbol del documento y extraer información útil.

2. **Scrapy**:
    
  Es un framework de scraping web de alto nivel para Python que se utiliza para extraer datos de sitios web. Es más adecuado para proyectos más grandes y complejos debido a su estructura modular y su capacidad para manejar múltiples solicitudes simultáneamente. 
  [Scrapy](https://scrapy.org/ ) 

3. **Selenium**:     
  Aunque está diseñado principalmente para pruebas automatizadas de aplicaciones web, Selenium también se puede utilizar para el scraping web. Permite la automatización del navegador web y la interacción con el contenido de una página web, lo que lo hace útil para sitios web con contenido generado dinámicamente a través de JavaScript.

4. **Requests-HTML**:     
  Es una biblioteca que se basa en las funcionalidades de la biblioteca requests para realizar solicitudes HTTP, pero también proporciona métodos para interactuar con el contenido HTML de una página web de manera similar a cómo lo haría con JavaScript en un navegador.

5. **Lxml**:     
  Es una biblioteca de procesamiento XML y HTML en Python que proporciona una interfaz similar a la de ElementTree pero con una mayor velocidad y capacidad para manejar documentos XML más grandes.

6. **PyQuery**:     
  Proporciona una sintaxis similar a la de jQuery para analizar documentos HTML y realizar selecciones de elementos.

Estas son solo algunas de las bibliotecas populares disponibles para realizar web scraping en Python. La elección de la biblioteca depende de varios factores, como la complejidad del proyecto, la estructura de la página web objetivo y las preferencias personales del desarrollador.

## Beautiful Soup

### Instalación

Si no tienes BeautifulSoup instalado, puedes instalarlo usando pip:

```bash
pip install beautifulsoup4

```

### Ejemplo básico de extracción de texto de una página web:

Supongamos que queremos extraer el título y el primer párrafo de un artículo de Wikipedia sobre Python:

```python
import requests
from bs4 import BeautifulSoup

# URL del artículo de Wikipedia sobre Python
url = 'https://es.wikipedia.org/wiki/Python'

# Realizamos la solicitud GET
response = requests.get(url)

# Creamos un objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extraemos el título
title = soup.find('h1', id='firstHeading').text
print('Título:', title)

# Extraemos el primer párrafo del contenido
first_paragraph = soup.find('div', class_='mw-parser-output').p.text
print('Primer párrafo:', first_paragraph)

```

### Ejemplo de extracción de enlaces de una página web:

Supongamos que queremos extraer todos los enlaces de la página de inicio de Wikipedia:

```python
import requests
from bs4 import BeautifulSoup

# URL de la página de inicio de Wikipedia
url = 'https://es.wikipedia.org/'

# Realizamos la solicitud GET
response = requests.get(url)

# Creamos un objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extraemos todos los enlaces (<a>) de la página
links = soup.find_all('a')

# Mostramos los enlaces
for link in links:
    print(link.get('href'))

```

Estos son solo ejemplos básicos para empezar con BeautifulSoup. Puedes realizar una variedad de operaciones más complejas, como navegar por la estructura del árbol HTML, buscar elementos específicos por etiqueta, clase, identificador, etc., y extraer datos más detallados según tus necesidades. Recuerda siempre respetar los términos de servicio de los sitios web y no abusar del scraping web.


## Scrapy

Scrapy es un framework de scraping web de alto nivel en Python que facilita la extracción de datos de sitios web de manera eficiente. A diferencia de Beautiful Soup, que es una biblioteca para análisis de HTML y XML, Scrapy es un framework completo que proporciona una estructura y funcionalidades para construir y ejecutar spiders (arañas), que son programas diseñados para realizar el scraping web de manera sistemática.

Aquí tienes más información sobre Scrapy:

### Características principales:

* **Arquitectura escalable**:     
  Scrapy está diseñado para ser escalable y puede manejar grandes volúmenes de datos y páginas web de manera eficiente.

* **Selección y extracción de datos**:     
  Proporciona un conjunto de selectores para identificar y extraer datos específicos de una página web, incluyendo XPath y selectores CSS.

* **Manejo de solicitudes y respuestas HTTP**:     
  Scrapy maneja automáticamente las solicitudes y respuestas HTTP, lo que facilita el scraping de múltiples páginas y sitios web.

* **Middleware y pipelines personalizables**:     
  Permite personalizar el comportamiento de las solicitudes y respuestas HTTP, así como el procesamiento de los datos extraídos.

* **Programación asincrónica**:     
  Scrapy utiliza Twisted, un framework para programación asincrónica en Python, lo que permite realizar múltiples solicitudes de forma simultánea y eficiente.

  ### Ejemplo básico de uso de Scrapy:
Para comenzar a usar Scrapy, primero necesitas instalarlo. Puedes instalarlo usando pip:

```bash
pip install scrapy

```
Luego, puedes crear un nuevo proyecto de Scrapy utilizando el comando scrapy startproject:

```bash
scrapy startproject myproject
cd myproject

```

Dentro del proyecto, puedes definir spiders para realizar scraping web. Por ejemplo, aquí tienes un ejemplo de una spider simple para extraer los títulos de los artículos de Wikipedia:

```python
import scrapy

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    start_urls = ['https://es.wikipedia.org/wiki/Python']

    def parse(self, response):
        for title in response.css('h1'):
            yield {'title': title.css('::text').get()}

```
Puedes ejecutar esta spider utilizando el comando scrapy crawl:

```bash
scrapy crawl wikipedia -o output.json

```

Esto ejecutará la spider y guardará los resultados en un archivo JSON llamado output.json.

### Recursos adicionales:

* [Documentación oficial de Scrapy](https://docs.scrapy.org/en/latest/)
* [Tutoriales y ejemplos de Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)

Scrapy es una herramienta poderosa para el scraping web en Python, especialmente para proyectos más grandes y complejos que requieren un manejo avanzado de solicitudes, navegación y extracción de datos.

# XML

XML (eXtensible Markup Language) es un formato de datos que se utiliza para almacenar y transportar información de manera legible tanto para humanos como para máquinas. En Python, puedes trabajar con XML utilizando varias bibliotecas, siendo las dos más comunes:


* ElementTree: Esta es una biblioteca de la biblioteca estándar de Python que proporciona una forma simple de analizar y trabajar con XML. Puedes crear árboles de elementos XML y manipularlos fácilmente. Aquí hay un ejemplo básico de cómo usar ElementTree:

```python
import xml.etree.ElementTree as ET

# Analizar un archivo XML
tree = ET.parse('archivo.xml')
root = tree.getroot()

# Iterar sobre los elementos
for child in root:
    print(child.tag, child.attrib)

# Acceder a elementos específicos
print(root[0].text)

```

* lxml: Esta es una biblioteca de Python más completa y eficiente para trabajar con XML y HTML. Proporciona una interfaz más rica y potente que ElementTree. Aquí hay un ejemplo básico de cómo usar lxml:

```python
from lxml import etree

# Analizar un archivo XML
tree = etree.parse('archivo.xml')
root = tree.getroot()

# Iterar sobre los elementos
for child in root:
    print(child.tag, child.attrib)

# Acceder a elementos específicos
print(root[0].text)

```

XML se utiliza en una amplia variedad de aplicaciones, como intercambio de datos, configuración de archivos, almacenamiento de datos estructurados, etc. Se utiliza comúnmente en servicios web, como formato de mensaje en SOAP (Simple Object Access Protocol) y para representar datos en RESTful APIs.

Puedes encontrar XML en muchos lugares, como archivos de configuración, datos estructurados en la web, intercambio de datos entre sistemas, etc.

> En resumen, XML es un formato de datos flexible y ampliamente utilizado que se puede manipular fácilmente en Python utilizando bibliotecas como ElementTree y lxml.

## Modulo

**xml.dom.minidom** es un módulo en la biblioteca estándar de Python que proporciona una implementación mínima del Modelo de Objeto de Documento (DOM) para XML. DOM es una forma estándar de representar y manipular documentos XML como una estructura de árbol en la memoria.

xml.dom.minidom permite **parsear** y **manipular** documentos XML de manera similar a como lo harías con otros módulos XML, como xml.etree.ElementTree o lxml, pero con una interfaz diferente.

Aquí hay un ejemplo básico de cómo usar xml.dom.minidom para parsear y manipular un documento XML:


```python
import xml.dom.minidom

# Parsear un documento XML
dom_tree = xml.dom.minidom.parse("archivo.xml")

# Obtener el elemento raíz del árbol
root = dom_tree.documentElement

# Obtener todos los elementos con un tag específico
elementos = dom_tree.getElementsByTagName("elemento")

# Iterar sobre los elementos y acceder a sus atributos y texto
for elemento in elementos:
    print("Tag:", elemento.tagName)
    print("Atributos:", elemento.attributes.items())
    print("Texto:", elemento.firstChild.data if elemento.firstChild else "")

```
Dentro del módulo xml.dom.minidom, el método parseString() se utiliza para analizar una cadena que contiene un documento XML en lugar de un archivo XML físico. Toma una cadena como argumento que representa un documento XML y devuelve un objeto Document que representa el árbol DOM generado a partir de esa cadena XML.

Aquí hay un ejemplo básico de cómo usar parseString():

```python
import xml.dom.minidom

xml_string = """
<root>
    <elemento atributo="valor">Texto de ejemplo</elemento>
</root>
"""

dom_tree = xml.dom.minidom.parseString(xml_string)

root = dom_tree.documentElement
elementos = root.getElementsByTagName("elemento")

for elemento in elementos:
    print("Tag:", elemento.tagName)
    print("Atributos:", elemento.attributes.items())
    print("Texto:", elemento.firstChild.data if elemento.firstChild else "")

```

En este ejemplo, xml_string contiene una cadena que representa un documento XML. Luego, parseString() se utiliza para analizar esta cadena y crear un árbol DOM que representa la estructura del documento XML. Luego, puedes trabajar con el árbol DOM como lo harías con un documento XML analizado de un archivo físico.


xml.dom.minidom es útil para situaciones en las que necesitas trabajar con el modelo DOM y prefieres una solución simple y liviana. Sin embargo, en comparación con otras bibliotecas como xml.etree.ElementTree o lxml, xml.dom.minidom puede ser menos eficiente y más verboso para trabajos más grandes debido a su implementación más básica.

Además de xml.dom.minidom, que proporciona una implementación del Modelo de Objeto de Documento (DOM) para XML, y xml.etree.ElementTree y lxml, que ofrecen una forma más eficiente de trabajar con árboles XML, hay otros módulos y bibliotecas en Python que son útiles para trabajar con XML:

1. xml.sax: SAX (Simple API for XML) es una forma de procesar documentos XML de manera secuencial. El módulo xml.sax proporciona una interfaz SAX para Python, lo que permite analizar grandes archivos XML de manera eficiente sin necesidad de cargar todo el documento en la memoria. Es útil para analizar documentos XML de gran tamaño de manera eficiente.

2. xmlrpc.client: Este módulo proporciona una implementación del cliente XML-RPC en Python, que se utiliza para realizar llamadas a procedimientos remotos (RPC) utilizando XML como formato de datos. XML-RPC es un protocolo ligero basado en XML que permite la comunicación entre diferentes sistemas a través de la web.

3. xmlrpc.server: Este módulo proporciona una implementación del servidor XML-RPC en Python, que se utiliza para exponer funciones y métodos como servicios web que pueden ser llamados por clientes remotos a través de XML-RPC.

4. SOAPpy: SOAPpy es una biblioteca para Python que proporciona herramientas para trabajar con SOAP (Simple Object Access Protocol), un protocolo basado en XML para intercambiar mensajes entre sistemas distribuidos. SOAPpy permite crear clientes y servidores SOAP en Python y trabajar con servicios web basados en SOAP.

Estos son algunos de los módulos y bibliotecas más comunes relacionados con XML en Python. Cada uno tiene sus propias características y casos de uso específicos, por lo que la elección del módulo adecuado depende de los requisitos y el contexto de tu proyecto.


[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
