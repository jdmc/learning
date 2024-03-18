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


[Back2Index](https://github.com/jdmc/learning/blob/master/notes.md) 
