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
    def __init__(self, saldo, titular):
        self__saldo= saldo
        self__titular = titular
            
    #Obtener el saldo actual (obtener_saldo)
    
    #Realizar un depósito (realizar_deposito)
    
    #Realizar un retiro (realizar_retiro)
    
    #titular +   #saldo inicial
    
cuenta_bancaria1 = CuentaBancaria(10, "Juan")
    