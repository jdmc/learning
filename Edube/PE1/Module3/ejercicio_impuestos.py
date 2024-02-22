""" Érase una vez una tierra de leche y miel, habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto, su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
Tu tarea es escribir una calculadora de impuestos.

Debe aceptar un valor de punto flotante: el ingreso.
A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el código de esqueleto del editor. """

# income =< 85.528 => low tax else high tax


# low_tax = 18% - (556 - 0.02)
# high_tax = 32% + (14,839 + 0.02)

# total = income + (low/high_)tax

# tax = total - income 

# Ingreso del ciudadano "feliz"
income = float(input("Introduce el ingreso anual:"))

limit = 85528

#calcular impuesto
if income <= limit:
    ipi = round((income * 0.18) -  556.02) # total 
    if ipi <= 0:
        ipi = 0
    print("total impuesto bajo", ipi)
else:
    ipi = round(((income - limit) * 0.32) + 14839.02) # total 
    print("total impuesto alto", ipi)

print("El impuesto es:", ipi, "pesos")


# Ingreso del ciudadano
ingreso = float(input("Ingrese el ingreso anual: "))

# Límite para la exención fiscal
limite_exencion = 85528

# Calcular el impuesto
if ingreso <= limite_exencion:
    impuesto = round((ingreso * 0.18) - 556.02)
    if impuesto < 0:
        impuesto = 0
else:
    impuesto = round(14839.02 + ((ingreso - limite_exencion) * 0.32))

# Imprimir el impuesto calculado
print("El impuesto calculado es:", impuesto, "pesos")
