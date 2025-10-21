# Pedimos el nombre con input (prompt)
nombre = input("¿Cómo te llamas? ")

# Mostramos un pequeño menú
print()
print("Menú de opciones:")
print("1. Saludar")
print("2. Mostrar edad")
print("3. Despedirse")

# Pedimos la opción
opcion = input("Elige una opción (1-3): ")

# Usamos match-case para manejar las opciones
match opcion:
    case "1":
        # Verificamos con un if si el nombre no está vacío
        if nombre == "":
            print("No introduciste ningún nombre")
        else:
            print("Hola,", nombre)
    case "2":
        edad = input("¿Cuántos años tienes? ")
        print("Tienes", edad, "años")
    case "3":
        print("Hasta luego")
    case _:
        print("Opción no válida")
