friend_emails = {
    "Anne": "anne@example.com",
    "Brent": "brent@example.com",
    "Dan": "dan@example.com",
    "David": "david@example.com",
    "Fox": "fox@example.com",
    "Jane": "jane@example.com",
    "Kevin": "kevin@example.com",
    "Robert": "robert@example.com"
}



#preguntar el nombre del amigo para buscar su correo.
# controlando los posibles errores (main errors)
#proceso de busqueda enmarcado en una funcion
#Tiempo: 8 min

nombre = input("Ingrese nombre amigo: ")

def buscar_correo(correo):
    if correo in friend_emails:
        print(f"El correo {correo} pertenece al amigo {nombre}")
    else:
        print(f"El correo {correo} no pertenece al amigo {nombre}")