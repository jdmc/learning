""" 

La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. 
12Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito. """


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_mins = hour * 60 + mins + dura

print(total_mins)

minutos = mins + dura

print(minutos)

hour_conv= total_mins // 60
min_conv_rest = total_mins % 60

print(hour_conv)
print(min_conv_rest) 

print("Tiempo final es:", hour_conv,":", min_conv_rest)