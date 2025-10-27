import platform

# Preguntar al usuario si desea ver la información del sistema
respuesta = input("¿Quieres ver la información de tu sistema? (si/no): ")

if respuesta.lower() == "si":
    # Mostrar el menú de opciones
    print("\n¿Qué información quieres ver?")
    print("1. Versión del sistema operativo")
    print("2. Nombre de la máquina")
    print("3. Versión de Python")
    print("4. Arquitectura del sistema")
    print("5. Toda la información")

    # Pedir la opción al usuario
    opcion = input("Elige una opción (1-5): ")

    # Condicionales para mostrar la información correspondiente
    if opcion == "1":
        print("Versión del sistema:", platform.version())

    elif opcion == "2":
        print("Nombre de la máquina:", platform.node())

    elif opcion == "3":
        print("Versión de Python:", platform.python_version())

    elif opcion == "4":
        print("Arquitectura del sistema:", platform.architecture()[0])

    elif opcion == "5":
        print("Información completa del sistema:")
        print(platform.uname())

    else:
        print("Opción no válida.")

elif respuesta.lower() == "no":
    print("De acuerdo, no se mostrará la información del sistema.")

else:
    print("Respuesta no reconocida. Por favor, escribe 'si' o 'no'.")
