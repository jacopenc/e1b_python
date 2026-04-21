# coche.py
# Ejemplo básico de clase Coche 

class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0

    def arrancar(self):
        print("El coche ha arrancado")

    def acelerar(self, cantidad):
        self.velocidad = self.velocidad + cantidad
        print("Velocidad actual: " + str(self.velocidad) + " km/h")

    def frenar(self):
        self.velocidad = 0
        print("El coche se ha detenido")

    def mostrar_info(self):
        print("Marca: " + self.marca)
        print("Color: " + self.color)
        print("Velocidad: " + str(self.velocidad) + " km/h")


# Programa principal
coche1 = Coche("Toyota", "rojo")

coche1.mostrar_info()
coche1.arrancar()
coche1.acelerar(50)
coche1.frenar()
coche1.mostrar_info()