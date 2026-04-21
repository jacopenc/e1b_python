class Curso:
    def __init__(self, codigo, nombre, tutor):
        self.codigo = codigo     
        self.nombre = nombre     
        self.tutor = tutor       

    def mostrar_info(self):
        print("Código del curso: " + self.codigo)
        print("Nombre del curso: " + self.nombre)
        print("Tutor: " + self.tutor)

class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.curso = None   # inicialmente sin curso

    def set_curso(self, curso):
        self.curso = curso
        print("Curso asignado correctamente")

    def estudiar(self):
        print(self.nombre + " está estudiando")

    def mostrar_info(self):
        print("Nombre del alumno: " + self.nombre)
        print("Edad: " + str(self.edad))

        if self.curso:
            print("Curso del alumno:")
            self.curso.mostrar_info()
        else:
            print("El alumno no tiene curso asignado")

# cursos
curso1 = Curso("1EB", "2º ASIR", "D. José Acosta")
curso2 = Curso("2DAW", "1º DAW", "Dña. Marta López")

# alumnos
alumno1 = Alumno("Ana", 18)
alumno2 = Alumno("Luis", 20)
alumno3 = Alumno("Carlos", 19)

# asignar cursos
alumno1.set_curso(curso1)
alumno2.set_curso(curso2)
# alumno3 se queda sin curso a propósito

# Mostrar info
alumno1.mostrar_info()
print()
alumno2.mostrar_info()
print()
alumno3.mostrar_info()