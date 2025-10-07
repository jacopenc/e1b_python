# Ejemplo de control de cast con otros datos

try:
    peso = float(input("Indica peso en kilogramos "))
    nota = int(input("Dime nota de último examen (0-10)? "))
except ValueError:
    print("Error: Debes escribir valores validos.")
    peso = 0.0
    nota = 0

print("Peso:", peso, "kg")
print("Nota del examen:", nota)
