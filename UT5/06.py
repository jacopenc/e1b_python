class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy " + self.nombre)

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)  # Hereda atributos
        self.curso = curso

    def estudiar(self):
        print(self.nombre + " está estudiando " + self.curso)

# Uso
e1 = Estudiante("Ana", 18, "Matemáticas")
e1.saludar()   # heredado de Persona
e1.estudiar()  # propio de Estudiante
