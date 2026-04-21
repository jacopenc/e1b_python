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

    @staticmethod
    def transferir(origen, destino, cantidad):
        if cantidad > origen.saldo:
            print("No se puede transferir, saldo insuficiente")
        else:
            origen.saldo -= cantidad
            destino.saldo += cantidad
            print("Transferencia realizada")



cuenta1 = CuentaBancaria("Jose", 1000)
cuenta2 = CuentaBancaria("Ana", 500)

cuenta1.mostrar_info()
cuenta1.ingresar(500)


CuentaBancaria.transferir(cuenta1, cuenta2, 300)

cuenta1.mostrar_info()
cuenta2.mostrar_info()