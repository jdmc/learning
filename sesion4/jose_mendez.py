"""
Primeros pasos; definir segun info disponible que variables o como se llamen (?) necesito:

    day_temp_min [lista]
    day_temp_max[lista]
    week_temp_min
    week_temp_max
    weekdays [lista] > days of week = day
    temp_average > dividir
    
    NTH:
    
    Dia Max + temp
    Dia Min + temp
"""
def main():
    
    # Definir los días de la semana
    def weekdays():
        return ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    
    # Lista para almacenar todas las temperaturas ingresadas durante la semana
    week_temp = []
 
    # Definir los días de la semana para proporcionar una lista de los días de la semana. Esta incluido dentro de main ya que solo se utiliza dentro de la funcion 'main'
    days_of_week = weekdays()
    
     # Inicializar las variables para la temperatura máxima y mínima de la semana con('inf') = infinito, estás asignándole el valor más bajo (-)/ alto posible 
    max_temp_of_week = float('-inf')  # Inicializar con un valor muy bajo, siempre debe llevar un valor de partida
    min_temp_of_week = float('inf')   # Inicializar con un valor muy alto
 
    # Entrada de datos usuario, puedo usar float o int para definir las entradas numéricas
    print("Ingrese las temperaturas máximas y mínimas para cada día de la semana segun aparecen:")
    for day in days_of_week:
        # Solicitar al usuario que ingrese las temperaturas para el día actual
        day_temp_max = float(input(f"Ingrese la temperatura máxima para el {day}: "))
        day_temp_min = float(input(f"Ingrese la temperatura mínima para el {day}: "))
 
        # MODO TUPLA ***************
        # Agregar (append) una tupla (day_temp_max, day_temp_min) con los valores obtenidos por el usuario a la lista de temperaturas (week_temp)
        week_temp.append((day_temp_max, day_temp_min))
        
        # Días Max y Min, Utilizar day_temp_max y day_temp_min de tupla DENTRO DEL FOR!!!
        if day_temp_max > max_temp_of_week: # si la temp de entrada del día es más alta que la MAX
            max_temp_of_week = day_temp_max # la MAX temp de la semana es igual al temp MAX del día
            max_day_with_temp = day         # el día que destaca es el día con la MAX temp
        if day_temp_min < min_temp_of_week: # si la temp de entrada del día es más baja que la MIN
            min_temp_of_week = day_temp_min # la MIN temp de la semana es igual al temp MIN del día
            min_day_with_temp = day         # el día que destaca es el día con la MIN temp
    
    # Sumar los día con min y los días con max de la semana. Las temperaturas tupla [0] = day_temp_max / [1] = day_temp_min
    total_week_temp_max = sum(tupla[0] for tupla in week_temp)  # Sumar solo las temperaturas máximas
    total_week_temp_min = sum(tupla[1] for tupla in week_temp)  # Sumar solo las temperaturas mínimas
 
    # END MODO TUPLA ***************

    # promedio semanal de las temperaturas min y max, donde (len) pilla número de elementos en el objeto (days_of_week). Si conozco los elementos en este caso 7 días puedo ponerlo igualmente
    average_temp_max = total_week_temp_max / len(days_of_week) 
    average_temp_min = total_week_temp_min / 7
 
    # Mostrar el promedio de las temperaturas máximas y mínimas de la semana
    print("Promedio de temperatura máxima de la semana:", average_temp_max)
    print("Promedio de temperatura mínima de la semana:", average_temp_min)
    
  # Mostrar el día con la temperatura máxima y mínima de la semana
    print("Día con la temperatura máxima de la semana:", max_day_with_temp)
    print("Temperatura máxima registrada durante la semana:", max_temp_of_week)
    print("Día con la temperatura mínima de la semana:", min_day_with_temp)
    print("Temperatura mínima registrada durante la semana:", min_temp_of_week)

if __name__ == "__main__":
    main()
    
"""
# MODO LISTA **************

# Lista para almacenar todas las temperaturas ingresadas durante la semana

    # Agregar las temperaturas a la lista
    week_temp.append(day_temp_max)
    week_temp.append(day_temp_min)
        
    # Encontrar la temperatura máxima y mínima de la semana
    week_temp_max = max(week_temp)
    week_temp_min = min(week_temp)
    
    # Calcular el promedio semanal de las temperaturas lista
    total_week_temp_max = sum(week_temp[::2])  # Sumar solo las temperaturas máximas, crea una nueva lista que contiene solo los elementos en posiciones pares 0,2,4
    total_week_temp_min = sum(week_temp[1::2]) # Sumar solo las temperaturas mínimas

""" 