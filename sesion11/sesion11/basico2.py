from cuenta_bancaria import Cuenta_Bancaria


if __name__ == "__main__":

    cuenta = Cuenta_Bancaria(400.0, 'Juan Palomo')

    try:
        cuenta.realizar_deposito(100.0)

        print("Saldo actual tras ingreso 100 eur es de", cuenta.obtener_saldo(), "euros")

        cuenta.realizar_retiro(300.0)

        print("Saldo actual es de", cuenta.obtener_saldo(), "euros")

        cuenta.realizar_retiro(200.0)
        print("Saldo actual es de", cuenta.obtener_saldo(), "euros")

        cuenta.realizar_retiro(50.0)
    except Exception as ex:
        print(ex)
    finally:
        print("Operacion fnalizada")

