def obtener_promedio_asignaturas(asignaturas: dict) -> list: # que devuelve? -> una lista
    lista_promedios = list() # lista de tuplas
    for asignatura, calificaciones in asignaturas.items(): #recorrer diccionario "items" recorrido por pares 
        promedio_asignatura = calcular_promedio(calificaciones)
        lista_promedios.append ((asignatura, promedio_asignatura))
    
    return lista_promedios

def calcular_promedio(lista_notas: list) -> float: # promedio "float"
    return round(sum(lista_notas) / len(lista_notas),2)
    