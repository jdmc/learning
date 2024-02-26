""" 
Define una clase llamada CuentaBancaria con los siguientes atributos privados:
    • saldo: un atributo para almacenar el saldo de la cuenta (debe comenzar con un valor predeterminado). 
    • titular: un atributo para almacenar el nombre del titular de la cuenta. 
    
    1.Agrega métodos públicos para: 
        
        • Obtener el saldo actual (obtener_saldo). 
        • Realizar un depósito (realizar_deposito) que aumenta el saldo. 
        • Realizar un retiro (realizar_retiro) que disminuye el saldo. 
        
    2.Implementa la encapsulación adecuada para que los atributos saldo y titular solo puedan ser modificados internamente. >> @property
    3.Crea una instancia de la clase CuentaBancaria e inicialízala con un saldo inicial y el nombre del titular. 
    4.Realiza algunas operaciones de depósito y retiro utilizando los métodos definidos. 
    
    cuenta_bancaria modulo    
    
    """
    
class CuentaBancaria:
    def __init__(self, saldo_inicial, titular):
        self.__saldo = saldo_inicial
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    def obtener_saldo(self):
        return self.__saldo

    def realizar_deposito(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.__saldo}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def realizar_retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.__saldo}.")
        else:
            print("Cantidad no válida o saldo insuficiente.")

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria(1000, "Juan Pérez")

# Realizar algunas operaciones de depósito y retiro
cuenta.realizar_deposito(500)
cuenta.realizar_retiro(200)
cuenta.realizar_retiro(1500)  # Intentar retirar más de lo que hay en la cuenta

# Obtener el saldo actual
print("Saldo actual:", cuenta.obtener_saldo())

""" 
Explicación:

1. La clase CuentaBancaria define dos atributos privados: _saldo y _titular.
2. Se definen métodos públicos para:
       a) Obtener el saldo actual (obtener_saldo): 
       Se usa la propiedad @property para acceder al atributo _saldo. 
       b) Realizar un depósito (realizar_deposito): 
       Se incrementa el valor de _saldo.
       c) Realizar un retiro (realizar_retiro): 
       Se verifica que el monto a retirar sea menor o igual al saldo actual. 
       Si es así, se decrementa el valor de _saldo. De lo contrario, se muestra un mensaje de error.
3.Se crea una instancia de la clase CuentaBancaria con un saldo inicial y el nombre del titular.
4.Se realizan operaciones de depósito y retiro utilizando los métodos definidos.
5. Se muestra información de la cuenta usando el método __str__.
       
       
2* >> Se utilizan decoradores @property para definir métodos para obtener los valores de los atributos privados (saldo y titular), 
asegurando así que no se puedan modificar externamente.
Se definen métodos públicos realizar_deposito y realizar_retiro para realizar operaciones de depósito y retiro, respectivamente.
Se crea una instancia de CuentaBancaria con un saldo inicial y el nombre del titular.
Se realizan algunas operaciones de depósito y retiro utilizando los métodos definidos.
Se obtiene el saldo actual de la cuenta utilizando el método obtener_saldo.

Se implementa la encapsulación usando @property para el getter de saldo.
Se crea una instancia de la clase y se inicializa con un saldo inicial y el nombre del titular.
Se realizan operaciones de depósito y retiro usando los métodos definidos.
Se imprime la información de la cuenta usando el método __str__.


Encapsulación:

Los atributos _saldo y _titular son privados y solo pueden ser modificados internamente por la clase.

Getter:

El método @property saldo permite obtener el valor del atributo _saldo de forma pública.
 """