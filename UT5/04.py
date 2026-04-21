# Clase Motor más completa
class Motor:
    def __init__(self, tipo, potencia, cilindrada, combustible):
        self.tipo = tipo           
        self.potencia = potencia    
        self.cilindrada = cilindrada 
        self.combustible = combustible 

    def mostrar_info(self):
        print("Tipo: " + self.tipo)
        print("Potencia: " + str(self.potencia) + " CV")
        print("Cilindrada: " + str(self.cilindrada) + " cm3")
        print("Combustible: " + self.combustible)

# Clase Coche
class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composición: un coche tiene un motor

    def mostrar_info(self):
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Información del motor:")
        self.motor.mostrar_info()

# Crear objetos
motor1 = Motor("Diesel", 120, 1600, "Gasóleo")
coche1 = Coche("Toyota", "Corolla", motor1)

# Mostrar información completa
coche1.mostrar_info()
