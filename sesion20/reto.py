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



def buscar_email(nombre: str)-> str:
    try:
        return friend_emails[nombre]
    except KeyError:
        return "no encontrado"
        
if __name__ == "__main__":
    
    nombre = input("Ingrese nombre amigo: ")
    email = buscar_email(nombre)
    print(email)
    
    
def find_lowest(temperatures: list) -> int:
    #return min(temperatures)
    
    """ temperatures.sort()
    lowest = temperatures[0]
    return lowest """

    sorted_temps = sorted(temperatures)
    return sorted_temps[0]

if __name__ == "__main__":
    temps = [85, 76, 79, 72, 10, 81]
    lowest = find_lowest(temps)
    print(lowest)