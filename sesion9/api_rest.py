""" 
#API REST 

(Interfaz de Programación de Aplicaciones Representacional por sus siglas en inglés) 
es un conjunto de reglas y convenciones que permite a sistemas informáticos comunicarse entre sí a través de Internet de una manera estándarizada y uniforme.

Una API REST utiliza el protocolo HTTP para realizar operaciones sobre recursos, donde cada recurso es una entidad que puede ser accedida o manipulada a través de la API. 
Estos recursos están identificados por URLs (Uniform Resource Locators) y pueden ser cualquier tipo de datos, como documentos, imágenes, videos, usuarios, etc.

Las APIs REST están basadas en el concepto de "estado del sistema" y "operaciones de transferencia de estado representacional" (REST), 
lo que significa que los servicios web RESTful permiten a los clientes realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre los recursos utilizando los métodos HTTP estándar (GET, POST, PUT, DELETE).

En resumen, una API REST proporciona una forma estándar y uniforme para que aplicaciones informáticas interactúen entre sí a través de Internet, permitiendo el intercambio de datos de manera eficiente y confiable.

#200

El código de estado HTTP 200 es una respuesta exitosa que indica que la solicitud se ha completado correctamente. 
En el contexto de una API REST, recibir un código de estado 200 significa que la solicitud fue procesada con éxito por el servidor y que se ha devuelto la respuesta esperada.

Un "request" (o solicitud) es una acción que realiza un cliente para obtener información o realizar una operación en un servidor a través de una red, típicamente utilizando el protocolo HTTP (Hypertext Transfer Protocol) en el contexto de la web.

En el contexto de una API REST, una solicitud (request) se refiere a la acción que realiza un cliente para interactuar con un servicio web RESTful. Esta solicitud puede ser de varios tipos, como:

GET: Se utiliza para recuperar datos de un recurso específico en el servidor.
POST: Se utiliza para enviar datos nuevos al servidor para que los procese y los almacene.
PUT: Se utiliza para actualizar datos de un recurso existente en el servidor.
DELETE: Se utiliza para eliminar un recurso específico en el servidor.
PATCH: Se utiliza para realizar una actualización parcial de un recurso existente en el servidor.
Además del tipo de solicitud, una solicitud HTTP también puede incluir otros elementos importantes, como:

URL (Uniform Resource Locator): La dirección del recurso en el servidor al que se está accediendo.
Encabezados (Headers): Información adicional que se envía junto con la solicitud, como datos de autenticación, tipo de contenido, etc.
Cuerpo de la Solicitud (Request Body): Datos opcionales que se envían junto con la solicitud, como parámetros de consulta (en el caso de solicitudes GET), datos de formulario (en el caso de solicitudes POST), o datos JSON (en el caso de solicitudes PUT o PATCH).

#
 """
#obterener libreria
#modulos de python >> pypi.org

# https://jsonplaceholder.typicode.com/users 

import requests 
import csv # importa el módulo CSV (Comma Separated Values) en Python. El módulo CSV proporciona funciones para trabajar con archivos CSV, lo que facilita la lectura y escritura de datos en formato CSV


# Realizar la solicitud GET
response = requests.get('https://jsonplaceholder.typicode.com/users') # endpoint
#print(response.text) #imprime todo como texto
lista_usuario = response.json() #convertir cadena en lista convencional >> Convertir la respuesta JSON en un objeto Python

#print(len(data)) # inmprime una lista de diccionario del archivo json / con "len" te indica el numero de usuarios de esa lista

# Ejercicio:

# ********* Bajar los usuarios y guardarlos en un fichero en formato CSV (id, sername, email, website) ***************

# Definir los campos que se desean guardar en el archivo CSV
campos_encabezados = ['id', 'username', 'email', 'website']

# Especificar el nombre del archivo CSV donde vamos guardar los usuarios del URL 
nombre_archivo = 'usuarios.csv'

# Escribir los datos en el archivo CSV
with open(nombre_archivo, 'w') as archivo_csv:
    # Escribir el encabezado/ titulos de los campos del archivo CSV
    archivo_csv.write('***'.join(campos_encabezados) + '\n')    
    # Iterar/recorrer sobre los usuarios del JSON y escribir cada uno en el archivo CSV bajo su campo encabezado correspondiente
    for usuario in lista_usuario:
        fila = '---'.join([str(usuario[campo_usuario]) for campo_usuario in campos_encabezados]) # comprensión de lista
        archivo_csv.write(fila + '\n')

print(f"Los datos de los usuarios se han guardado en el archivo '{nombre_archivo}' en formato CSV.")
