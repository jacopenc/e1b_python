# Clase Curso
class Curso:
    def __init__(self, codigo, nombre, tutor):
        self.codigo = codigo     
        self.nombre = nombre     
        self.tutor = tutor       

    def mostrar_info(self):
        print("Código del curso: " + self.codigo)
        print("Nombre del curso: " + self.nombre)
        print("Tutor: " + self.tutor)


# Clase Alumno
class Alumno:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre   # Nombre del alumno
        self.edad = edad       # Edad
        self.curso = curso     # Composición: Alumno pertenece a un Curso

    def estudiar(self):
        print(self.nombre + " está estudiando")

    def mostrar_info(self):
        print("Nombre del alumno: " + self.nombre)
        print("Edad: " + str(self.edad))
        print("Curso del alumno:")
        self.curso.mostrar_info()   # Mostrar info del curso


# ------------------ Programa principal ------------------

# Crear curso
curso1 = Curso("1Eb", "2º ASIR", "D. José Acosta")

# Crear alumno asociado al curso
alumno1 = Alumno("Ana", 18, curso1)

# Mostrar información completa
alumno1.mostrar_info()
alumno1.estudiar()
