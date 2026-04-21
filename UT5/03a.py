class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Depósito realizado. Saldo actual: " + str(self.saldo))

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - cantidad
            print("Retiro realizado. Saldo actual: " + str(self.saldo))

    def mostrar_info(self):
        print("Titular: " + self.titular)
        print("Saldo: " + str(self.saldo))


# Programa principal
cuenta1 = CuentaBancaria("Luis", 1000)

cuenta1.mostrar_info()
cuenta1.ingresar(500)
cuenta1.retirar(200)
cuenta1.retirar(2000)
