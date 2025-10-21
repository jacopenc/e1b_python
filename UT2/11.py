# Mostrar opciones de sistemas operativos
print("Elige tu Sistema Operativo:")
print("1. Windows")
print("2. Linux")
print("3. macOS")

# Pedir al usuario que elija uno
opcion = input("Escribe el número de tu elección: ")

# Usar match-case para manejar la elección
match opcion:
    case "1":
        print("Has elegido Windows")
        instruccion = input("Escribe un comando para ejecutar en Windows: ")
        print("Ejecutando el comando en Windows:", instruccion)
    case "2":
        print("Has elegido Linux")
        instruccion = input("Escribe un comando para ejecutar en Linux: ")
        print("Ejecutando el comando en Linux:", instruccion)
    case "3":
        print("Has elegido macOS")
        instruccion = input("Escribe un comando para ejecutar en macOS: ")
        print("Ejecutando el comando en macOS:", instruccion)
    case _:
        print("Opción no válida")
