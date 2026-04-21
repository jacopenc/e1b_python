class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def estudiar(self):
        print("El alumno está estudiando")

    def cambiar_nota(self, nueva_nota):
        self.nota = nueva_nota
        print("La nota ha sido actualizada")

    def mostrar_info(self):
        print("Nombre: " + self.nombre)
        print("Nota: " + str(self.nota))

    def esta_aprobado(self):
        if self.nota >= 5:
            print("El alumno está aprobado")
        else:
            print("El alumno está suspenso")


# Programa principal
alumno1 = Alumno("Ana", 7)

alumno1.mostrar_info()
alumno1.estudiar()
alumno1.esta_aprobado()
alumno1.cambiar_nota(4)
alumno1.esta_aprobado()
